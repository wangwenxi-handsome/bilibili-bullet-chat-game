import multiprocessing
from listen import warp_main
from src.main import Game

def get_chat(quene):
    chats = {}
    while(1):
        chat = quene.get()
        if chat[0] in chats:
            chats[chat[0]].append(chat[1])
        else:
            chats[chat[0]] = [chat[1]]
        print(chat)


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    listen = multiprocessing.Process(target=warp_main, args=(queue,))
    listen.start()

    game = Game()
    game.run(queue)