import requests , os
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By                                    
from time import sleep


class Merc_livre():
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        

    def collect_data(self):

        columns = ['descricao',
                   'preco',
                   'forma_pgto']

        df = pd.DataFrame(columns=columns)
        df.to_excel('notebooks_mercado_livre.xlsx', index=False)    
        site = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        self.webdriver.find_element(By.XPATH, "//*[contains(text(), 'Entendi')]").click()
        itens = soup.find_all('li', class_="ui-search-layout__item")
        pagina_inicio = soup.find('span', class_='andes-pagination__link').get_text().strip()
        pagina_fim = soup.find('li', class_='andes-pagination__page-count').get_text().strip().lstrip()[2:]
        pag = int(pagina_inicio)
        df = pd.read_excel(os.getcwd() + '\\notebooks_mercado_livre.xlsx')

        while pag < int(pagina_fim):
            for i in itens:
                descricao = i.find('h2', class_="ui-search-item__title")
                preco = i.find_all('span', class_="price-tag-text-sr-only")[1]
                pre = preco.get_text().replace('R$', '').replace('.', '').replace("'", "").replace(',','').lstrip()[:3]
                preco_form = "Em até 10x de :",f"{float(pre)/10:.2f}"
                pgto = i.find('span', class_="price-tag-text-sr-only")
                self.webdriver.execute_script('window.scroll(0, 9400)')
                #print(descricao.get_text())
                #print(preco.get_text())
                #print(str(preco_form).replace('(', '').replace("'", "").replace(',','').replace(')','').replace('.', ','))
                df.loc[int(len(df) + 1)] = descricao.get_text(), preco.get_text(), str(preco_form).replace('(', '').replace("'", "").replace(',','').replace(')','').replace('.', ',')
                
            df.to_excel('notebooks_mercado_livre.xlsx', index=False)
            try:
                self.webdriver.find_element(By.CSS_SELECTOR, 'a[title="Próxima"]').click()
                pag +=1 
                print(pag)
            except:
                pass
        print("bot finalizando......")