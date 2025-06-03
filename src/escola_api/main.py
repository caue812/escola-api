from datetime import date
from typing import List

import uvicorn
from fastapi import HTTPException
from pydantic import Field, BaseModel

from src.escola_api.api.v1 import aluno_controller
from src.escola_api.database.banco_dados import Base, engine
from src.escola_api.api.v1 import curso_controller
from src.escola_api.app import app

app.include_router(aluno_controller.router)
app.include_router(curso_controller.router)

Base.metadata.create_all(bind=engine)


class Formacao(BaseModel):
    id: int
    nome: str
    descricao: str
    duracao: str

class FormacaoCadastro(BaseModel):
    nome: str
    descricao: str
    duracao: str

class FormacaoEditar(BaseModel):
    descricao: str


formacoes: List[Formacao] = []


@app.get("/api/formacoes")
def listar_formacoes():
    return formacoes


@app.post("/api/formacoes")
def cadastrar_formacao(form: FormacaoCadastro):
    novo_id = max([formacao_item.id for formacao_item in formacoes], default=0) + 1
    nova_formacao = Formacao(
        id=novo_id,
        nome=form.nome,
        descricao=form.descricao,
        duracao=form.duracao
    )
    formacoes.append(nova_formacao)
    return nova_formacao


@app.put("/api/formacoes/{id}")
def editar_formacao(id: int, form: FormacaoEditar):
    for formacao_item in formacoes:
        if formacao_item.id == id:
            formacao_item.descricao = form.descricao
            return formacao_item
    raise HTTPException(status_code=404, detail=f"Formação com id {id} não encontrada")

class Professor(BaseModel):
    id: int
    nome: str
    cnpj: str
    nome_fantasia: str = Field(alias="nomeFantasia")
    chave_pix: str = Field(alias="chavePix")
    formacao: str
    data_nascimento: date = Field(alias="dataNascimento")
    signo: str

class ProfessorCadastro(BaseModel):
    nome: str
    cnpj: str
    nome_fantasia: str = Field(alias="nomeFantasia")
    chave_pix: str = Field(alias="chavePix")
    formacao: str
    data_nascimento: date = Field(alias="dataNascimento")

class ProfessorEditar(ProfessorCadastro):
    pass


professores: List[Professor] = []


def calcular_signo(data_nasc: date) -> str:
    dia = data_nasc.day
    mes = data_nasc.month
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return "Áries"
    if (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Touro"
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return "Capricórnio"
    if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
        return "Aquário"
    if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    return "Desconhecido"


@app.get("/api/professores")
def listar_professores():
    return professores


@app.post("/api/professores")
def cadastrar_professor(form: ProfessorCadastro):
    novo_id = max([professor_item.id for professor_item in professores], default=0) + 1
    signo = calcular_signo(form.data_nascimento)
    novo_professor = Professor(
        id=novo_id,
        nome=form.nome,
        cnpj=form.cnpj,
        nome_fantasia=form.nome_fantasia,
        chave_pix=form.chave_pix,
        formacao=form.formacao,
        data_nascimento=form.data_nascimento,
        signo=signo
    )
    professores.append(novo_professor)
    return novo_professor


@app.put("/api/professores/{id}")
def editar_professor(id: int, form: ProfessorEditar):
    for professor_item in professores:
        if professor_item.id == id:
            professor_item.nome = form.nome
            professor_item.cnpj = form.cnpj
            professor_item.nome_fantasia = form.nome_fantasia
            professor_item.chave_pix = form.chave_pix
            professor_item.formacao = form.formacao
            professor_item.data_nascimento = form.data_nascimento
            professor_item.signo = calcular_signo(form.data_nascimento)
            return professor_item
    raise HTTPException(status_code=404, detail=f"Professor com id {id} não encontrado")




if __name__ == "__main__":
    uvicorn.run("main:app")