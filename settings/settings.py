# Screen setup

from support.drawable_object import Drawable_Object


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TILE_SIZE = 32
FPS = 60
UPPER_BOUND = SCREEN_HEIGHT / 4
LOWER_BOUND = SCREEN_HEIGHT - UPPER_BOUND
LEFT_BOUND = SCREEN_WIDTH / 4
RIGHT_BOUND = SCREEN_WIDTH - LEFT_BOUND

TEST_MAP = [
    ["X"," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "],
    ["X","P"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "],
    ["X","X"," ","X"," ","X","X"," "," ","X","X","X"," "," "," "," "," "," "," "," "," "," "," "],
    ["X","X"," ","X"," ","X","X","X","X","X","X","X"," ","X"," ","X","X","X","X","X","X","X","X"]
]

def Destroy(self, object):
    del object
    del self.object
    del self
