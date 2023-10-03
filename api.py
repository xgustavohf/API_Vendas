import os
import mysql.connector
import pandas as pd
from flask import Flask, jsonify
from collections import OrderedDict
from chatgpt import gerar_mensagem_chatgpt

app = Flask(__name__)

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host='containers-us-west-59.railway.app', 
            user='root',
            password='uwmhxiiizEXGe1PBEcbG',
            port=5809,  
            database='railway'
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

@app.route('/')
def homepage():
    return 'A API está funcionando'

@app.route('/vendas')
def pegarvendas():
    conexao = conectar_bd()

    if conexao is None:
        return jsonify({"erro": "Não foi possível conectar ao banco de dados"})

    consulta_sql = """
    SELECT idvendas, nome_completo, cpf, rg, data_nascimento, idade, sexo, email, uf, cep, cidade, endereco, telefone,
    janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro,
    total_vendas, meta, status
    FROM vendas
    """

    cursor = conexao.cursor()
    cursor.execute(consulta_sql)

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    colunas = [i[0] for i in cursor.description]
    tabela = pd.DataFrame(resultado, columns=colunas)

    # Realiza a soma das vendas mensais
    tabela['total_vendas'] = tabela.iloc[:, 13:25].sum(axis=1)

    resposta = []

    for _, row in tabela.iterrows():
        cliente = OrderedDict()
        cliente['idvendas'] = row['idvendas']

        outros_campos = OrderedDict()
        outros_campos['nome_completo'] = row['nome_completo']
        outros_campos['cpf'] = row['cpf']
        outros_campos['rg'] = row['rg']
        outros_campos['data_nascimento'] = row['data_nascimento']
        outros_campos['idade'] = row['idade']
        outros_campos['sexo'] = row['sexo']
        outros_campos['email'] = row['email']
        outros_campos['uf'] = row['uf']
        outros_campos['cep'] = row['cep']
        outros_campos['cidade'] = row['cidade']
        outros_campos['endereco'] = row['endereco']
        outros_campos['telefone'] = row['telefone']
        outros_campos['janeiro'] = row['janeiro']
        outros_campos['fevereiro'] = row['fevereiro']
        outros_campos['marco'] = row['marco']
        outros_campos['abril'] = row['abril']
        outros_campos['maio'] = row['maio']
        outros_campos['junho'] = row['junho']
        outros_campos['julho'] = row['julho']
        outros_campos['agosto'] = row['agosto']
        outros_campos['setembro'] = row['setembro']
        outros_campos['outubro'] = row['outubro']
        outros_campos['novembro'] = row['novembro']
        outros_campos['dezembro'] = row['dezembro']
        outros_campos['total_vendas'] = row['total_vendas']
        outros_campos['meta'] = row['meta']

        mensagem_chatgpt = gerar_mensagem_chatgpt()  # Chama a função do arquivo chatgpt

        outros_campos['status'] = mensagem_chatgpt

        cliente['outros_campos'] = outros_campos

        resposta.append(cliente)

    return jsonify(resposta)

if __name__ == '__main__':
    app.run()
