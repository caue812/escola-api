# from pydantic import Field, BaseModel
#
#
# class Professor(BaseModel):
#     id: int
#     nome: str
#     cnpj: str
#     nome_fantasia: str = Field(alias="nomeFantasia")
#     chave_pix: str = Field(alias="chavePix")
#     formacao: str
#     data_nascimento: date = Field(alias="dataNascimento")
#     signo: str
#
#
# class ProfessorCadastro(BaseModel):
#     nome: str
#     cnpj: str
#     nome_fantasia: str = Field(alias="nomeFantasia")
#     chave_pix: str = Field(alias="chavePix")
#     formacao: str
#     data_nascimento: date = Field(alias="dataNascimento")
#
#
# class ProfessorEditar(ProfessorCadastro):
#     pass
#
#
# professores: List[Professor] = []

