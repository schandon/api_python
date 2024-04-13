from pydantic import BaseModel
from typing import Optional, List
from model.estado import Estado



class EstadoSchema(BaseModel):
    """ Define como um novo estado a ser inserido deve ser representado
    """
    id : int
    nome: str 
    uf: str

    

class EstadoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do estado.
    """
    id: int 


class ListagemEstadosSchema(BaseModel):
    """ Define como uma listagem de estados será retornada.
    """
    estados:List[EstadoSchema]


def apresenta_estados(estados: List[Estado]):
    """ Retorna uma representação do estado seguindo o schema definido em
       EstadoViewSchema.
    """
    result = []
    for estado in estados:
        result.append({
            "id":estado.id,
            "nome": estado.nome,
            "uf": estado.uf,
        })

    return {"estados": result}


class EstadoViewSchema(BaseModel):
    """ Define como um estado será retornado: estado.
    """
    id: int = 1
    nome: str = "Rio de Janeiro"
    uf: str = "RJ"


class EstadoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_estado(estado: Estado):
    """ Retorna uma representação do estado seguindo o schema definido em
        EstadoViewSchema.
    """
    return {
        "id": estado.id,
        "nome": estado.nome,
        "uf": estado.uf
    }
