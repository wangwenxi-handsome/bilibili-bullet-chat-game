import random
import pygame
import numpy as np
from src.person import Person


w_start = 27
w_end = 1454
w_num = 45
h_start = 2
h_end = 790
h_num = 15
font_size = 10

font_h_ = 20


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.prepare_pic()
        self.init_pos()
        self.ava_ids = list(range(1, self.num + 1))
        self.people = {}
        self.font = pygame.font.Font("font/BOBOHEI-2.otf", font_size)

    def prepare_pic(self):
        self.map = pygame.image.load("pic/map.jpg").convert()
        self.r_cell = pygame.image.load("pic/red_cell.png").convert_alpha()
        self.y_cell = pygame.image.load("pic/yello_cell.png").convert_alpha()
        self.b_cell = pygame.image.load("pic/blue_cell.png").convert_alpha()
        self.g_cell = pygame.image.load("pic/green_cell.png").convert_alpha()
        self.cell = {"r": self.r_cell, "y": self.y_cell, "b": self.b_cell, "g": self.g_cell}

    def init_pos(self, ):
        w_pos = list(np.linspace(w_start, w_end, num=w_num, endpoint=True))
        h_pos = list(np.linspace(h_start, h_end, num=h_num, endpoint=True))
        self.pos = {}
        num = 0
        for i, h in enumerate(h_pos):
            for j, w in enumerate(w_pos):
                if (i % 2 == 0) != (j % 2 == 0):
                    num += 1
                    self.pos[num] = (int(w), int(h))
        self.num = num

    def if_have_ids(self):
        return len(self.ava_ids) > 0

    def create_person(self, name):
        if name in self.people or (not self.if_have_ids()):
            return
        id = random.choice(self.ava_ids)
        self.ava_ids.remove(id)
        person = Person(id, name, self.font)
        self.people[name] = person
        self.render_person(self.people[name])

    def delete_person(self, name):
        self.ava_ids.append(self.people[name].id)
        self.people.pop(name)

    def change_answer(self, name, answer):
        if name not in self.people:
            return
        if answer in ['a', 'A']:
            self.people[name].change_answer('r')
        if answer in ['b', 'B']:
            self.people[name].change_answer('y')
        if answer in ['c', 'C']:
            self.people[name].change_answer('b')
        if answer in ['d', 'D']:
            self.people[name].change_answer('g')
        self.render_person(self.people[name])
        
    def render_scene(self):
        self.render_map()
        for name in self.people:
            self.render_person(self.people[name])

    def render_map(self):
        self.screen.blit(self.map, (0, 0))

    def render_person(self, person):
        self.render_cell(person.id, person.color)
        self.screen.blit(person.name, (self.pos[person.id][0], self.pos[person.id][1] + 30))

    def render_cell(self, id, color = None):
        if color:
            if not isinstance(id, list):
                id = [id]
            for i in id:
                self.screen.blit(self.cell[color], self.pos[i])

    def render_debug(self):
        for id in self.pos:
            color = random.choice(["r", "y", "b", "g"])
            self.render_cell(self.screen, id, color)