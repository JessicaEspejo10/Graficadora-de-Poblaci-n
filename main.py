import utils

def run(data):
  utils.get_population()
  
  print(utils.population_by_country('Colombia', data))

if __name__ == '__main__':
  data = utils.read_csv('./world_population/world_population.csv')
  run(data)
  print(data)