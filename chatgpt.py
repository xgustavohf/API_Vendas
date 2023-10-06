import openai

openai.api_key = ''

def gerar_mensagem_chatgpt(status):
    prompt = f"Gerar mensagem sobre status da meta de vendas: {status}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50 
    )
    
    mensagem = response.choices[0].text.strip()
    
    return mensagem
