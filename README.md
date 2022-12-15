

# Scraping Notebooks!...
Coletando dados e valores de notebooks no mercado livre e salvando em uma planilha excel.

## Referência

 - [Pandas](https://pandas.pydata.org/docs/)
 - [Selenium](https://selenium-python.readthedocs.io/)
 - [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 - [Python](https://www.python.org/downloads/release/python-3100/)

## Apêndice

O Bot utiliza o [Selenium](https://selenium-python.readthedocs.io/) para automatizar o browser, e [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/) para coletar os dados dos notebooks ( descrição, preço, e condições de pagamento).
Ao iniciar o Bot ele abre o navegador na url do [www.mercadolivre.com.br/notebook](https://lista.mercadolivre.com.br/notebook#D[A:notebook]) e percorre todas as paginas com notebooks coletando os dados.
Ao final da coleta ele ainda salva todos os dados em uma planilha excel, que pode ser facilmente enviada por email para um destinatario especifico utilizando [Smtplib]() .
## Melhorias

Será adicionado a funcionalidade de enviar a planilha com os dados coletados por email..
## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de fabinhoarao@gmail.com

