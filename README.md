**Xbox Gamertag Tracker**

This Python script allows tracking and checking the existence of Gamertags on Xbox-related websites. It queries the following sites:

- [xboxgamertag.com](https://xboxgamertag.com/)
- [trueachievements.com](https://www.trueachievements.com/)

The script uses the `requests` library for making HTTP requests and `BeautifulSoup` for HTML parsing.

## Requirements

- Python
- Python libraries: `requests`, `beautifulsoup4`

## Usage

1. Clone this repository:

```bash
git clone https://github.com/kensdy/Xbox-Gamertag-Tracking
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python xbox_gamertag_tracker.py
```

## Configuration

You can configure log display by changing the `exibir_logs` variable to `True` or `False` at the beginning of the script.

## Usage Example

```bash
Enter the name to be checked: example_gamertag
```

This script is inspired by the [Sherlock](https://github.com/sherlock-project/sherlock) project.

---

Confira o [readme.md](https://github.com/kensdy/Xbox-Gamertag-Tracking/blob/main/PT-BR_README.md) em potuguês 🇧🇷.
