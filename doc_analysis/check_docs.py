from doc_analysis import img_to_text
import re

def rg_frente(img_path):
    print("analizando frente do rg")
    nome = "nda"
    nasDate = "nda"
    text = img_to_text.rg_frente(img_path)['text']
    text = text.split('\n')

    # Remove os espaço em branco
    text = [item for item in text if item]
    print(text)

    # procura pela palavar filiacão, esse é o melhor indicador para achar o nome
    index_filiacao = 0
    for i in enumerate(text):
        word=i[1].lower() 

        # Verifica se há alguma data no documento, na parte da frente do rg, 
        # a unica data possivel é a de nascimento
        data_no_texto = re.findall(r'(\d+/\d+/\d+)',i[1])

        # print(data_no_texto)
        if  "filiacao" in word or "filiaçao" in word or "filiacão" in word or "filiação" in word :
            nome = text[i[0]-1]

        if len(data_no_texto) == 1 :
            nasDate = data_no_texto[0] 

        


    return{'nome':nome, "nasDate":nasDate}

def rg_costas(img):
    text = img_to_text.rg_costas(img)
    text = text['text']
    print(text)

    # Encontar e trata os dados da imagem
    cpf=re.findall(r'\d{9}\D\d{2}', text)[0]
    cpf = re.sub(r'\D', "", cpf)

    rg= re.findall(r'\d{2}\D\d{3}\D\d{3}\D\d{1}', text)[0]
    rg = re.sub(r'\D', "", rg)

    data_expedicao= re.findall(r'\d{2}\D\d{2}\D\d{4}', text)[0]
    data_expedicao = re.sub(r'\D', "/", data_expedicao)

    toReturn ={'cpf':cpf, 'rg':rg, 'data_expedicao':data_expedicao} 
    # print(toReturn)

    return toReturn

# Essas funções servem apenas para debug
def rg_costas_text(text):
    cpf=re.findall(r'\d{9}\D\d{2}', text)[0]
    cpf = re.sub(r'\D', "", cpf)

    rg= re.findall(r'\d{2}\D\d{3}\D\d{3}\D\d{1}', text)[0]
    rg = re.sub(r'\D', "", rg)

    data_expedicao= re.findall(r'\d{2}\D\d{2}\D\d{4}', text)[0]
    data_expedicao = re.sub(r'\D', "-", data_expedicao)

    print(text)
    return {'cpf':cpf, 'rg':rg, 'data_expedicao':data_expedicao}

