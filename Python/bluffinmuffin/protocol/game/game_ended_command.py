from bluffinmuffin.protocol.interfaces import AbstractGameCommand


class GameEndedCommand(AbstractGameCommand):

    def __init__(self, obj):
        super().__init__(obj)
