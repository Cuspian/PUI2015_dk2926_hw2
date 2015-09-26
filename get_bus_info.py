# Importing libraries to work with JSON, command line input and URL
# requesting, csv
import json
import sys
import urllib2 as ulib
import csv

if __name__ == '__main__':
    # Reading the arguments API_key(1), Bus_Line_Name(2) and CSV_Name(3) from
    # the command line input
    API_key = sys.argv[1]
    Bus_Line_Name = sys.argv[2]
    CSV_Name = sys.argv[3]
    # Generating request URL to obtain the data about the MTA Buses
    MTA_URL = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (
        API_key, Bus_Line_Name)
    print "Requesting MTA BUS data from %s" % (MTA_URL)
    print "Bus line: %s" % (Bus_Line_Name)
    # Requesting the data with the URL
    Request = ulib.urlopen(MTA_URL)
    Bus_Data = json.loads(Request.read())

    # StopPointName
    # Parsing the JSON data to obtain the locations of the buses
    Bus_Location = Bus_Data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    # Creating or rewriting a CSV file to store the results
    with open(CSV_Name, 'wb') as CsvFile:
        Writer = csv.writer(CsvFile)
        Headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        Writer.writerow(Headers)
        # Counting active buses
        Bus_Count = len(Bus_Location)
        print "Number of Active Buses: "+str(Bus_Count)
        # Loop to parse the Bus Info about the latitude, longitude, stop name
        # and stop status
        for i in range(0, Bus_Count):
            Bus_Latitude = Bus_Location[i]['MonitoredVehicleJourney'][
                'VehicleLocation']['Latitude']
            Bus_Longitude = Bus_Location[i]['MonitoredVehicleJourney'][
                'VehicleLocation']['Longitude']
            # Checking if the OnwardCalls is not empty
            if Bus_Location[i]['MonitoredVehicleJourney']['OnwardCalls'] is not None:
                Stop_Status = Bus_Location[i]['MonitoredVehicleJourney']['OnwardCalls'][
                    'OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
                Stop_Name = Bus_Location[i]['MonitoredVehicleJourney'][
                    'OnwardCalls']['OnwardCall'][0]['StopPointName']
            else:
                Stop_Status = 'N/A'
                Stop_Status = 'N/A'
            Writer.writerow(
                [Bus_Latitude, Bus_Longitude, Stop_Name, Stop_Status])
            print "Bus %s is at latitude %s and longitude %s stop status %s stop name %s" % (str(i), str(Bus_Latitude), str(Bus_Longitude), Stop_Status, Stop_Name)
