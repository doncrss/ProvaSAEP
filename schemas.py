from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

class UsuarioCreate(BaseModel):
  id = str
  nome = str
  cargo = str
  email = EmailStr
  senha = str

class UsuarioUpdate(BaseModel):
  id = str
  nome = Optional[str] = None
  email = Optional[EmailStr] = None
  senha = Optional[str] = None

class UsuarioResponse(BaseModel):
  id = str 
  nome = str 
  email: EmailStr

class ProdutoCreate(BaseModel):
  id = str
  tipo = str
  uni_medida = str
  qtd = str
  variacao = str
  peso = float

class ProdutoUpdate(BaseModel):
  id = Optional[str] = None
  tipo = Optional[str] = None
  uni_medida = Optional[str] = None
  qtd = Optional[str] = None
  variacao = Optional[str] = None
  peso = Optional[float] = None

class ProdutoResponse(BaseModel):
  id = str
  tipo = str
  uni_medida = str
  qtd = str
  variacao = str
  peso = float

class MovimentacaoCreate(BaseModel):
  id = str
  data = datetime
  tipo = str

class MovimentacaoResponse(BaseModel):
  id = str
  data = datetime
  tipo = str