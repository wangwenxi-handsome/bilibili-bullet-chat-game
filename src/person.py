import time
import pygame


class Person:
    def __init__(self, id, name, font):
        self.id = id
        self.name = self.create_name(name, font)
        self.color = None
        self.time = time.time()

    def update_active_time(self, ):
        self.time = time.time()

    def if_delete(self, time):
        if time.time() - self.time > 60:
            return True
        else:
            return False

    def create_name(self, name, font):
        if len(name) > 10:
            name = name[:10]
        return font.render(name, True, (0, 0, 0))

    def change_answer(self, color):
        self.color = color
        self.update_active_time()