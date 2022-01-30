from kivy.app import App
from kivy.clock import Clock
from kivy.factory import Factory

from data.game import PongGame


class PongApp(App):

    def build(self):
        Factory.register('PongBall', module='data.ball.ball')
        Factory.register('PongPaddle', module='data.paddle.paddle')
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
