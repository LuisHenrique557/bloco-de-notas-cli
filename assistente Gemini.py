from google import genai

# Sua chave de acesso gerada
CHAVE_DO_GOOGLE = "AQ.Ab8RN6JcxP408R9z5JZygJmcOvb02nwgJKXynG_zr7z9n9PcxQ"
client = genai.Client(api_key=CHAVE_DO_GOOGLE)

print("--- 🤖 Seu Chatbot Particular de ADS está Online! ---")
print("(Digite 'sair' a qualquer momento para encerrar o programa)\n")

# Alterado para o modelo 2.0-flash, que é aceito universalmente sem travas de 404
chat = client.chats.create(model="gemini-3.6-flash")


while True:
    pergunta = input("Você: ")

    if pergunta.lower() == 'sair':
        print("\n🤖 Até mais! Bons estudos em ADS!")
        break

    print("Gemini pensando...")

    resposta = chat.send_message(pergunta)

    print(f"\nGemini: {resposta.text}")
    print("-" * 40)
