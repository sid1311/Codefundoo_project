from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import xlrd
from xlwt import Workbook

geolocator = Nominatim(user_agent="codefundoo")
address = input("Enter your location\n")
location = geolocator.geocode(address)
loc1 = (location.latitude,location.longitude)

loc = ("E:\Workspace\Codefundoo\eq_databasenew.xlsx")
wb = xlrd.open_workbook(loc)
sh = wb.sheet_by_index(0)

wb = Workbook()
sheet1 = wb.add_sheet('sheet1')

for i in range (sh.nrows):
    loc2 = (sh.cell_value(i,0), sh.cell_value(i,1))
    distance = geodesic(loc1, loc2).miles
    distance = distance * 1.609
    sheet1.write(i,0,distance)

wb.save('output.xls')