from bot.bot import Merc_livre
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service   
import os                                                               


class Aplication():
    def __init__(self):

        self.serv = Service((ChromeDriverManager().install()))
        self.options = ChromeOptions()
        self.prefs = {"download.defout_directcory" : os.getcwd(),
                    "profile.content_settings.exceptions.automatic_dowloads.*.setting": 1}
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.options.add_experimental_option("prefs", self.prefs)
        self.execulte_bot()

    def execulte_bot(self):
        self.webdriver = Chrome(service=self.serv, options=self.options)
        self.url = 'https://lista.mercadolivre.com.br/notebook#D[A:notebook]'
        self.bot = Merc_livre(self.webdriver, self.url)
        self.bot.webdriver.get(self.url)
        self.bot.webdriver.maximize_window()
        self.bot.collect_data()
        self.webdriver.close()


   



if __name__ == "__main__":
    Aplication()
    exit()
            




