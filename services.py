from sqlalchemy.orm import Session
from models import Usuario, Produto, Movimentacao

def criar_usuario(db: Session, dados: dict):
    usuario = Usuario(**dados)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


def listar_usuarios(db: Session):
    return db.query(Usuario).all()


def buscar_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()


def excluir_usuario(db: Session, usuario_id: int):
    usuario = buscar_usuario(db, usuario_id)

    if usuario is None:
        return None

    db.delete(usuario)
    db.commit()

    return usuario



def criar_produto(db: Session, dados: dict):
    produto = Produto(**dados)

    db.add(produto)
    db.commit()
    db.refresh(produto)

    return produto


def listar_produtos(db: Session):
    return db.query(Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(
        Produto.id == produto_id
    ).first()


def atualizar_produto(db: Session, produto_id: int, dados: dict):
    produto = buscar_produto(db, produto_id)

    if produto is None:
        return None

    for campo, valor in dados.items():
        setattr(produto, campo, valor)

    db.commit()
    db.refresh(produto)

    return produto


def excluir_produto(db: Session, produto_id: int):
    produto = buscar_produto(db, produto_id)

    if produto is None:
        return None

    db.delete(produto)
    db.commit()

    return produto


def criar_movimentacao(db: Session, dados: dict):
    produto = buscar_produto(db, dados["produto_id"])

    if produto is None:
        return None

    tipo = dados["tipo"].lower()
    quantidade = dados.get("quantidade", 1)

    operacoes = {
        "entrada": lambda: setattr(
            produto, "qtd", produto.qtd + quantidade
        ),
        "saida": lambda: setattr(
            produto, "qtd", produto.qtd - quantidade
        )
    }

    if tipo not in operacoes:
        raise ValueError("Tipo de movimentação inválido")

    if tipo == "saida" and produto.qtd < quantidade:
        raise ValueError("Estoque insuficiente")

    operacoes[tipo]()

    movimentacao = Movimentacao(**dados)

    db.add(movimentacao)
    db.commit()
    db.refresh(movimentacao)

    return movimentacao


def listar_movimentacoes(db: Session):
    return db.query(Movimentacao).all()


def buscar_movimentacao(db: Session, movimentacao_id: int):
    return db.query(Movimentacao).filter(
        Movimentacao.id == movimentacao_id
    ).first()