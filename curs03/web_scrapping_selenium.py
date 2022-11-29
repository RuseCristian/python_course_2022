from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser = webdriver.Chrome

browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")

table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')

header_len = browser.find_element( by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')


dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        print(header[int(j)], lista[i])
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))

print(dictionar)

df = pd.DataFrame(dictionar)
print(df)
df.to_excel("BNR_ALL_DATA.xls")
