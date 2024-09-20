from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

#Configurações do navegador
options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

#Navega até a página da notícia
navegador.get("HTTPS_WEBSITE_LINK_HERE") #Coloque o link do Website que deseja analisar aqui

sleep(2)

#Obtém o conteúdo da página
page_content = navegador.page_source
navegador.quit()  # Fecha o navegador

#Faz o parsing do HTML usando BeautifulSoup
site = BeautifulSoup(page_content, 'html.parser')

#Captura todos os parágrafos na página
paragrafos = site.find_all('p')

#Filtra e concatena os parágrafos com base no comprimento (por exemplo, > 50 caracteres)
texto_noticia = ' '.join([paragrafo.get_text().strip() for paragrafo in paragrafos if len(paragrafo.get_text().strip()) > 50])
