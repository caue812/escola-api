from sqlalchemy import Column, Integer, String

from src.escola_api.database.banco_dados import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    sigla = Column(String(3), nullable=False)
