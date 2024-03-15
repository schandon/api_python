from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Estado(Base):
  __tablename__ = "estado"

  id = Column("pk_estado", Integer, primary_key=True)
  nome = Column(String(60))
  uf = Column(String(2), unique=True)
  data_criacao = Column(DateTime, default=datetime.now())
  data_atualizacao = Column(DateTime, default=datetime.now())
  # id_municipio = relationship(Municipio)


  def __init__(self, id: int, nome:str, uf:str,
              data_atualizacao: Union[DateTime, None] = None,
              data_criacao:Union[DateTime, None] = None  ):
    self.id = id
    self.nome = nome
    self.uf = uf

    if data_criacao:
      self.data_criacao = data_criacao

    if data_atualizacao:
      self.data_atualizacao = data_atualizacao