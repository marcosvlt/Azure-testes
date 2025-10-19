# Webpage Text Extraction and Translation using Azure OpenAI

This script fetches a webpage, extracts its visible text, cleans it, and translates it to a specified language using Azure OpenAI via LangChain.

---

## 1. Imports

```python
import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI
from google.colab import userdata
```

- **`requests`**: Sends HTTP requests to fetch webpages.
- **`BeautifulSoup`**: Parses HTML to extract readable text.
- **`AzureChatOpenAI`**: Client to interact with Azure OpenAI models.
- **`userdata`**: Securely stores/retrieves API keys in Google Colab.

---

## 2. Azure OpenAI Client Setup

```python
client = AzureChatOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=userdata.get('azure_endpoint'),
    api_key=userdata.get('subscription_key'),
    max_retries=0,
    model_name="gpt-4o-mini"
)
```

- Connects to the Azure OpenAI service using the endpoint and subscription key stored in Colab.
- Uses the **`gpt-4o-mini`** model for translation.
- **`max_retries=0`** disables automatic retries.

---

## 3. Extract Text from a Webpage

```python
def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        
        texto = soup.get_text(separator=' ')
        
        # Clean text
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
        texto = ' '.join(part for part in parts if part)
        return texto
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
```

- Sends a GET request to the given URL.
- Parses the HTML and removes `<script>` and `<style>` tags.
- Extracts visible text and cleans it by stripping extra spaces and line breaks.
- Returns a single string containing the cleaned text.

---

## 4. Translate Article

```python
def translate_article(text, lang):
    messages = [
        ("system", "Você atua como um tradutor de textos"),
        ("user", f"Traduza o seguinte texto para {lang} e responda em markdown:\n\n{text}")
    ]

    response = client.invoke(messages)
    print(response.content)
    return response.content
```

- Prepares a conversation for the AI model:
  - **System message**: instructs the AI to act as a translator.
  - **User message**: asks for translation of the text into the target language.
- Sends the messages to the Azure OpenAI client using `invoke`.
- Returns and prints the translated text in Markdown format.

---

## 5. Main Execution

```python
url = "https://example.com"  # Replace with your target URL

text = extract_text_from_url(url)
print("texto traduzido")
translate_article(text, "pt-br")
```

- Replace `url` with the webpage you want to translate.
- Extracts the webpage text.
- Translates the text to Brazilian Portuguese (`pt-br`).
