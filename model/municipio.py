from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base 

class municipio(Base):
  id = Column("Pk_municipio", Integer, primary_key=True)
  nome = Column(String(60), unique=True)
  data_criacao = colum(DateTime, default=datetime.now())
  data_atualizacao = colum(DateTime, default=datetime.now())
  # id_estado = relationship(Estado)

  def __init__(self, nome:str ): 
    self.nome = nome
