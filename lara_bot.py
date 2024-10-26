from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Configurar logging para debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '7674145014:AAHGX3idwnUV-_G1zDcOy1S5oxz7VEWzleg'  # Coloque seu token entre aspas

# Dados fictícios para pacotes
pacotes = {
    'pacote1': 20,
    'pacote2': 50,
}

# Dicionário para armazenar usuários e seus pacotes
usuarios = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Comando /start recebido.")
    await update.message.reply_photo(
        photo=open('/Users/caosbeats/Desktop/Lara/porn/cobrindo.png', 'rb'),  # Caminho da sua imagem
        caption='Olá! Eu sou a Lara. Aqui estão os meus pacotes disponíveis:\n'
                '/precos - Ver preços dos pacotes\n'
                '/pagar - Informações sobre pagamento via Pix\n'
                '/info - Informações sobre mim'
    )

async def precos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Comando /precos recebido.")
    message = "Pacotes disponíveis:\n"
    for pacote, preco in pacotes.items():
        message += f"{pacote}: R${preco}\n"
    await update.message.reply_text(message)

async def pagar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Comando /pagar recebido.")
    await update.message.reply_text(
        'Para efetuar o pagamento, utilize o Pix:\n'
        'Chave Pix: seu_email@example.com\n'
        'Após o pagamento, envie seu nome e o pacote escolhido com o comando:\n'
        '/confirmar_pagamento pacote1 ou /confirmar_pagamento pacote2'
    )

async def confirmar_pagamento(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    usuario_id = update.message.from_user.id
    pacote = context.args[0] if context.args else None

    if pacote in pacotes:
        usuarios[usuario_id] = pacote
        await update.message.reply_text(f'Pagamento recebido! Você comprou o {pacote}.')
    else:
        await update.message.reply_text('Pacote inválido. Tente novamente.')

# Novo comando adicionado
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Eu sou a Lara, seu assistente virtual. Estou aqui para ajudar com pacotes de conteúdo!'
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('precos', precos))
    app.add_handler(CommandHandler('pagar', pagar))
    app.add_handler(CommandHandler('confirmar_pagamento', confirmar_pagamento))
    app.add_handler(CommandHandler('info', info))  # Adicionando o novo comando

    logging.info("Bot está rodando...")  # Mensagem de log
    app.run_polling()

if __name__ == '__main__':
    main()
