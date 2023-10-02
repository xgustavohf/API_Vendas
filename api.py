import pandas as pd
from flask import Flask, jsonify
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'A API está funcionando'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv(r'C:\Users\Gustavo\Desktop\CursoDio\IA\vendas.csv')
    
    colunas_relevantes = [
        'id', 'nome_completo', 'cpf', 'rg', 'data_nascimento', 'idade', 'sexo',
        'email', 'uf', 'cep', 'cidade', 'endereço', 'telefone',
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
        'total_vendas', 'status_financeiro'
    ]
    
    resultado = tabela[colunas_relevantes]
    
   
    resultado['total_vendas'] = resultado.iloc[:, 13:25].sum(axis=1)
    
    
    resposta = []
    
    for _, row in resultado.iterrows():
        
        cliente = OrderedDict()
        
        cliente['id'] = row['id']
          
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
        outros_campos['endereço'] = row['endereço']
        outros_campos['telefone'] = row['telefone']
        outros_campos['janeiro'] = row['janeiro']
        outros_campos['fevereiro'] = row['fevereiro']
        outros_campos['março'] = row['março']
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
        outros_campos['status_financeiro'] = row['status_financeiro']
        
        cliente['outros_campos'] = outros_campos
        
        resposta.append(cliente)
    
    return jsonify(resposta)

if __name__ == '__main__':
    app.run()
