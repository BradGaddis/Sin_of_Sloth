# Screen setup

from drawable_object import Drawable_Object


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
TILE_SIZE = 32
FPS = 60


TEST_MAP = [
    ["X"," ","X"," "," "," "," "," "],
    ["X"," "," "," "," "," "," "," "],
    ["X","P"," "," "," "," "," "," "],
    ["X","X"," ","X"," ","X","X","X"],
    ["X","X"," ","X"," ","X","X","X"]
]

def Destroy(self, object):
    if issubclass(object, Drawable_Object):
        object.kill()
        print(f"{object} killed")
    del self.object
    del self
