from fastapi import  HTTPException
from fastapi.params import Depends
from requests import Session

from escola_api.database.banco_dados import SessionLocal
from escola_api.database.modelos import CursoEntidade
from src.escola_api.schemas.curso_schemas import Curso, CursoCadastro, CursoEditar
from src.escola_api.app import router



cursos = [
    Curso(id=1, nome="Python Web", sigla="PY1"),
    Curso(id=2, nome="Git e GitHub", sigla="GT")
]

#Função de dependência para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal() # Cria uma nova sessão do banco de dados
    try:
        yield db # Retorna a sessão de forma que o FastAPI possa utilizá-la nas rotas
    finally:
        db.close() # Gerante que a sessão será fechada após o uso



@router.get("/api/cursos")
def listar_todos_cursos(db: Session = Depends(get_db)):
    cursos = db.query(CursoEntidade).all()
    return cursos


@router.get("/api/cursos/{id}")
def obter_por_id_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro):
    ultimo_id = max([curso.id for curso in cursos], default=0)
    curso = Curso(id=ultimo_id + 1, nome=form.nome, sigla=form.sigla)
    cursos.append(curso)
    return curso


@router.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            cursos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.put("/api/cursos/{id}")
def editar_curso(id: int, form: CursoEditar):
    for curso in cursos:
        if curso.id == id:
            curso.nome = form.nome
            curso.sigla = form.sigla
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")
