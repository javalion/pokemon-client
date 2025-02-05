import requests
from pokemon import Pokemon


def main() -> None:
    print("Starting Pokemon Client")
    response = requests.get("https://api.tcgdex.net/v2/en/cards/swsh3-136")
    pokemon = Pokemon(**response.json())
    print(pokemon)
    print(pokemon.name)
    print(pokemon.rarity)
    print("Stopping Pokemon Client")

if __name__ == "__main__":
    main()