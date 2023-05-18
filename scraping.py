import requests
from bs4 import BeautifulSoup

url = 'http://portal.mec.gov.br/pec-g/cursos-e-instituicoes'

# Realiza a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
content = response.content

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Encontra todas as tags <a> que possuem a classe "link-instituicao"
div = soup.find('div', class_='item-page')
links = div.find_all('a')

# Extrai as URLs dos links e salva em um arquivo de texto
with open('universidades.txt', 'w') as file:
    for link in links:
        url = link['href']
        file.write(url + '\n')
