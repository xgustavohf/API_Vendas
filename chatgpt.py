import openai

openai.api_key = ''

def gerar_mensagem_chatgpt():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Gerar mensagem para status financeiro:", 
        max_tokens=10 
    )
    
    mensagem = response.choices[0].text.strip()
    
    return mensagem
