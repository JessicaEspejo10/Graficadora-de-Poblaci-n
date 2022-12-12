import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  ax.set_xlabel('Year')
  ax.set_ylabel('Population')
  ax.set_title('Historical population of ' + str(country))
  plt.savefig('historical_' + str(country) + '.png')
  plt.show()

def generate_pie_chart(labels, values, title):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels, autopct='%1.1f%%', shadow=True, startangle=180, textprops={'fontsize' : 8}, pctdistance=0.8)
  ax.axis('equal')
 
  ax.set_title(title)
  plt.show()
  
if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'd']
  values = [100, 250, 320, 500]
  #generate_bar_chart(labels, values)
  title = 'prueba'
  generate_pie_chart(labels, values, title)