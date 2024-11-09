import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)  

        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove all script and style elements
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        #Get text and replace multiple spaces with single space
        text = soup.get_text(separator=' ')

        #Clean text
        lines = (line.strip() for line in text.splitlines())
        #Ensure phrase.strip() is called
        parts = (phrase.strip() for line in lines for phrase in line.split(" "))
        clean_text = '\n'.join(part for part in parts if part)

        return clean_text

    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch the URL. Error: {e}')
        return None

