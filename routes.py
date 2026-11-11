from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import services

router = APIRouter()


@router.post("/usuarios", status_code=201)
def criar_usuario(dados: dict, db: Session = Depends(get_db)):
    return services.criar_usuario(db, dados)


@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    return services.listar_usuarios(db)


@router.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = services.buscar_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario


@router.delete("/usuarios/{usuario_id}")
def excluir_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = services.excluir_usuario(db, usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {"mensagem": "Usuário excluído com sucesso"}


@router.post("/produtos", status_code=201)
def criar_produto(dados: dict, db: Session = Depends(get_db)):
    return services.criar_produto(db, dados)


@router.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    return services.listar_produtos(db)


@router.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = services.buscar_produto(db, produto_id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


@router.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    dados: dict,
    db: Session = Depends(get_db)
):
    produto = services.atualizar_produto(db, produto_id, dados)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


@router.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = services.excluir_produto(db, produto_id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return {"mensagem": "Produto excluído com sucesso"}

@router.post("/movimentacoes", status_code=201)
def criar_movimentacao(dados: dict, db: Session = Depends(get_db)):
    try:
        movimentacao = services.criar_movimentacao(db, dados)

        if movimentacao is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")

        return movimentacao

    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@router.get("/movimentacoes")
def listar_movimentacoes(db: Session = Depends(get_db)):
    return services.listar_movimentacoes(db)


@router.get("/movimentacoes/{movimentacao_id}")
def buscar_movimentacao(
    movimentacao_id: int,
    db: Session = Depends(get_db)
):
    movimentacao = services.buscar_movimentacao(db, movimentacao_id)

    if movimentacao is None:
        raise HTTPException(
            status_code=404,
            detail="Movimentação não encontrada"
        )

    return movimentacao