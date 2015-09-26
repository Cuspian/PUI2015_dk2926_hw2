This is a repositary for Home Work 2, Principals of Urban Informatics.

Assignment 1 is stored in show_bus_locations.py. It takes 2 arguments from the command line - API_key to access the MTA Bus data
and Bus_Line_Name to set the name of the Bus Line. The program returns a list of the active Buses and their locations, 
defined in latitudes and longitudes.
Example of using the show_bus_locations.py : 
run show_bus_locations.py 84a8b585-00fb-42b9-8f3c-221586ce3e34 B52

Assignment 2 is stored in get_bus_info.py. It takes 3 arguments from the command line - API_key to access the MTA Bus data,
Bus_Line_Name to set the name of the Bus Line and the CSV_Name to set the output csv file. The program returns a list of the 
active Buses, their locations in latitude, longitude, current stop name and stop status. Information is printed on the screen 
and is written to the CSV_Name file.
Example of using the get_bus_info.py : 
run get_bus_info.py 84a8b585-00fb-42b9-8f3c-221586ce3e34 M7 M7.csv
