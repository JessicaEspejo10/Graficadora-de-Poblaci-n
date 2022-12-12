import matplotlib.pyplot as plt
from collections import OrderedDict

def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']), 
    '2020': int(country_dict['2020 Population']),  
    '2015': int(country_dict['2015 Population']),  
    '2010': int(country_dict['2010 Population']),  
    '2000': int(country_dict['2000 Population']), 
    '1990': int(country_dict['1990 Population']),  
    '1980': int(country_dict['1980 Population']), 
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(country, data):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_world_percentage(data):
  percent_dict = {item['Country/Territory']: item ['World Population Percentage'] for item in data}
  sorted_percent = OrderedDict(sorted(percent_dict.items(), key = lambda item: item[1], reverse = True))
  percent_res = dict(list(sorted_percent.items())[0:10])  
  labels = percent_res.keys()
  values = percent_res.values()
  return labels, values

def get_continent_percentage(data):
  data = list(filter(lambda item : item ['Continent'] == 'South America', data))
  percent_dict = {item['Country/Territory']: item ['World Population Percentage'] for item in data}
  labels = percent_dict.keys()
  values = percent_dict.values()
  return labels, values

