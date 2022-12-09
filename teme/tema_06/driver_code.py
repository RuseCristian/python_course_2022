from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import ExcelWriter

request_page = requests.get("https://frsah.ro/calendar/")
link = BeautifulSoup(request_page.text, 'html.parser')

main = link.find_all('tr', attrs={'class': 'wptb-row'})

dataset = []
for obj in main:
    temp_list = []
    for table_cell in obj.find_all('td', attrs={'class': 'wptb-cell'}):
        temp_list.append(table_cell.text)
    dataset.append(temp_list)
    del temp_list


del dataset[:27]
header_list = dataset[0]


df = pd.DataFrame(dataset, columns=header_list, index=range(1, len(dataset) + 1))
df.to_excel("CompetitiiSah.xlsx", header=header_list)
