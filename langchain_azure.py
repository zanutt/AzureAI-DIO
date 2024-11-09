from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint='EndPointAzure',
    api_key='APIKEYFROMAZURE',
    api_version='2024-02-15-preview',
    deployment_name='gpt-4o-mini',
    max_retries=0
)

def trasnlate_article(text, lang):
    messages =[
        ("system",  "Voce atua como tradutor de textos"),
        ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
    ]

    response = client.invoke(messages)
    print(response.content)
    return response.content

