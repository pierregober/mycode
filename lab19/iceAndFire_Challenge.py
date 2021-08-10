#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def main():

    print('\n\n')
    print('   _____    _______        _                          _                                                        _ ')
    print('  / ____|  |__   __|      | |                        | |                                                      | |')
    print(' | |  __  ___ | |      ___| |__   __ _ _ __ __ _  ___| |_ ___ _ __   _ __  _ __ ___   __ _ _ __ __ _ _ __ ___ | |')
    print(' | | |_ |/ _ \| |     / __| \'_ \ / _` | \'__/ _` |/ __| __/ _ \ \'__| | \'_ \| \'__/ _ \ / _` | \'__/ _` | \'_ ` _ \| |')
    print(' | |__| | (_) | |    | (__| | | | (_| | | | (_| | (__| ||  __/ |    | |_) | | | (_) | (_| | | | (_| | | | | | |_|')
    print('  \_____|\___/|_|     \___|_| |_|\__,_|_|  \__,_|\___|\__\___|_|    | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_(_)')
    print('                                                                    | |               __/ |                      ')
    print('                                                                    |_|              |___/                       ')
    print('\n\n')

    # Ask user for input
    got_charToLookup = input(
        "Pick a number between 1 and 1000 to return info on a GoT character! ")

    # Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    # Decode the response
    got_dj = gotresp.json()
    # pprint.pprint(got_dj)

    # My seperate values of for each detail
    houses = got_dj['allegiances']
    pages = got_dj['books']

    # My Collectors for details
    houseCollector = []
    pagesCollector = []

    if len(pages) > 0:
        for a in pages:
            pag = requests.get(a)
            pagBook = pag.json()['name']
            pagesCollector.append(pagBook)
    else:
        pagesCollector.append("Character doesnt have any references in any books")

    if len(houses) > 0:
        for b in houses:
            houseD = requests.get(b)
            houseDetails = houseD.json()['name']
            houseCollector.append(houseDetails)
    else:
        houseCollector.append("Character doesnt have any houses that they are apart of")

    print("\n\n====================================================")
    print("Name:", got_dj['name'])
    print("Houses:")
    print(*houseCollector, sep=", ")
    print("Books:")
    print(*pagesCollector, sep=", ")
    print("====================================================\n\n")


if __name__ == "__main__":
    main()
