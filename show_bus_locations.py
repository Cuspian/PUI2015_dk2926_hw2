# Importing libraries to work with JSON, command line input and URL requesting
import json
import sys
import urllib2 as ulib

if __name__ == '__main__':
    # Reading the arguments API_key(1) and Bus_Line_Name(2) from the command
    # line input
    API_key = sys.argv[1]
    Bus_Line_Name = sys.argv[2]
    # Generating request URL to obtain the data about the MTA Buses
    MTA_URL = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (
        API_key, Bus_Line_Name)
    print "Requesting MTA BUS data from %s" % (MTA_URL)
    print "Bus line: %s" % (Bus_Line_Name)
    # Requesting the data with the URL
    Request = ulib.urlopen(MTA_URL)
    Bus_Data = json.loads(Request.read())
    # Parsing the JSON data to obtain the locations of the buses
    Bus_Location = Bus_Data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    # Counting active buses
    Bus_Count = len(Bus_Location)
    print "Number of Active Buses: "+str(Bus_Count)
    # Printing out the longitude and latitude of the active buses
    for i in range(0, Bus_Count):
        Bus_Latitude = Bus_Location[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Latitude']
        Bus_Longitude = Bus_Location[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Longitude']
        print "Bus %s is at latitude %s and longitude %s" % (str(i), str(Bus_Latitude), str(Bus_Longitude))
