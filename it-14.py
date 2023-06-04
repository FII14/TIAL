import argparse
import requests
from colorama import Fore
import os

r=Fore.RED
w=Fore.RESET
g=Fore.GREEN

os.system("clear")

# Create the argument parser
print(f"""{r}
 ._..__   .___..__ .__. __ .  ..___.__
  | [__)    |  [__)[__]/  `|_/ [__ [__)
 _|_|       |  |  \|  |\__.|  \[___|  \.
{w}""")
parser = argparse.ArgumentParser(description='Track IP location.')

# Add the argument for IP address
parser.add_argument('--ip', type=str, help='The IP address to track')

# Add the argument for output file
parser.add_argument('--output', type=str, help='The output file to save the location information')

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

        # Display the complete location information
        print("-----------------------------------------")
        print(f" IP Location Information: {ip_address}")
        print("-----------------------------------------")
        print(f" City: {city}")
        print(f" Region: {region}")
        print(f" Country: {country}")
        print(f" ZIP Code: {zip_code}")
        print(f" Coordinates: {lat}, {lon}")
        print(f" ISP: {isp}")
        print("-----------------------------------------")
        print(f"                           {g}Code by: FII14{w}")
        # Check if the output file argument is provided
        if args.output:
            output_file = args.output
            with open(output_file, 'w') as file:
                file.write("-----------------------------------------\n")
                file.write(f"IP Location Information: {ip_address}\n")
                file.write("-----------------------------------------\n")
                file.write(f"City: {city}\n")
                file.write(f"Region: {region}\n")
                file.write(f"Country: {country}\n")
                file.write(f"ZIP Code: {zip_code}\n")
                file.write(f"Coordinates: {lat}, {lon}\n")
                file.write(f"ISP: {isp}\n")
                file.write("---------------------------------------\n")
                file.write("                         Code by: FII14\n")