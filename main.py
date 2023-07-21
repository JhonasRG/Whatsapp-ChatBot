from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
import openai
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreto'  # CHAVE SECRETA PODE SER QUALQUER COISA

# OPEN-AI CHAT GPT

openai.api_key = "sua-chave-de-api-openai"  # CHAVE DE API DA OPENAI
completion = openai.Completion()

inicio_chat_log = '''Humano: Eae, quem é você?
IA: Tudo bem, como posso te ajudar hoje?
'''

def fazer_pergunta(pergunta, chat_log=None):
    if chat_log is None:
        chat_log = inicio_chat_log
    prompt = f'{chat_log}Humano: {pergunta}\nIA:'
    prompt = pergunta
    resposta = completion.create(
        prompt=prompt, engine="text-davinci-003", stop=['\nHumano'], temperature=0.2,
        top_p=1, frequency_penalty=0.1, presence_penalty=0.0, best_of=1,
        max_tokens=256)
    resposta_texto = resposta.choices[0].text.strip()
    return resposta_texto

def adicionar_interacao_ao_chat_log(pergunta, resposta, chat_log=None):
    if chat_log is None:
        chat_log = inicio_chat_log
    return f'{chat_log}Humano: {pergunta}\nIA: {resposta}\n'

# TWILIO

conta_sid = 'SUA_CONTA_SID_DO_TWILIO'  # SID DA CONTA TWILIO
auth_token = 'SEU_AUTH_TOKEN_DO_TWILIO'  # TOKEN DE AUTENTICAÇÃO DA CONTA TWILIO
client = Client(conta_sid, auth_token)

def enviar_mensagem(corpo_mensagem, numero_telefone):
    print("CORPO DA MENSAGEM " + corpo_mensagem)
    mensagem = client.messages.create(
        from_='whatsapp: --número obtido da Twilio-- ',  # Com Código do País
        body=corpo_mensagem,
        to='whatsapp:' + numero_telefone  # Com Código do País
    )
    print(mensagem)  # Imprimir resposta

@app.route('/bot', methods=['POST'])
def bot():
    mensagem_recebida = request.values['Body']
    numero_telefone = (request.values['WaId'])

    if mensagem_recebida:
        chat_log = session.get('chat_log')
        resposta = fazer_pergunta(mensagem_recebida, chat_log)
        session['chat_log'] = adicionar_interacao_ao_chat_log(mensagem_recebida, resposta, chat_log)
        enviar_mensagem(resposta, numero_telefone)
        print(resposta)
    else:
        enviar_mensagem("Mensagem não pode estar vazia", numero_telefone)
        print("Mensagem está vazia")
    r = MessagingResponse()
    r.message("")        
    return str(r)

if __name__ == '__main__':
    app.run()
