from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Estado(Base):
    __tablename__ = 'estado'

    id = Column("id", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    uf = Column(String(2), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, uf:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.uf = uf

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


