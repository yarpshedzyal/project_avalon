from bs4 import BeautifulSoup 
import requests

ulr = 'https://www.amazon.com/Krollen-Industrial-Gallon-Square-Commercial/dp/B0B4B8JG22/ref=sr_1_3?crid=V9F13ZF9XKIF&dib=eyJ2IjoiMSJ9.QFspTHc-3fGcZOL3Q4U53ObaZyNfFfJ4MpNsKrJOC0qvKAbQ88YGtZ2GoTMnwN2uUQV1mNRmmgzVROcOvwNYEefTyToTzokaUbw1Y92lvHuAVyW-qnVcuK_Z8Jv4JXBWNQ4tgj1FFcOgDxuMzZRNWv2TS_CuMIzmggPzXH4mazYiox61sugACV4Ecs2jnJpwaKvP2ZP109h6sgTFiGZj_asF-AzrhFKL6blBziHxBHM.9Gj70rPn2DLlilVBXLrHC7YiN_aZtxPwzJPePoVrPLs&dib_tag=se&keywords=krollen%2Bindustrial%2B35%2Bgallon%2Bblack%2Bsquare%2Bcommercial%2Btrash%2Bcan&qid=1714312571&sprefix=krollen%2B%2Caps%2C176&sr=8-3&th=1'

response = requests.get(ulr)
# print(response.status_code)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')
    buybox_text = soup.find('#addToCart > div > div > div')
    print(soup.get_text())    
if buybox_text: 
    print(buybox_text)
else:
    print('error 14')

