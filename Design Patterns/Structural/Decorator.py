from abc import ABC, abstractmethod


class BasePlayer:

    def __init__(self):
        pass

    def handle_input(self, c):

        if   c=='w':
            print('moving forward')
        elif c == 'a':
            print('moving left')
        elif c == 's':
            print('moving back')
        elif c == 'd':
            print('moving right')
        elif c == 'e':
            print('attacking ')
        elif c == ' ':
            print('jumping')
        else:
            print('undefined command')


class AbstractDecorator(ABC):

    def __init__(self, wrapee):
        self.wrapee = wrapee

    @abstractmethod 
    def handle_input(self, c):
        pass


class BowmanPlayer(AbstractDecorator):

    def handle_input(self, c):
        if c == 'e':
            print('With arrows ', end='')

        self.wrapee.handle_input(c)


class BlazingPlayer(AbstractDecorator):

    def handle_input(self, c):
        if c == 'e':
            print('With fire ', end='')

        self.wrapee.handle_input(c)


class BouncyPlayer(AbstractDecorator):

    def handle_input(self, c):
        if c == ' ':
            print('Double Jupm ', end='')

        self.wrapee.handle_input(c)


player = BasePlayer()
player.handle_input('e')
player.handle_input(' ')

player = BlazingPlayer(player)
player.handle_input('e')
player.handle_input(' ')

player = BouncyPlayer(player)
player.handle_input('e')
player.handle_input(' ')

player = BowmanPlayer(player)
player.handle_input('e')
player.handle_input(' ')
