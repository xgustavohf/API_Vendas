import openai
import mysql.connector

openai.api_key = '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'

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            port=3307,
            user='root',
            password='root',
            database='ghf_api'
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def gerar_mensagem_chatgpt():

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Gerar mensagem para status financeiro:",  
        max_tokens=50 
    )
    
    mensagem = response.choices[0].text.strip()
    
    return mensagem
