import Azure_translate
import Azure_translate_article
import langchain_azure

#Showcase of translations

#text
print(Azure_translate.translator_text('You get a shiver in the dark', Azure_translate.target_language))

#Document
input_file = 'musica_teste.docx'
Azure_translate.translate_document(input_file)

#translate a simple text for the article
langchain_azure.trasnlate_article("Let's see if the deployment was succeeded.", "portugues")

#trasnlate article
url = 'https://dev.to/elwinjyot/react-basics-part-3-3fa5'
extracted_text = Azure_translate_article.extract_text_from_url(url)
if extracted_text:
    article = langchain_azure.trasnlate_article(extracted_text, "portuges")

print(article)

