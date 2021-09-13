import phonenumbers
from phonenumbers.phonenumberutil import parse
from phonenumbers import geocoder
from phonenumbers import carrier

number=input("Enter Your number including country code: ")
chr_number =phonenumbers.parse(number,"CH" )
service_number = phonenumbers.parse(number, "RO") 

Country= geocoder.description_for_number(chr_number,"en")
serviceName = carrier.name_for_number(service_number,"en")

print("Your Number : ",number,"\nDetails")
print("Country: "+ Country)
print("Service: " +serviceName )