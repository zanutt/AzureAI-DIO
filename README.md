Esse projeto é um fluxo básico para tradução de textos e documentos, com integração à API do Azure para processamento de linguagem natural e extração de conteúdo da web. ​

1. Azure_translate.py
Este script lida com traduções de texto e documentos usando a API Microsoft Translator, integrada via requisições HTTP. Os principais elementos incluem:

translator_text(text, target_language): Função que traduz uma frase do inglês para um idioma-alvo, usando a API Translator da Microsoft. Ela constrói uma URL de requisição com parâmetros para a tradução e retorna o texto traduzido.
translate_document(path): Função que processa um documento .docx, traduzindo o conteúdo de cada parágrafo. O documento traduzido é salvo com um novo nome, indicando o idioma de destino.

2. Azure_translate_article.py
Focado na extração de texto de URLs para uso posterior em tradução, este script utiliza requests e BeautifulSoup:

extract_text_from_url(url): Esta função obtém o conteúdo textual de uma página web, removendo elementos de script e style. O texto é processado para eliminar espaços e linhas desnecessárias, retornando uma versão limpa do conteúdo da página.

3. langchain_azure.py
Integra o LangChain com o Azure OpenAI para realizar traduções de artigos usando GPT-4:

trasnlate_article(text, lang): Função que usa o modelo Azure OpenAI para traduzir um texto para o idioma especificado. Utiliza um formato de mensagens com contexto de tradução e retorna o conteúdo traduzido em formato Markdown.

4. main.py
Este é o ponto de entrada do projeto e executa exemplos de cada função principal:

Exemplo de tradução de texto: Usa translator_text para traduzir uma frase simples.
Exemplo de tradução de documento: Traduz o conteúdo de um arquivo .docx específico.
Exemplo de tradução de artigo: Extrai texto de uma URL e o traduz, demonstrando o uso da função trasnlate_article de langchain_azure.py.
