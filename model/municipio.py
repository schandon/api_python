from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base 

class municipio(Base):
  __tablename__ = 'municipio'

  id = Column("Pk_municipio", Integer, primary_key=True)
  nome = Column(String(60), unique=True)
  data_criacao = Column(DateTime, default=datetime.now())
  data_atualizacao = Column(DateTime, default=datetime.now())
  estado = Column(Integer, ForeignKey("produto.pk_estado"), nullable=False)

  def __init__(self, nome:str, data_atualizacao: Union[DateTime, None] = None): 
    self.nome = nome
    if data_atualizacao :
      self.data_atualizacao = data_atualizacao