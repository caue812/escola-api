from datetime import date, datetime
from typing import List

import uvicorn
from fastapi import HTTPException
from pydantic import BaseModel, Field

from escola_api.api.v1 import aluno_controller
from src.escola_api.api.v1 import curso_controller
from src.escola_api.app import app, router
from src.escola_api.database.banco_dados import Base, engine

Base.metadata.create_all(bind=engine)
app.include_router(curso_controller.router)
app.include_router(aluno_controller.router)

#
# @router.get("/")
# def index():
#     return {"mensagem": "Olá mundo"}
#
#
# @router.get("/calculadora")
# def calculadora(numero1: int, numero2: int):
#     soma = numero1 + numero2
#     return {"soma": soma}
#
#
# @router.get("/processar-cliente")
# def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
#     nome_completo = nome + " " + sobrenome
#     ano_nascimento = datetime.now().year - idade
#
#     if 1990 <= ano_nascimento < 2000:
#         decada = "decada de 90"
#     elif 1980 <= ano_nascimento < 1990:
#         decada = "decada de 80"
#     elif 1970 <= ano_nascimento < 1980:
#         decada = "decada de 70"
#     else:
#         decada = "decada abaixo de 70 ou acima de 90"
#
#     return {
#         "nome_completo": nome_completo,
#         "ano_nascimento": ano_nascimento,
#         "decada": decada,
#     }


Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
