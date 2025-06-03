from typing_extensions import List

from src.escola_api.schemas.aluno_schemas import Aluno, AlunoEditar, AlunoCadastro
from src.escola_api.app import router
from datetime import date
from fastapi import HTTPException, status


alunos: List[Aluno] = [
    Aluno(id=1, nome="João", sobrenome="Diniz", cpf="06295095955", dataNascimento=date(1990, 5, 25)),
    Aluno(id=2, nome="Maria", sobrenome="Silva", cpf="12345678901", dataNascimento=date(1995, 8, 15))
]


@router.get("/api/alunos")
def listar_todos_alunos():
    return alunos


@router.get("/api/alunos/{id}")
def obter_aluno_por_id(id: int):
    for aluno in alunos:
        if aluno.id == id:
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.post("/api/alunos")
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


@router.put("/api/alunos/{id}")
def editar_aluno(id: int, form: AlunoEditar):
    for aluno in alunos:
        if aluno.id == id:
            aluno.nome = form.nome
            aluno.sobrenome = form.sobrenome
            aluno.cpf = form.cpf
            aluno.data_nascimento = form.data_nascimento
            return aluno
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")


@router.delete("/api/alunos/{id}", status_code=204)
def apagar_aluno(id: int):
    for aluno in alunos:
        if aluno.id == id:
            alunos.remove(aluno)
            return
    raise HTTPException(status_code=404, detail=f"Aluno não encontrado com id: {id}")