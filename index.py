from player import Player
from dice import Dice
from properties import Properties
from db import Database

# Objects
_player = Player()
_dice = Dice()
_properties = Properties()
_db = Database()

def playerRoll():
    _player.setSpace(_dice.roll())

# Checking where the player is on the board
def checkSpace():
    landed = _properties.properties[_player.space][0]
    _db.incrementLanded(landed)

def checkGoToJail():
    if _properties.properties[_player.space][1] is 30:
        # TODO: SKIP GAME
        print('')

if __name__ == '__main__':
    for game in range(100):
        for rounds in range(40):
            playerRoll()
            checkSpace()
        _player.space = 0
    _db.createGraph()
    _db.purgeDocuments()
    