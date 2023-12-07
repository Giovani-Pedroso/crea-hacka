from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode
import doc_analysis
from dotenv import load_dotenv
from doc_analysis import check_docs
from telegram_bot import text_messages
import os
load_dotenv()



'''
lista de comandos a implementar e suas descriçoes

start - inicia a conversar com o bot começar - começar a conversar com o bot
iniciar - inicia a conversar com o bot começar - começar a conversar com o bot
documentos - ver a lista de documentos necessários para realizar o registro
registar - inicia o processo de registro
dev_reset - reseta a base de dados, usar para de bug 
andamento - ver como está o andamento do processo de registro
sobre - informações sobre o bot
'''

class Bot:
    def __init__(self, token) -> None:
        self.token = token
        self.tipo_de_analise ="nda"
        # self.tipo_de_analise ="rg_costas"
        self.rg_nome=""
        self.rg_numero=""
        self.rg_nascimento=""
        self.rg_cpf=""
        self.rg_da_expedicao=""

    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.tipo_de_analise ="nda"
        await update.message.reply_text(text=text_messages.INICIAR,
                                       parse_mode=ParseMode.MARKDOWN_V2)

    async def _sobre(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.tipo_de_analise ="nda"
        await update.message.reply_text(text=text_messages.SOBRE,
                                       parse_mode=ParseMode.MARKDOWN_V2)

    async def _registro(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # chat_id = update.effective_chat.id
        await update.message.reply_text( text="Ola vamos começar a realizar seu registro")

        await update.message.reply_text(text=text_messages.REGISTRO_RG_FRENTE)
        await update.message.reply_photo( photo=open('./telegram_bot/static/rg-frente.png','rb'))
        self.tipo_de_analise ="rg_frente"

    async def _documentos(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.tipo_de_analise ="nda"
        await update.message.reply_text(text=text_messages.DOCUMENTOS,
                                       parse_mode=ParseMode.MARKDOWN_V2)

    async def _error(self, update, context):
        self.tipo_de_analise ="nda"
        print(f'\n\n--------------------------------------------------------\n\n')
        print(f'Update {update}')
        print(f' caused error {context.error}')

    async def _photo_handler(self, update, context):
        print(f"Tipo de imagem a analiar {self.tipo_de_analise}")
        if self.tipo_de_analise == "nda":
            return
        
        # print (f"imame update id {update.message.photo[-1].file_id}")

        #Pega o id da imagem com a maior resolucao
        file_id = update.message.photo[-1].file_id

        #Se remover a linha abaixo o codigo para de funcionar
        print (type(update.message.photo))

        #Salva a imagem para a analize
        file = await context.bot.getFile(file_id)
        file_path = f'./tmp/{file_id}.jpg'
        await file.download_to_drive(file_path)

        await update.message.reply_text("Analizando a imagem", parse_mode=ParseMode.MARKDOWN_V2)

        if self.tipo_de_analise =="rg_frente":
            frente = check_docs.rg_frente(file_path)
            self.rg_nome = frente['nome']
            self.rg_nascimento = frente['nasDate']
            print(f'nome: {self.rg_nome }')
            print(f'nascimento: {self.rg_nascimento }')
            await update.message.reply_text(f"Apenas para confirmar\n*Seu nome* é {self.rg_nome}\n*Você* nasceu no dia {self.rg_nascimento}",
                                            parse_mode=ParseMode.MARKDOWN_V2)

            await update.message.reply_text(text=text_messages.REGISTRO_ERRO_RG_FRENTE,
                                            parse_mode=ParseMode.MARKDOWN_V2)
            self.tipo_de_analise = "rg_costas"

        if self.tipo_de_analise =="rg_costas":
            costas = check_docs.rg_costas(file_path)
            print(f"costas {costas}")
            self.rg_numero = costas['rg']
            self.rg_cpf = costas['cpf']
            self.rg_da_expedicao = costas['data_expedicao']
            await update.message.reply_text(f"""Apenas para confirmar\n*O numero do seu cpf é:*{self.rg_cpf}\n*O numero do seu rg é:* {self.rg_numero}\n*A data de emição é:* {self.rg_da_expedicao}""",
                                            parse_mode=ParseMode.MARKDOWN_V2)

            await update.message.reply_text(text=text_messages.REGISTRO_ERRO_RG_COSTAS,
                                            parse_mode=ParseMode.MARKDOWN_V2)
            self.tipo_de_analise = "curriculo"

        elif self.tipo_de_analise =="curriculo":
            ...

        elif self.tipo_de_analise =="historico":
            ...

        else:
            ...

        os.remove(file_path)

        

    #Teste de checagem de boleto
    #Checa se codigo é da linha digitavel corresponde ao
    # if header_info['bankCodeReal'] !=header_info['bankCodeReal']:
        # await update.message.reply_text(f'O diz ser do banco {heater_info["bankName"]} porem essa informação não com o codigo {heater_info["bankCodeReal"]}')
    
    async def _test(self):
        print("just a test command")
        ...

    async def _rgFrente(self, update, context):
        await update.message.reply_text("Porfavor envie outra foto da parte da frente de  seu rg")
        self.tipo_de_analise="rg_frente"

    async def _rgCostas(self, update, context):
        await update.message.reply_text("Porfavor envie outra foto da parte de tras de  seu rg")
        self.tipo_de_analise="rg_costas"

    def init(self):

        application = ApplicationBuilder().token(self.token).build()
        
        # Esses comandos são iguais possuindo nomes diferentes apenas para melhorar o experiencia do usuário
        start_handler = CommandHandler('start', self._start)
        inicio_handler = CommandHandler('iniciar', self._start)

        registro_handler = CommandHandler('registar',   self._registro)
        sobre_handler = CommandHandler('sobre', self._sobre)
        documentos_handler= CommandHandler('documentos', self._documentos)
        test_handler= CommandHandler('test', self._test)

        rgFrente_handler = CommandHandler('rgFrente', self._rgFrente)
        rgCostas_handler= CommandHandler('rgCostas', self._rgCostas)

        application.add_handler(start_handler)
        application.add_handler(inicio_handler)
        application.add_handler(registro_handler)
        application.add_handler(sobre_handler)
        application.add_handler(documentos_handler)
        application.add_handler(test_handler)
        application.add_handler(rgFrente_handler)
        application.add_handler(rgCostas_handler)

        #Images
        application.add_handler(MessageHandler(filters.PHOTO, self._photo_handler))
        
        #Erros
        application.add_error_handler(self._error)

        print("bot foi iniciado")
        application.run_polling(poll_interval=2)


