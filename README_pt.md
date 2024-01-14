**Xbox Gamertag Tracker**
[English](README.md) | Português


Este script em Python permite rastrear e verificar a existência de Gamertags em sites relacionados ao Xbox. Ele consulta os seguintes sites:

- [xboxgamertag.com](https://xboxgamertag.com/)
- [trueachievements.com](https://www.trueachievements.com/)

O script utiliza a biblioteca `requests` para realizar solicitações HTTP e `BeautifulSoup` para análise HTML.

## Requisitos

- Python
- Bibliotecas Python: `requests`, `beautifulsoup4`

## Uso

1. Clone este repositório:

```bash
git clone https://github.com/kensdy/Xbox-Gamertag-Tracking
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script:

```bash
python xbox_gamertag_tracker.py
```

## Configuração

Você pode configurar a exibição de logs alterando a variável `exibir_logs` para `True` ou `False` no início do script.

## Exemplo de Uso

```bash
Digite o nome a ser verificado: gamertag_exemplo
```

Este script é inspirado no projeto [Sherlock](https://github.com/sherlock-project/sherlock).
