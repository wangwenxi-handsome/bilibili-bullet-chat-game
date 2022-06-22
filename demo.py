import pygame
import random
import time


width = 800
height = 560
width_center = (0, 730)
height_center = (280, 490)
font_size = 10
move = 20
people = {}


def create_person(screen, raw_pic, font, name = "熙熙"):
    person = Person(name, raw_pic, font)
    people[name] = person


def show_people(screen):
    for name in people:
        if time.time() - people[name].time > 1800:
            people.pop(name)
        screen.blit(people[name].pic, (people[name].w, people[name].h))

    for name in people:
        screen.blit(people[name].name, (people[name].w, people[name].h - 20))


def play_music():
    # music
    pygame.mixer.init()
    pygame.mixer.music.load("music/red_shoes.mp3") # 加载歌曲
    pygame.mixer.music.play(loops = -1) # 播放


def game_init():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('hello world')
    return screen


def run(queue):
    screen = game_init()

    # pic
    background = pygame.image.load("pic/background.jpeg").convert()
    dijia = pygame.image.load("pic/dijia.png").convert_alpha()

    # font
    font = pygame.font.Font("font/BOBOHEI-2.otf", font_size)

    # music
    play_music()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # backgroud
        screen.blit(background, (0, 0))

        # people
        if not queue.empty():
            chat = queue.get()
            if chat[0] not in people and chat[1] == "创建角色":
                create_person(screen, dijia, font, chat[0])
            if chat[0] in people:
                people[chat[0]].update(chat[1])
        show_people(screen)
        
        # display
        pygame.display.update()


class Person:
    def __init__(self, name, raw_pic, font):
        self.name = font.render(name, True, (255, 255, 255))
        self.w = random.randint(*width_center)
        self.h = random.randint(*height_center)
        self.person_size = int((self.h + 70) / height * 70)
        self.pic = pygame.transform.scale(raw_pic, (self.person_size, self.person_size))
        self.time = time.time()

    def update(self, word):
        if word == "w":
            self.h = max(0, self.h - move)
            self.person_size = int((self.h + 70) / height * 70)
        if word == "s":
            self.h = min(height, self.h + move)
            self.person_size = int((self.h + 70) / height * 70)
        if word == "a":
            self.w = max(0, self.w - move)
            self.person_size = int((self.h + 70) / height * 70)
        if word == "d":
            self.w = min(width, self.w + move)
            self.person_size = int((self.h + 70) / height * 70)


if __name__ == "__main__":
    run()