from datetime import date

from pydantic import BaseModel, Field



class MatriculaBase(BaseModel):
    aluno_id: int = Field()
    curso_id: int = Field()

class Matricula(MatriculaBase):
    data_matricula: date = Field(alias="dataMatricula")

class MatriculaCadastro(BaseModel):
        pass

class MatriculaCadastro(BaseModel):
    curso_id: int



