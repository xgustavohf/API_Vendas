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
    meta, status
    FROM vendas
    """

    cursor = conexao.cursor()
    cursor.execute(consulta_sql)

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    colunas = [i[0] for i in cursor.description]
    tabela = pd.DataFrame(resultado, columns=colunas)

    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    tabela[meses] = tabela[meses].apply(pd.to_numeric, errors='coerce')
    
    tabela['total_vendas'] = tabela[meses].sum(axis=1)

    resposta = []

    for _, row in tabela.iterrows():
        cliente = OrderedDict()
        cliente['idvendas'] = row['idvendas']

        outros_campos = {col: row[col] for col in colunas if col != 'idvendas'}

        outros_campos['total_vendas'] = '{:.2f}'.format(row['total_vendas'])

        mensagem_chatgpt = gerar_mensagem_chatgpt() 

        outros_campos['status'] = mensagem_chatgpt

        cliente['outros_campos'] = outros_campos

        resposta.append(cliente)

    return jsonify(resposta)

if __name__ == '__main__':
    app.run()
