import utils
import chart
import read_csv

def run_country_population(data):
  country = input('Type Country -> ')
  result = utils.population_by_country(country, data)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    chart.generate_bar_chart(labels, values)
   
  #print(result)
def run_percent_population(data):
  labels, values = utils.get_world_percentage(data)
  chart.generate_pie_chart(labels, values)

def menu(data):
  print('Bienvenido a la graficadora de población\n')
  print('________________________________________________\n\n')
  option = input('Digite 1 si desea graficar la población histórica de un país, o 2 si desea graficar el porcentaje de población numndial por paises: ')
  if option == '1':
    run_country_population(data)
  elif option == '2':
    run_percent_population(data)
  else:
    print('La opción que ingresó no es válida')
    menu(data)

if __name__ == '__main__':
  data = read_csv.read_csv('.\world_population.csv')
  menu(data)
    
