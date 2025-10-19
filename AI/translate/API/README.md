# Microsoft Translator + Word Document Automation

This Python script automates text translation using the **Microsoft
Translator Text API (Azure Cognitive Services)** and integrates it with
**Word (.docx)** files using the `python-docx` library.

------------------------------------------------------------------------

## Imports

``` python
import requests, uuid, json
from docx import Document
from google.colab import userdata
```

### Explanation

-   **requests** → handles HTTP requests to call the Azure Translator
    API.\
-   **uuid** → generates a unique client trace ID for tracking each
    translation request.\
-   **json** → parses JSON responses from the API.\
-   **docx.Document** → from the `python-docx` package; used to read and
    write `.docx` files.\
-   **google.colab.userdata** → securely retrieves stored secrets (e.g.,
    API keys) inside Google Colab notebooks.

------------------------------------------------------------------------

## Credentials and Configuration

``` python
subscription_key = userdata.get('KEY1')
endpoint = userdata.get('endpoint')
location = 'eastus2'

language_destination = 'pt-br'
```

### Explanation

-   `subscription_key`: Your Azure Translator API key stored in Colab's    
-   `endpoint`: The API endpoint URL (e.g.,
    "https://api.cognitive.microsofttranslator.com"\
-   `location`: Azure region (used in request headers).\
-   `language_destination`: Default translation target language (`pt-br`
    for Brazilian Portuguese).

------------------------------------------------------------------------

## `translator_text()` Function

``` python
def translator_text(text, target_language):
  path = '/translate'
  constructed_url = endpoint + path
  headers = {
      'Ocp-Apim-Subscription-Key': subscription_key, 
      'Ocp-Apim-Subscription-Region': location,
      'Content-type': 'application/json',
      'X-ClientTraceId': str(uuid.uuid4())
  }

  body = [{
      'text': text
  }]

  params = {
      'api-version': '3.0',
      'from' : 'en',
      'to': [target_language]
  }

  request = requests.post(constructed_url, params=params, headers=headers, json=body)
  response = request.json()
  return response[0]["translations"][0]["text"]
```

### Explanation

This function sends a POST request to the Microsoft Translator API to
translate a single string.

#### Step-by-step:

1.  **URL construction:** Joins the base `endpoint` with the
    `/translate` path \
2.  **Headers:** Includes API key, region, and a unique client ID 
3.  **Body:** A JSON object containing the text to translate 
4.  **Parameters (`params`):**
    -   API version (`3.0`)\
    -   Source language (`from='en'`)\
    -   Target language (`to=[target_language]`)\
5.  **POST request:** Calls the Translator API using `requests.post()`.\
6.  **Response parsing:** Extracts the translated text from the JSON
    response.

**Example Response (simplified):**

``` json
[
  {
    "translations": [
      {"text": "Ó capitão! meu capitão! nossa terrível viagem terminou"}
    ]
  }
]
```

------------------------------------------------------------------------

## `translate_document()` Function

``` python
def translate_document(path):
  document = Document(path)
  full_text = []
  for paragraph in document.paragraphs:
    translated_text = translator_text(paragraph.text, language_destination)
    full_text.append(translated_text)

  translated_doc = Document()
  for line in full_text:    
    translated_doc.add_paragraph(line)
  path_translated = path.replace(".docx", f"_{language_destination}.docx")
  translated_doc.save(path_translated)
  return path_translated
```

### Explanation

This function reads a Word file, translates its paragraphs, and saves
the translated version.

#### Workflow:

1.  **Load document:** Opens the `.docx` file specified by `path`.

2.  **Iterate paragraphs:** Loops through all paragraphs in the
    document.

3.  **Translate:** Sends each paragraph to the `translator_text()`
    function.

4.  **Collect translations:** Appends each translated line to
    `full_text`.

5.  **Create new document:** Initializes a new `.docx` file and adds
    each translated paragraph.

6.  **Save output:** Generates a new file name, for example:

        input.docx → input_pt-br.docx

7.  **Return:** Returns the new file path.

------------------------------------------------------------------------

## Usage Example

``` python
# Translate a single text
# translator_text("O Captain! my Captain! our fearful trip is done", language_destination)

# Translate an entire Word document
input_file = "example.docx"
# translate_document(input_file)
```

### Notes

-   Uncomment the lines above to run them.
-   Ensure `KEY1` and `endpoint` are set in Google Colab's secrets.
-   The file must be uploaded to your Colab environment.

------------------------------------------------------------------------
