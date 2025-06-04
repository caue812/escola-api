#
#
# @router.post("/api/professores")
# def cadastrar_professor(form: ProfessorCadastro):
#     novo_id = max([professor_item.id for professor_item in professores], default=0) + 1
#     signo = calcular_signo(form.data_nascimento)
#     novo_professor = Professor(
#         id=novo_id,
#         nome=form.nome,
#         cnpj=form.cnpj,
#         nome_fantasia=form.nome_fantasia,
#         chave_pix=form.chave_pix,
#         formacao=form.formacao,
#         data_nascimento=form.data_nascimento,
#         signo=signo
#     )
#     professores.append(novo_professor)
#     return novo_professor
#
#
# @router.put("/api/professores/{id}")
# def editar_professor(id: int, form: ProfessorEditar):
#     for professor_item in professores:
#         if professor_item.id == id:
#             professor_item.nome = form.nome
#             professor_item.cnpj = form.cnpj
#             professor_item.nome_fantasia = form.nome_fantasia
#             professor_item.chave_pix = form.chave_pix
#             professor_item.formacao = form.formacao
#             professor_item.data_nascimento = form.data_nascimento
#             professor_item.signo = calcular_signo(form.data_nascimento)
#             return professor_item
#     raise HTTPException(status_code=404, detail=f"Professor com id {id} não encontrado")
