import requests
from bs4 import BeautifulSoup
import logging

# Constants for HTTP headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Setting up the logging system
display_logs = False  # Set to False if you do not want to display logs
if display_logs:
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def display_ascii_art():
    # Example ASCII art
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
   Created by Kensdy
    """
    print(ascii_art)

def check_gamertag(gamertag):
    url = f"https://xboxgamertag.com/search/{gamertag}"

    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')

        gamertag_not_exist = soup.find('h1', string=lambda text: 'Gamertag doesn\'t exist' in text)
        gamertag_exist = soup.find('h1', string=True)

        # Add a blank line before logs
        print("\n")

        if gamertag_not_exist:
            if display_logs:
                logger.info(f"No user found with the gamertag {gamertag} on https://xboxgamertag.com/.")
            print(f"No user found with the gamertag {gamertag} on https://xboxgamertag.com/.")
        elif gamertag_exist:
            if display_logs:
                logger.info(f"User with gamertag {gamertag} found on {url}.")
            print(f"User with gamertag {gamertag} found on {url}.")

            # Fetch Gamerscore and Games Played directly from the profile
            profile_details = soup.find('div', class_='col-sm-12')
            gamerscore = profile_details.find('span', string='Gamerscore')
            games_played = profile_details.find('span', string='Games Played')

            if gamerscore:
                if display_logs:
                    logger.info(f"Gamerscore: {gamerscore.find_next('span').get_text(strip=True)}")

            if games_played:
                if display_logs:
                    logger.info(f"Games Played: {games_played.find_next('span').get_text(strip=True)}")

        else:
            if display_logs:
                logger.warning(f"Could not determine the status of the gamertag '{gamertag}'.")
            print(f"Could not determine the status of the gamertag '{gamertag}'.")

    except requests.ConnectionError:
        if display_logs:
            logger.error(f"Could not access the URL {url}.")

def check_user(username):
    url = f"https://www.trueachievements.com/gamer/{username}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # This will raise an exception if the response is an HTTP error (like 404)
        soup = BeautifulSoup(response.text, 'html.parser')

        gamertag_element = soup.select_one('div.tabs li.tab_green span')
        if gamertag_element:
            gamertag = gamertag_element.text
            if display_logs:
                logger.info(f"User with username {username} found on {url}.")
            print(f"User with username {username} found on {url}.")

        else:
            if display_logs:
                logger.info(f"No user found with the username {username} on https://www.trueachievements.com/.")
            print(f"No user found with the username {username} on https://www.trueachievements.com/.")

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            if display_logs:
                logger.info(f"No user found with the username {username} on https://www.trueachievements.com/.")
            print(f"No user found with the username {username} on https://www.trueachievements.com/.")
        else:
            if display_logs:
                logger.error(f"Error accessing the URL {url}: {e}")

def main():
    # Display ASCII art
    display_ascii_art()

    # Prompt the user to input the name to be checked
    name_to_check = input("Enter the name to be checked: ")

    # Execute both functions for the provided name
    check_gamertag(name_to_check)
    check_user(name_to_check)

if __name__ == "__main__":
    main()
