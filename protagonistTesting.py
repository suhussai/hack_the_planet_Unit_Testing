import unittest        
from entities.protagonist import Protagonist
import pymunk as pm
import sfml as sf
from utility.constants import *

from utility.constants import *
from utility.menu_banter import *


class baseTesting(unittest.TestCase):
    
    def setUp(self):
        # Animation stuff
        dudeFrame		= 6
        dudeFrameCounter = 0
        dudeFrameSpeed   = 5

        # load the textures for possible heroes
        dudeTextures = []
        characters   = []
        try:
            dudeTextures.append(sf.Texture.from_file("assets/sprites/dude0.png"))
            dudeTextures.append(sf.Texture.from_file("assets/sprites/dude1.png"))
            dudeTextures.append(sf.Texture.from_file("assets/sprites/dude2.png"))
        except IOError:
            print("ERROR")
            exit(1)
    
        for dudeTexture in dudeTextures:
            characters.append(sf.Sprite(dudeTexture))
    
        for i in range(len(characters)):
            characters[i].ratio	= sf.Vector2(4,4)
            characters[i].origin   = texture_size/2
            characters[i].position = (game_size.x/(len(characters) + 1) * (i + 1), game_size.y/2)
    
        topLeft = sf.Vector2(114,0)
        for character in characters:
            character.texture_rectangle = sf.Rectangle(topLeft, texture_size)

        level = 1
        space = pm.Space()
        sprite = characters[1]        

        # create hero's physical body
        dude_body = pm.Body(50, pm.inf) # Has a weight, but cannot rotate

        # create hero's boundaries
        dude_poly = pm.Poly.create_box(dude_body, person_size)
        dude_poly.friction = 1
        dude_poly.collision_type = 3

        jump_sensor = pm.Poly.create_box(dude_body, size=(50,2), offset=(0,65))
        jump_sensor.sensor = True
        jump_sensor.collision_type = 2

        space.add(dude_body, dude_poly, jump_sensor)

        self.hero = Protagonist(dude_body, dude_poly, sprite, sf.Vector2(19,44), "")

    def tearDown(self):
        self.hero = None
        
    def testForNone(self):
        self.assertFalse(None, self.hero)

    def testJump(self):
        self.hero.jump(800)
        self.assertTrue(self.hero._body.velocity.y == -800)

    def testForDoubleJump(self):
        self.hero.jump(800)
        self.assertFalse(self.hero.can("jump")) # check for  double jump
        self.assertTrue(self.hero._body.velocity.y == -800)


    def testWalkRight(self):
        # # Animation stuff:
        # RIGHT = 0
        # LEFT  = 1

        # start walking left first
        # to make sure that
        # walking right actually works
        self.hero.walk(800, LEFT)

        frame_countBefore = self.hero._frame_count

        # test walking right
        self.hero.walk(800, RIGHT)
        self.assertTrue(self.hero._direction == RIGHT)
        self.assertTrue(self.hero._body.velocity.x == 800)
        self.assertTrue(self.hero._frame_count == frame_countBefore + 1)

    def testWalkLeft(self):
        # # Animation stuff:
        # RIGHT = 0
        # LEFT  = 1

        # start walking right first
        # to make sure that
        # walking left actually works
        self.hero.walk(800, RIGHT)

        frame_countBefore = self.hero._frame_count

        # test walking left
        self.hero.walk(800, LEFT)
        self.assertTrue(self.hero._direction == LEFT)
        self.assertTrue(self.hero._body.velocity.x == -800)
        self.assertTrue(self.hero._frame_count == frame_countBefore + 1)

    def testStop(self):
        self.hero.stop()
        self.assertTrue(self.hero._frame == 6)
        self.assertTrue(self.hero._frame_count == 0)

    def testHeroReset(self):
        self.hero.reset_all_the_things()
        self.assertTrue(self.hero._frame == 6)
        self.assertTrue(self.hero._health == 1)
        self.assertTrue(self.hero._direction == RIGHT)
        self.assertTrue(self.hero._body.position == (100,500))
        self.assertTrue(self.hero._body.velocity == (0,0))

if __name__ == '__main__':
    unittest.main()
