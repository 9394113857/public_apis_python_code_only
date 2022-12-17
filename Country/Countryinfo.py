from countryinfo import CountryInfo
user_country = input("Enter Country Name: ")
country_info_gathered = CountryInfo(user_country)

data = country_info_gathered.info()
for i, j in data.items():
  print(f"{i}:>>{j}")

# https://thecleverprogrammer.com/2021/04/12/countryinfo-in-python-tutorial/