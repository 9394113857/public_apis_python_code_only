# https://www.makeuseof.com/python-country-data-program-fetch/

from countryinfo import CountryInfo
import pandas as pd

country = CountryInfo()
data = country.all()
print(data)

df = pd.DataFrame(data)
df.to_csv("Country_Data_Fetcher.csv")
