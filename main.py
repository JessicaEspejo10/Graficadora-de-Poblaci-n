import utils
import chart
import read_csv

def run_country_population(data):
  country = input('Type Country -> ')
  result = utils.population_by_country(country, data)
  
  if len(result) > 0:
    country_1 = result[0]
    labels, values = utils.get_population(country_1)
    chart.generate_bar_chart(labels, values, country)
   
  #print(result)
   # como hacer que las etiquetas no se vean montadas, ajustar etiquetas y mostrar valores
def run_percent_population(data):
  print('\n Graficaremos la población de los paises de mayor a menor')
  num_countries = input('¿Cuántos paises deseas graficar?: ')
  labels, values = utils.get_world_percentage(data, int(num_countries))
  title = 'Top ' + num_countries + ' Countries with more population'
  chart.generate_pie_chart(labels, values, title)

def run_continent_percent(data):
  index = input('\nIndique el continente que desea graficar: \n 1 - Asia \n 2 - Europe \n 3 - Africa \n 4 - Oceania \n 5 - North America \n 6 - South America')
  continents = ['Asia', 'Europe', 'Africa', 'Oceania', 'North America', 'South America']
  cont_selected = continents[int(index)-1]
  labels, values = utils.get_continent_percentage(data, cont_selected)
  title = 'Population of ' + cont_selected
  chart.generate_pie_chart(labels, values, title)
  

def menu(data):
  print('\nBIENVENIDO A LA GRAFICADORA DE POBLACIÓN\n')
  option = input('---------Menú ---------\n 1 - Graficar la población histórica de un país específico \n 2 - Graficar porcentaje de población por paises \n 3 - Graficar porcentaje de población por Continente\n')
  if option == '1':
    run_country_population(data)
  elif option == '2': 
    run_percent_population(data)
  elif option == '3':
    run_continent_percent(data)
  else:
    print('La opción que ingresó no es válida')
    menu(data)

if __name__ == '__main__':
  data = read_csv.read_csv('.\world_population.csv')
  menu(data)
    
