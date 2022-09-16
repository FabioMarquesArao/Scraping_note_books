import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service                                                                  
import os 
from time import sleep



serv = Service((ChromeDriverManager().install()))
options = ChromeOptions()
prefs = {"download.defout_directcory" : os.getcwd(),
            "profile.content_settings.exceptions.automatic_dowloads.*.setting": 1}
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option("prefs", prefs)
webdriver = Chrome(service=serv, options=options)
url = 'https://lista.mercadolivre.com.br/notebook#D[A:notebook]'
webdriver.get(url)
webdriver.maximize_window()

columns = ['descricao',
           'preco',
           'forma_pgto']

df = pd.DataFrame(columns=columns)
df.to_excel('notebooks_mercado_livre.xlsx', index=False)
                        
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
webdriver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
itens = soup.find_all('li', class_="ui-search-layout__item")
pagina_inicio = soup.find('span', class_='andes-pagination__link').get_text().strip()
pagina_fim = soup.find('li', class_='andes-pagination__page-count').get_text().strip().lstrip()[2:]
pag = int(pagina_inicio)
df = pd.read_excel(os.getcwd() + '\\notebooks_mercado_livre.xlsx')
#while pag < int(pagina_fim):
    

for i in itens:
    descricao = i.find('h2', class_="ui-search-item__title ui-search-item__group__element shops-custom-secondary-font")
    preco = i.find('span', class_="price-tag-amount")
    pre = preco.get_text().replace('R$', '').replace('.', '').replace("'", "").replace(',','').lstrip()
    preco_form = "Em até 10x de :",float(pre)/10
    pgto = i.find('span', class_="price-tag-text-sr-only")
    webdriver.execute_script('window.scroll(0, 9400)')
    
    print(descricao.get_text())
    print(preco.get_text())
    print(str(preco_form).replace('(', '').replace("'", "").replace(',','').replace(')','').replace('.', ','))
    
    df.loc[int(len(df) + 1)] = descricao.get_text(), preco.get_text(), str(preco_form).replace('(', '').replace("'", "").replace(',','').replace(')','').replace('.', ',')
      
df.to_excel('notebooks_mercado_livre.xlsx', index=False)
                
    #webdriver.find_element(By.XPATH, "//*[contains(text(), 'Seguinte')]").click()
    #pag +=1 
#print(pag)
    




