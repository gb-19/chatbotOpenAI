import openai # Importa a biblioteca OpenAI para interagir com a API

# Inicializa o cliente OpenAI com sua chave de API
client = openai.OpenAI(api_key='sua_chave_aqui')

def enviar_conversa(mensagem, lista_mensagens):
    # Adiciona a mensagem do usuário ao histórico
    lista_mensagens.append({'role': 'user', 'content': mensagem})

   # Envia a conversa completa (histórico) para a API e obtém a resposta
    resposta = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=lista_mensagens,
    )
    # Extrai o conteúdo da resposta
    conteudo_resposta = resposta.choices[0].message.content
    # Adiciona a resposta do chatbot ao histórico
    lista_mensagens.append({'role': 'assistant', 'content': conteudo_resposta})

    # Retorna a resposta para exibir ao usuário
    return conteudo_resposta
    
# Inicializa a lista que armazena o histórico da conversa
lista_mensagens = []
# Inicia o loop principal para interação com o usuário
while True:
    # Recebe a mensagem digitada pelo usuário
    texto = input("Digite sua mensagem: ")

    # Verifica se o usuário quer encerrar a conversa
    if texto.lower() == 'sair':  # <-- corrigido aqui
        break
    else:
        # Envia a mensagem para o chatbot e recebe a resposta
        resposta = enviar_conversa(texto, lista_mensagens)
        # Exibe a resposta do chatbot no terminal
        print('Chatbot:', resposta)
