import matplotlib.pyplot as plt
import csv

def get_population():
  keys = ['col', 'bol']
  values = [300, 450]
  return keys, values

def population_by_country(country, data):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

 
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.show()

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header,row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data