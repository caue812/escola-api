from datetime import date, datetime
from typing import List

import uvicorn
<<<<<<< HEAD
from fastapi import HTTPException
from pydantic import BaseModel, Field

from escola_api.api.v1 import aluno_controller
from src.escola_api.api.v1 import curso_controller
from src.escola_api.app import app, router
from src.escola_api.database.banco_dados import Base, engine
Base.metadata.create_all(bind=engine)
app.include_router(curso_controller.router)
app.include_router(aluno_controller.router)
=======
<<<<<<< HEAD
from fastapi import HTTPException
from pydantic import BaseModel, Field

from escola_api.api.v1 import aluno_consoller
from src.escola_api.api.v1 import curso_consoller
from src.escola_api.app import app, router
from src.escola_api.database.banco_dados import Base, engine

app.include_router(curso_consoller.router)
app.include_router(aluno_consoller.router)
>>>>>>> refs/remotes/origin/main


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
<<<<<<< HEAD
=======
=======
from typing_extensions import Optional

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def index():
    return {"mensagem": "Olá mundo"}


@app.get("/calculadora")
def calculadora(numero1: int, numero2: int):
    soma = numero1 + numero2
    return {"soma": soma}


@app.get("/processar-cliente")
def processar_dados_cliente(nome: str, idade: int, sobrenome: str):
    nome_completo = nome + " " + sobrenome
    ano_nascimento = datetime.now().year - idade

    if 1990 <= ano_nascimento < 2000:
        decada = "decada de 90"
    elif 1980 <= ano_nascimento < 1990:
        decada = "decada de 80"
    elif 1970 <= ano_nascimento < 1980:
        decada = "decada de 70"
    else:
        decada = "decada abaixo de 70 ou acima de 90"

    return {
        "nome_completo": nome_completo,
        "ano_nascimento": ano_nascimento,
        "decada": decada,
    }


class Curso(BaseModel):
    id: int = Field()
    nome: str = Field()
    sigla:  Optional[str] = Field(default=None)


class CursoCadastro(BaseModel):
    nome: str = Field()
    sigla:  Optional[str] = Field(default=None)


class CursoEditar(BaseModel):
    nome: str = Field()
    sigla:  Optional[str] = Field(default=None)


cursos = [
    Curso(id=1, nome="Python Web", sigla="PY1"),
    Curso(id=2, nome="Git e GitHub", sigla="GT")
]


@app.get("/api/cursos")
def listar_todos_cursos():
    return cursos


@app.get("/api/cursos/{id}")
def obter_por_id_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@app.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro):
    ultimo_id = max([curso.id for curso in cursos], default=0)
    curso = Curso(id=ultimo_id + 1, nome=form.nome, sigla=form.sigla)
    cursos.append(curso)
    return curso


@app.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            cursos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@app.put("/api/cursos/{id}")
def editar_curso(id: int, form: CursoEditar):
    for curso in cursos:
        if curso.id == id:
            curso.nome = form.nome
            curso.sigla = form.sigla
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


# MODELOS DE ALUNO
class Aluno(BaseModel):
    id: int = Field()
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


class AlunoCadastro(BaseModel):
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


class AlunoEditar(BaseModel):
    nome: str = Field()
    sobrenome: str = Field()
    cpf: str = Field()
    data_nascimento: datetime = Field(alias="dataNascimento")


alunos: List[Aluno] = [
    Aluno(id=1, nome="João", sobrenome="Diniz", cpf="06295095955", dataNascimento=date(1990, 5, 25)),
    Aluno(id=2, nome="Maria", sobrenome="Silva", cpf="12345678901", dataNascimento=date(1995, 8, 15))
]


@app.get("/api/alunos")
def listar_todos_alunos():
    return alunos


@app.get("/api/alunos/{id}")
def obter_aluno_por_id(id: int):
    for aluno in alunos:
        if aluno.id == id:
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@app.post("/api/alunos")
def cadastrar_aluno(form: AlunoCadastro):
    novo_id = max([aluno.id for aluno in alunos], default=0) + 1
    novo_aluno = Aluno(
        id=novo_id,
        nome=form.nome,
        sobrenome=form.sobrenome,
        cpf=form.cpf,
        dataNascimento=form.data_nascimento
    )
    alunos.append(novo_aluno)
    return novo_aluno


@app.put("/api/alunos/{id}")
def editar_aluno(id: int, form: AlunoEditar):
    for aluno in alunos:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf
            aluno.data_nascimento = form.data_nascimento
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@app.delete("/api/alunos/{id}", status_code=204)
def apagar_aluno(id: int):
    for aluno in alunos:
        if aluno.id == id:
            alunos.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")

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



>>>>>>> origin/main
>>>>>>> refs/remotes/origin/main
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
