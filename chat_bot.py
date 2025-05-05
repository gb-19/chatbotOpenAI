import openai

client = openai.OpenAI(api_key= 'sua_chave_aqui')

def enviar_conversa (mensagem, lista_mensagens=[]):

    lista_mensagens.append(
        {'role':'user', 'content': mensagem}
    )

    resposta = client.chat.completions.create(
        model= 'gpt-3.5-turbo',
        messages= lista_mensagens,
    )
    return resposta.choices[0].message.content

lista_mensagens = []
while True:
    texto = input ("Digite sua mensagem:")

    if texto == 'sair':
        break
    else:
        resposta = enviar_conversa(texto, lista_mensagens)
        lista_mensagens.append({'role':'user', 'content': resposta})
        print ('Chatbot:', resposta)