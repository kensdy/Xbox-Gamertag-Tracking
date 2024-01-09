import requests
from bs4 import BeautifulSoup
import logging

# Constantes para cabeçalhos HTTP
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Configurando o sistema de logs
exibir_logs = False  # Defina como False se não quiser exibir logs
if exibir_logs:
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def exibir_ascii_art():
    # Arte ASCII de exemplo
    ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀        
⠀⠀⠀⠀⠀⡀⠀⠈⠉⠛⠿⣿⣿⣿⣿⠿⠛⠉⠁⠀⢀⠀⠀⠀⠀⠀       
⠀⠀⠀⣴⣿⣿⣿⣶⣄⡀⠀⠈⠙⠋⠁⠀⢀⣠⣶⣿⣿⣿⣦⠀⠀⠀      
⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⠀⠐⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀     
⠀⣾⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⢀⡀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣷⠀      
⢠⣿⣿⣿⣿⣿⡟⠁⠀⠀⢀⣴⣿⣿⣦⡀⠀⠀⠈⢻⣿⣿⣿⣿⣿⡄    
⢸⣿⣿⣿⣿⠏⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠹⣿⣿⣿⣿⡇     
⠘⣿⣿⣿⠏⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠹⣿⣿⣿⠃    
⠀⢿⣿⡟⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⢻⣿⡿⠀     
⠀⠈⢿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⡿⠁⠀    
⠀⠀⠀⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠀⠀⠀     
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀      
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀         
  _   _                             
 | | | |___  ___ _ __               
 | | | / __|/ _ \ '__|              
 | |_| \__ \  __/ |                 
  \___/|___/\___|_|   _             
 |_   _| __ __ _| | _(_)_ __   __ _ 
   | || '__/ _` | |/ / | '_ \ / _` |
   | || | | (_| |   <| | | | | (_| |
   |_||_|  \__,_|_|\_\_|_| |_|\__, |
                              |___/ 
   Criado Por Kensdy
    """
    print(ascii_art)

def verifica_gamertag(gamertag):
    url = f"https://xboxgamertag.com/search/{gamertag}"

    try:
        resposta = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resposta.text, 'html.parser')

        gamertag_not_exist = soup.find('h1', string=lambda text: 'Gamertag doesn\'t exist' in text)
        gamertag_exist = soup.find('h1', string=True)

        # Adiciona uma linha em branco antes dos logs
        print("\n")

        if gamertag_not_exist:
            if exibir_logs:
                logger.info(f"Não encontrado nenhum usuário com o nick {gamertag} no site https://xboxgamertag.com/.")
            print(f"Não encontrado nenhum usuário com o nick {gamertag} no site https://xboxgamertag.com/.")
        elif gamertag_exist:
            if exibir_logs:
                logger.info(f"Usuário com o nick {gamertag} encontrado no site {url}.")
            print(f"Usuário com o nick {gamertag} encontrado no site {url}.")

            # Buscar Gamerscore e Games Played diretamente do perfil
            profile_details = soup.find('div', class_='col-sm-12')
            gamerscore = profile_details.find('span', string='Gamerscore')
            games_played = profile_details.find('span', string='Games Played')

            if gamerscore:
                if exibir_logs:
                    logger.info(f"Gamerscore: {gamerscore.find_next('span').get_text(strip=True)}")

            if games_played:
                if exibir_logs:
                    logger.info(f"Games Played: {games_played.find_next('span').get_text(strip=True)}")

        else:
            if exibir_logs:
                logger.warning(f"Não foi possível determinar o status da Gamertag '{gamertag}'.")
            print(f"Não foi possível determinar o status da Gamertag '{gamertag}'.")

    except requests.ConnectionError:
        if exibir_logs:
            logger.error(f"Não foi possível acessar a URL {url}.")

def verifica_usuario(username):
    url = f"https://www.trueachievements.com/gamer/{username}"

    try:
        resposta = requests.get(url, headers=HEADERS)
        resposta.raise_for_status()  # Isso vai gerar uma exceção se a resposta for um erro HTTP (como 404)
        soup = BeautifulSoup(resposta.text, 'html.parser')

        gamertag_element = soup.select_one('div.tabs li.tab_green span')
        if gamertag_element:
            gamertag = gamertag_element.text
            if exibir_logs:
                logger.info(f"Usuário com o nick {username} encontrado no site {url}.")
            print(f"Usuário com o nick {username} encontrado no site {url}.")

        else:
            if exibir_logs:
                logger.info(f"Não encontrado nenhum usuário com o nick {username} no site https://www.trueachievements.com/.")
            print(f"Não encontrado nenhum usuário com o nick {username} no site https://www.trueachievements.com/.")

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            if exibir_logs:
                logger.info(f"Não encontrado nenhum usuário com o nick {username} no site https://www.trueachievements.com/.")
            print(f"Não encontrado nenhum usuário com o nick {username} no site https://www.trueachievements.com/.")
        else:
            if exibir_logs:
                logger.error(f"Erro ao acessar a URL {url}: {e}")

def main():
    # Exibir arte ASCII
    exibir_ascii_art()

    # Solicitar ao usuário para inserir o nome a ser verificado
    nome_a_verificar = input("Digite o nome a ser verificado: ")

    # Executar ambas as funções para o nome fornecido
    verifica_gamertag(nome_a_verificar)
    verifica_usuario(nome_a_verificar)

if __name__ == "__main__":
    main()
