import phonenumbers
from phonenumbers import carrier

# my_string_number = "+40021234567"

my_string_number = "+91"
user_number = input("Enter Your Number: ")
my_number = phonenumbers.parse(my_string_number + user_number)

print(carrier.name_for_number(my_number, "en"))