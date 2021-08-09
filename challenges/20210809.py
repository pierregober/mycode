#!/usr/bin/python3

import requests
import datetime

# importing necessary libraries
import reverse_geocoder as rg
import pprint

URL = "http://api.open-notify.org/iss-now.json"

# city = None


def reverseGeocode(coordinates):
    result = rg.search(coordinates)

    # result is a list containing ordered dictionary.
    # pprint.pprint(result[0]['name'])
    city = result[0]['name']
    return city


def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp = requests.get(URL).json()
    dataLocation = resp["iss_position"]
    convertedTime = datetime.datetime.fromtimestamp(resp['timestamp'])

    # Part Un
    print('=====Part Un===================================')
    print('CURRENT LOCATION OF THE ISS: ')
    print('Lon: ' + dataLocation['longitude'])
    print('Lat: ' + dataLocation['latitude'])
    print('===============================================')

    # Part deux
    print('====Part Deux==================================')
    print('CURRENT LOCATION OF THE ISS: ')
    print('Timestamp: ', convertedTime)
    print('Lon: ' + dataLocation['longitude'])
    print('Lat: ' + dataLocation['latitude'])
    print('===============================================')

    # Prep for part trois
    coordinates = (dataLocation['longitude'], dataLocation['latitude'])
    city = reverseGeocode(coordinates)

    # Part Trois
    print('====Part Trois=================================')
    print('CURRENT LOCATION OF THE ISS: ')
    print('Timestamp: ', convertedTime)
    print('Lon: ' + dataLocation['longitude'])
    print('Lat: ' + dataLocation['latitude'])
    print('City: ', city)
    print('===============================================')


if __name__ == "__main__":
    main()
