import requests


def main() -> None:
    print("Starting Pokemon Client")
    response = requests.get("https://api.tcgdex.net/v2/en/cards/swsh3-136")
    print(response.json()["name"])
    print(response.json()["rarity"])
    print("Stopping Pokemon Client")

if __name__ == "__main__":
    main()