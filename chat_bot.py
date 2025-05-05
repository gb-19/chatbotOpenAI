import openai

client = openai.OpenAI(api_key='sua_chave_aqui')

def enviar_conversa(mensagem, lista_mensagens):
    lista_mensagens.append({'role': 'user', 'content': mensagem})

    resposta = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=lista_mensagens,
    )
    conteudo_resposta = resposta.choices[0].message.content
    lista_mensagens.append({'role': 'assistant', 'content': conteudo_resposta})

    return conteudo_resposta

lista_mensagens = []
while True:
    texto = input("Digite sua mensagem: ")

    if texto.lower() == 'sair':  # <-- corrigido aqui
        break
    else:
        resposta = enviar_conversa(texto, lista_mensagens)
        print('Chatbot:', resposta)
