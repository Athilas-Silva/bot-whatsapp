# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o Whatsapp web
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(30)

# Definir contatos e grupos e mensagem a ser enviada
contatos = ["Mude aqui para o nome do contato ou grupo"]
mensagem = "Mensagem automatizada"

# Buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

# Enviar mensagens para o contato/grupo
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]') 
    campo_mensagem[1].click() #Selecionando a segunda caixa de texto
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# Campo de pesquisa "copyable-text selectable-text" retirado do Whatsapp Web
# Campo de mensagem privada "copyable-text selectable-text" retirado do Whatsapp Web
