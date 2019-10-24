from utils import trello


def main():
    trello_api = trello.TrelloAPI()
    trello_api.post()


if __name__ == '__main__':
    main()
