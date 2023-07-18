import http.client
import json
import csv
import re

url = "padax.github.io"  # Replace with the URL of your website
path = "/taipei-day-trip-resources/taipei-attractions-assignment.json"  # Replace with the path to your JSON document

conn = http.client.HTTPSConnection(url)
conn.request("GET", path)
response = conn.getresponse()

data = json.loads(response.read().decode())


def first_jpg_from_string(string):
    pattern = r"https?://[^\s]+?\.[jJ][pP][eE]?[gG]"
    matches = re.findall(pattern, string)

    if matches:
        first_jpg_url = matches[0]
        return(first_jpg_url)
    else:
        return("No JPEG URL found in the string.")

data1 = []
for index in range(len(data["result"]["results"])):
    data1.append([data["result"]["results"][index]['stitle'], data["result"]["results"][index]['address'][5: 8], data["result"]["results"][0]['longitude'],
      data["result"]["results"][index]['latitude'], first_jpg_from_string(data["result"]["results"][index]['file'])])
    

# Specify the CSV file path
csv_file_path = 'attraction.csv'  # Replace with your desired file name and extension

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the data to the CSV file row by row
    for row in data1:
        csv_writer.writerow(row)



data2 = {} # key: value = sight: MRT
for index in range(len(data["result"]["results"])):
    if data["result"]["results"][index]['MRT'] in data2:
        value = data2[data["result"]["results"][index]['MRT']]
        value.append(data["result"]["results"][index]['stitle'])
    else:
        if data["result"]["results"][index]['MRT'] is None:
            data2["無"] = [data["result"]["results"][index]['stitle']]
        else:
            data2[data["result"]["results"][index]['MRT']] = [data["result"]["results"][index]['stitle']]

# Specify the CSV file path
csv_file_path = 'mrt.csv'  # Replace with your desired file name and extension

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.writer(csv_file)

    for attraction, locations in data2.items():
        csv_writer.writerow([attraction] + locations)

