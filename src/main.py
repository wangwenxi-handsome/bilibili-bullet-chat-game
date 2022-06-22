import pygame
from src.scene import Scene


width = 1542
height = 865
max_comment = 1000


class Game:
    def __init__(self, width = width, height = height):
        self.w = width
        self.h = height
        self.screen = self.get_screen()
        self.scene = Scene(self.screen)

    def get_screen(self, ):
        pygame.init()
        screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('hello world')
        return screen

    def run(self, queue):
        self.scene.render_scene()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            count = 0
            while not queue.empty() and count < max_comment:
                chat = queue.get()
                count += 1
                if chat[1] == "加入" or "加入游戏":
                    self.scene.create_person(chat[0])
                if chat[1] in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
                    self.scene.change_answer(chat[0], chat[1])
            
            # display
            pygame.display.update()


if __name__ == "__main__":
    game = Game(width, height)
    game.run()