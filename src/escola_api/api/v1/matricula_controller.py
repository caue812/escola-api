from src.escola_api.app import router


@router.get("/api/matriculas", status_code=200, tags=["matriculas"])
def listar_todos_matriculas():
    pass


@router.post("/api/matriculas", status_code=200, tags=["matriculas"])
def cadastrar_matricula():
    pass

@router.delete("/api/matriculas{id}", status_code=204, tags=["matriculas"])
def apagar_matricula():
    pass

@router.put("/api/matriculas{id}", status_code=204, tags=["matriculas"])
def editar_matricula():
    pass

@router.get("/api/matriculas{id}", status_code=204, tags=["matriculas"])
def obter_por_id_matricula():
    pass
