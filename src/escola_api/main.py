from datetime import datetime

from fastapi import FastAPI

from fastapi.responses import JSONResponse


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

@app.get("/calcular-total-produto")
def calcular_total_produto(nome: str, quantidade: int, preco: float):
    total = quantidade * preco, 2
    return {"nome": nome,
            "quantidade": quantidade,
            "preco": preco,
            "total": total,
    }

@app.get("/calcular-combustivel")
def calcular_combustivel(gasolina: float, alcool: float):
    # Validação simples para números positivos
    if gasolina <= 0 or alcool <= 0:
        return JSONResponse(status_code=400, content={"erro": "Preços devem ser positivos"})

    # Comparação usando if / else if / else
    if alcool <= gasolina * 0.7:
        return {"abastecer": "álcool"}
    else:
        return {"abastecer": "gasolina"}

@app.get("/calcular-media")
def calcular_media(nota1: float, nota2: float, nota3: float):
    # Calcula a média das 3 notas
    media = (nota1 + nota2 + nota3) / 3
    # Arredonda para duas casas decimais
    media = round(media, 2)

    # Decide o status do aluno
    if media >= 70:
        status = "Aprovado"
    elif media >= 50:
        status = "Em recuperação"
    else:
        status = "Reprovado"

    # Retorna um dicionário (que vira JSON)
    return {
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "status": status
    }