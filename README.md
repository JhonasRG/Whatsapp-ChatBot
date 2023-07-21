# Whatsapp-ChatBot

Este código implementa um chatbot integrado ao serviço de mensagens do WhatsApp usando a biblioteca Flask e a API da OpenAI. O chatbot utiliza o modelo de linguagem GPT-3 da OpenAI para responder a perguntas enviadas pelos usuários.

Funcionalidade:

1- O usuário envia uma mensagem para o número de telefone configurado no Twilio para o chatbot.
2- O código Flask recebe a mensagem enviada pelo Twilio através do método POST na rota '/bot'.
3- O chatbot usa a API da OpenAI para processar a pergunta recebida e gerar uma resposta adequada usando o modelo GPT-3.
4- A resposta gerada é enviada de volta ao usuário através do WhatsApp usando a API do Twilio.
5- O histórico de interação do chatbot com o usuário é armazenado na sessão.

Para executar este código, você precisará obter as seguintes API keys:

API Key da OpenAI: Você pode obter uma chave de API da OpenAI se inscrevendo em sua plataforma e adquirindo acesso à API GPT-3. Depois de se inscrever, a OpenAI fornecerá uma chave de API que você deve substituir em "sua-chave-de-api-openai" no código.

Twilio Account SID e Auth Token: Você precisará se inscrever no serviço Twilio para obter um Account SID e Auth Token. Eles serão usados para autenticar suas solicitações à API do Twilio. Substitua "SUA_CONTA_SID_DO_TWILIO" e "SEU_AUTH_TOKEN_DO_TWILIO" no código com suas próprias credenciais do Twilio.
