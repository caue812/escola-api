from fastapi import HTTPException
from fastapi.params import Depends
from requests import Session

from src.escola_api.database.banco_dados import SessionLocal
from src.escola_api.database.modelos import CursoEntidade
from src.escola_api.schemas.curso_schemas import Curso, CursoCadastro, CursoEditar
from src.escola_api.app import router

cursos = [
    Curso(id=1, nome="Python Web", sigla="PY1"),
    Curso(id=2, nome="Git e GitHub", sigla="GT")
]


# Função de dependência para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()  # Cria uma nova sessão do banco de dados
    try:
        yield db  # Retorna a sessão de forma que o FastAPI possa utilizá-la nas rotas
    finally:
        db.close()  # Gerante que a sessão será fechada após o uso


@router.get("/api/cursos")
def listar_todos_cursos(db: Session = Depends(get_db)):
    cursos = db.query(CursoEntidade).all()
    return cursos


@router.get("/api/cursos/{id}")
def obter_por_id_curso(id: int, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.post("/api/cursos")
def cadastrar_curso(form: CursoCadastro, db: Session = Depends(get_db)):
    # Instanciar um objeto da classe Curso
    curso = CursoEntidade(nome=form.nome, sigla=form.sigla)
    db.add(curso) # INSERT
    db.commit() # Efetivando o registro  na tabela
    db.refresh(curso) # preenchendo o id que foi gerado no banco de dados

    return curso


@router.delete("/api/cursos/{id}", status_code=204)
def apagar_curso(id: int):
    for curso in cursos:
        if curso.id == id:
            cursos.remove(curso)
            return
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")


@router.put("/api/cursos/{id}")
def editar_curso(id: int, form: CursoEditar, db: Session = Depends(get_db)):
    curso = db.query(CursoEntidade).filter(CursoEntidade.id == id).first()
    if curso:
            curso.nome = form.nome
            curso.sigla = form.sigla
            db.commit()
            db.reflesh()
            return curso
    raise HTTPException(status_code=404, detail=f"Curso não encontrado com id: {id}")
