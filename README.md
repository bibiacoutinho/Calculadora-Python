# Calculadora
Projeto de calculadora com logs.

# Entregas
- [x] Interfaces - 10/09/21
- [ ] :hourglass:

# Como instalar
```
git clone git@github.com:bibiacoutinho/Calculadora-Python.git
```
No diretório raiz:
```
virtualenv -p /usr/bin/python3 ENV
source ENV/bin/activate
pip3 install -r requirements.txt
```
Obs: este processo precisa ser feito para cada repositorio do microsserviço correspondente, são eles:
- [Gateway](https://github.com/bibiacoutinho/Gateway)
- [Operação Elementar](https://github.com/bibiacoutinho/Operacoes-Elementares)
- [Operação Transcendente](https://github.com/bibiacoutinho/Operacao-Transcendente)
- [Logs](https://github.com/bibiacoutinho/Logs)

# Como executar
No diretório raiz:
```
cd src
python3 app.py
```
Obs: este processo precisa ser feito para cada repositorio do microsserviço correspondente, citados anteriormente.
Para desativar virtualenv:
```
deactivate
```
# Tecnologias utilizadas
* Python 3.6.9
* Pip 9.0.1
* Virtualenv 20.7.2
