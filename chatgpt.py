import openai

openai.api_key = ''

def gerar_mensagem_chatgpt():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Gerar mensagem para status financeiro:",  # Prompt para o ChatGPT
        max_tokens=50 
    )
    
    mensagem = response.choices[0].text.strip()
    
    return mensagem
