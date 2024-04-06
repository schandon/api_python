# Minha API

Este pequeno projeto faz parte do material para uma aplicação de busca a informações do IBGE.

Tem como objetivo pegar informações pesquisadas por nossos usuarios e salva-los num banco de dados interno.

---
## Como executar
Para não precisar instalar as bivliotecas na sua maquina, iremos utilizar a virtualização, como isso iremos seguir um conjunto de passos.
  * Passo 1:
    * Executar o código para criar a pasta do ambiente
 ```
      python -m venv env
```
  * Passo 2:
    * Entrar na modo virtualizado, executando o código
```
      env\Scripts\activate
```
##### OBS.
  * Passo 2.1:
    * Em caso de erro na criação do ambiente virtualizado, utilizaremos o comando a seguir, caso não de erro ao utilizar o Passo 02, ignore o Passo. 
```
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
``` 
  * Passo 3:
    * Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo. 
```
    pip install -r requirements.txt 
```
  * Passo 4:
    * Para executar a API  basta executar:
```
    flask run --host 0.0.0.0 --port 5000 --reload
```