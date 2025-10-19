import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
from google.colab import userdata


url = ''

client = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=userdata.get('azure_endpoint'),
    api_key=userdata.get('subscription_key'),
    max_retries=0,
    model_name = "gpt-4o-mini"

)



def extract_text_from_url(url):
  response = requests.get(url)  

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script', 'style']):
      script_or_style.decompose()
    texto = soup.get_text(separator= ' ')    
    #limpar texto
    linhas = (line.strip() for line in texto.splitlines() )
    parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
    texto = ' '.join(part for part in parts if part)
    return texto

  else:
    print(f"failed to fetch de URL. Status code: {response.status_code}")


  soup = BeautifulSoup(response.text, 'html.parser')
  
  
  text = soup.get_text()
  return text

def translate_article(text, lang):
  messages = [
      ("System:" "Você atua como um tradutor de textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown ")      
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content

text = extract_text_from_url(url)
print("texto traduzido")
translate_article(text, "pt-br")
