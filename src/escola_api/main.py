from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"mensagem": "Olá mundo"}

#localhost:8000/calculadora?numero1=20&numero2=40
@app.get("/calculadora")
def calculadora(numero1:  int, numero2: int):
    soma = numero1 + numero2
    return {"soma": soma}

@app.get("/processar-cliente")
def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
    # nome_completo => snake_case
    # nome_Completo => PascalCase
    # nomeCompleto => camelCase
    # nome-completo => kebab-ase
    nome_completo = nome + " " + sobrenome
    ano_nascimento = datetime.now().year - idade

    if ano_nascimento < 1990 and ano_nascimento < 2000:
        decada = "decada de 90"
    elif ano_nascimento >= 1980 and ano_nascimento < 1990:
        decada = "decada de 80"
    elif ano_nascimento >= 1970 and ano_nascimento < 1980:
        decada = "decada de 70"
    else:
        decada = ("decada de 70 ou acima de 90")
    return {
        "nome_completo": nome_completo,
        "ano_nascimento":ano_nascimento,
        "idade": decada,
    }


