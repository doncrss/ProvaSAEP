from sqlalchemy import Table, String, Integer, Column, ForeignKey, Float, Relationship, DateTime, func
from datetime import datetime
from database import Base

class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  nome = Column(String, nullable=False)
  senha = Column(String(255), nullable=False)
  email = Column(String, unique=True, nullable=False)
  cargo = Column(String, nullable=False)

class Produto(Base):
  __tablename__ = "produtos"
  id = Column(Integer, primary_key=True, nullable=False, index=True)
  nome = Column(String(30), nullable=False)
  uni_medida = Column(String, nullable=False)
  qtd = Column(Integer, default=0, nullable=False)
  variacao = Column(String, nullable=True)
  peso = Column(Float, default=0, nullable=True)
  movimentacoes = Relationship("movimentacoes", back_populates="produtos")

class Movimentacao(Base):
  __tablename__ = "movimentacoes"
  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  tipo = Column(String, nullable=False)
  data = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  produto_id = Column(ForeignKey("produtos.id"))
  produto = Relationship("Produto", back_populates="movimentacoes")