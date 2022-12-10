import utils
import chart
import read_csv

def run():
  data = read_csv.read_csv('.\world_population.csv')
  country = input('Type Country -> ')

  result = utils.population_by_country(country, data)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    chart.generate_bar_chart(labels, values)
   
  print(result)

if __name__ == '__main__':
  
  run()