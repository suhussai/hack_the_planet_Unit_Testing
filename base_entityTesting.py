import unittest        
from entities.base_entity import BaseEntity
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

        self.base_entity = BaseEntity(dude_body, dude_poly, sprite, sf.Vector2(19,44))

    def tearDown(self):
        self.base_entity = None
        
    def testForNone(self):
        self.assertFalse(None, self.base_entity)

    def testPosition(self):
        self.assertFalse(None, self.base_entity.get_position)

    def testFace(self):
        self.assertFalse(None, self.base_entity.face)
        
    def testHealth(self):
        self.base_entity.take_damage(0.2);
        self.assertFalse(self.base_entity._health == self.base_entity._max_health)
        self.assertTrue(self.base_entity._health == 1 - 0.2);
        self.base_entity.take_healing(0.2);
        self.assertTrue(self.base_entity._health == self.base_entity._max_health)
        self.assertTrue(self.base_entity._health == 1);

    def testCan(self):
        # test setting and getting
        # for the following actions
        for action in ["jump", "press"]:            
            self.base_entity.can(action, False)
            self.assertFalse(self.base_entity.can(action))
            
            self.base_entity.can(action, True)
            self.assertTrue(self.base_entity.can(action))
        
    def testUpdateSpritePosition(self):
        self.base_entity.update_sprite_position()
        self.assertTrue(self.base_entity._sprite.position == self.base_entity._body.position)

    def testUpdateSpriteFrame(self):
        topLeft = sf.Vector2(self.base_entity._frame_size.x*self.base_entity._frame,self.base_entity._frame_size.y*self.base_entity._direction)        
        self.base_entity.update_sprite_frame()
        self.assertTrue(self.base_entity._sprite.texture_rectangle == sf.Rectangle(topLeft, self.base_entity._frame_size))

        # change properties
        self.base_entity._direction = LEFT
        self.base_entity._frame = 2

        # update topLeft variable
        topLeft = sf.Vector2(self.base_entity._frame_size.x*self.base_entity._frame,self.base_entity._frame_size.y*self.base_entity._direction)        

        # check to make sure that sprite frame has not been updated
        self.assertFalse(self.base_entity._sprite.texture_rectangle == sf.Rectangle(topLeft, self.base_entity._frame_size))

        # update frame and check 
        # for equality
        self.base_entity.update_sprite_frame()
        self.assertTrue(self.base_entity._sprite.texture_rectangle == sf.Rectangle(topLeft, self.base_entity._frame_size))



if __name__ == '__main__':
    unittest.main()
