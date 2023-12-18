from dotenv import load_dotenv
from telegram_bot.bot import Bot 
from doc_analysis import check_docs
import os

load_dotenv()

MY_ENV_VAR = os.getenv('TEST')

# # for windows
if os.name == 'nt':
    _ = os.system('cls')

# # for mac and linux(here, os.name is 'posix')
else:
    _ = os.system('clear')

# print(f"rg frente {check_docs.rg_frente(test_rg_frente)}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_c_0.jpg')}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_frente.jpg')}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_frente.jpeg')}")
# print(check_docs.rg_frente('./img/rg_frente.jpg'))
# print(f"rg costas {check_docs.rg_costas('./img/rg_c_1.jpg')}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_c_2.jpg')}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_c_2.jpg')}")
# print(f"rg costas {check_docs.rg_costas('./img/rg_c_0.jpg')}")
# print(f"rg frente {check_docs.rg_frente('./img/rg_frente.jpg')}")



# print(check_docs.rg_costas_text(cos))

MyBot = Bot(os.getenv('TELEGRAM_TOKEN'))
MyBot.init()
