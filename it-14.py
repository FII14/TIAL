import argparse
import requests
import os

# Create the argument parser
parser = argparse.ArgumentParser(description='Track IP location.')

# Add the argument for IP address
parser.add_argument('-i', '--ip', type=str, help='The IP address to track')

# Parse the arguments from the command line
args = parser.parse_args()

# Check if the IP address argument is provided
if args.ip:
    ip_address = args.ip
else:
    print("IP address is required. Please provide the IP address using the -i or --ip option.")
    exit(1)

# Make an HTTP request to retrieve location data from the IP-API service
response = requests.get(f"http://ip-api.com/json/{ip_address}")

# Check if the request was successful
if response.status_code != 200:
    print("Failed to track IP location.")
else:
    data = response.json()
    
    # Check if the IP address was found
    if data['status'] == 'fail':
        print("IP address not found.")
    else:
        # Extract location information from the JSON response
        city = data['city']
        region = data['regionName']
        country = data['country']
        zip_code = data['zip']
        lat = data['lat']
        lon = data['lon']
        isp = data['isp']

        os.system("clear")

        # Display the complete location information
        print("")
        print("-------------------------------------------")
        print(f" IP Location Information: {ip_address}")
        print("-------------------------------------------")
        print(f" City: {city}")
        print(f" Region: {region}")
        print(f" Country: {country}")
        print(f" ZIP Code: {zip_code}")
        print(f" Coordinates: {lat}, {lon}")
        print(f" ISP: {isp}")
        print("-------------------------------------------")
        print("")
