# Introdução

Este projeto foi criado para a 2ª edição do Hackathon do CREA-SP (CREA-SP significa Conselho Regional de Engenharia e Agronomia - São Paulo) com o objetivo -----

O código foi testado em um computador com Manjaro (uma distribuição Linux baseada em Arch) para funcionar em uma máquina Windows será necessário algumas modificações na instalação do Tesseract e na configuração do seu caminho.

# Dependências

Para trabalhar com este projeto, são necessárias algumas dependências.
Tesseract

Para executar os scripts, é necessário instalar o programa Tesseract.
Linux

Para instalar o Tesseract, execute um destes comandos:

Arch
```bash
sudo pacman -S tesseract      
```

Ubuntu
```bash
sudo apt install tesseract      
```

Você também precisa instalar o data-set:

Arch
```bash
sudo pacman -S tesseract-data-por tesseract-data-eng      
```

Ubuntu
```bash
sudo apt install tesseract-data-por tesseract-data-eng      
```


## Python

Para instalar as dependências do Python, execute este comando:

```python
python -m pip install -r requirements.txt   
```

## Telegram

Para usar este programa, você precisará criar um bot no Telegram. Siga estes passos:
Passo 1: Configurar sua conta no Telegram

1. Se você não tem uma conta no Telegram, baixe o aplicativo Telegram e crie uma conta.
2. Abra o Telegram: Abra o aplicativo Telegram ou acesse a versão web do Telegram.
3. Encontre o BotFather: Procure por "BotFather" no Telegram ou acesse pelo seguinte link: BotFather.
4. Inicie um chat com o BotFather: Clique em "Iniciar" ou "Start" para começar um chat com o BotFather.
5. Crie um novo bot: Use o comando /newbot e siga as instruções para definir um nome e um username para o seu bot.
O BotFather fornecerá um token de API para o seu bot.

# Configuração de Variáveis de Ambiente

Para configurar as variáveis de ambiente, primeiro você precisa criar um arquivo .env no diretório raiz do projeto. Nele, você
precisa inserir as seguintes variáveis:

1. Caminho do Tesseract
2. Token do bot do Telegram

## Tesseract path

A encontrar o caminho do Tesseract no Linux, use este comando:

```bash
type -a tesseract 
```
Este comando retornará algumas linhas, tente cada uma para ver qual funciona adicione-a  no arquivo .env, ele deve ficar parecido com isso:

```
TESSERACT_PATH= "/usr/bin/tesseract"
```
Para testar, execute o comando:
```bash
python test_terreract.py
```

