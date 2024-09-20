#(MÉTODO ANTIGO - TESTE)
#####import os
#####import codecs

import google.generativeai as genai
from langchain.text_splitter import CharacterTextSplitter
from Web_Scrapping import texto_noticia

#Configure a chave da API
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE") #Pode ser criada através do Googel AI Studio --> 'https://aistudio.google.com/app/apikey'

#Crie o modelo
model = genai.GenerativeModel(model_name="gemini-pro") #Nome do modelo que você usará (por padrão, 'gemini-pro')

#Define a função para processar o texto
def process_news(text):
    #Divide o texto em chunks para processamento
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_text(text)

    #Analisa o sentimento de cada chunk
    results = [analyze_sentiment(chunk) for chunk in chunks]

    #Combina os resultados de todos os chunks
    overall_sentiment = summarize_sentiment(results)

    return overall_sentiment

def analyze_sentiment(text):
    chat_session = model.start_chat(history=[])  #Inicia uma sessão de conversa
    response = chat_session.send_message(f'Make a sentiment analysis of this news and rate it on a float scale from 0.00 to 1.00, where 0.00 is very negative and 1.00 is very positive: {text}')

    try:
        sentiment_score = float(response.text.strip())  #Converte a resposta para um valor float
    except ValueError:
        sentiment_score = 0  #Em caso de erro, define o sentimento como neutro (0)
    return sentiment_score

#Cria uma análise do por que determinada nota foi dada ao texto da notícia escolhida
def analyze_sentiment_justify(text):
    chat_session = model.start_chat(history=[]) #Inicia uma sessão de conversa
    response = chat_session.send_message(f'Faça uma análise de sentimento desta notícia e avalie em uma escala flutuante de 0.00 a 1.00, onde 0.00 é muito negativo e 1.00 é muito positivo: {text}')
    response = chat_session.send_message(f'Justifique e resuma sua análise quanto a esta notícia.')
    print(response.text)


#Define a função para resumir o sentimento
def summarize_sentiment(results):
    average_sentiment = sum(results) / len(results)  #Calcula a média dos valores de sentimento

    return {
        'average_sentiment': average_sentiment
    }

#Lê o conteúdo da notícia (MÉTODO ANTIGO - TESTE)
#####with codecs.open('news.txt', 'r', encoding='utf-8') as file:
#####    news_content = file.read()

#Processa a notícia e imprime o resultado
sentiment_summary = process_news(texto_noticia)
print(f'Sentimento da Notícia: {sentiment_summary['average_sentiment']}')
print('\n--------------------------\n')
analyze_sentiment_justify(texto_noticia)
