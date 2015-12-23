import folium
import csv
import sys

# Read in the database.  Using Sniffer allows us to determine the CSV format
# automatically
dialect = csv.Sniffer().sniff(open("zips.csv").read(1000))
zips = dict(
    [x['zip code'], x] for x in csv.DictReader(
        open("zips.csv"), dialect=dialect))

# find the entry for the specified zip code
zipcode = sys.argv[1]
entry = zips[zipcode]
city = entry['city']
longitude = float(entry['longitude'])
latitude = float(entry['latitude'])

print "zip code =", zipcode
print "city =", city
print "latitude =", latitude
print "longitude =", longitude

# create an HTML map
map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
map_osm.create_map(path='map.html')
