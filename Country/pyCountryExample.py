import pycountry
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-18-2020.csv')


def findCountryAlpha2(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_2
    except:
        return ("not founded!")


def findCountryAlpha3(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except:
        return ("not founded!")


def findCountryNumeric(country_name):
    try:
        return pycountry.countries.get(name=country_name).numeric
    except:
        return ("not founded!")


def findCountryOfficialName(country_name):
    try:
        return pycountry.countries.get(name=country_name).official_name
    except:
        return ("not founded!")


df['country_alpha_2'] = df.apply(lambda row: findCountryAlpha2(row.Country_Region), axis=1)
df['country_alpha_3'] = df.apply(lambda row: findCountryAlpha3(row.Country_Region), axis=1)
df['country_numeric'] = df.apply(lambda row: findCountryNumeric(row.Country_Region), axis=1)
df['official_name'] = df.apply(lambda row: findCountryOfficialName(row.Country_Region), axis=1)
