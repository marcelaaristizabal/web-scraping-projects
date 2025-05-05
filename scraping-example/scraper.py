import requests
from bs4 import BeautifulSoup

# URL de ejemplo (puedes cambiarla a una página que quieras scrapear)
url = "https://quotes.toscrape.com/"

# Hacer una solicitud HTTP GET
response = requests.get(url)

# Verificar que la respuesta sea exitosa (código de estado 200)
if response.status_code == 200:
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todas las citas en la página
    quotes = soup.find_all('span', class_='text')
    
    # Imprimir las primeras 5 citas
    for i, quote in enumerate(quotes[:5]):
        print(f"{i+1}. {quote.text}")
else:
    print("Error al obtener la página")
