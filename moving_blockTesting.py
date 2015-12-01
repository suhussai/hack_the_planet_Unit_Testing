import unittest        
from entities.moving_block import MovingBlock
import pymunk as pm
import sfml as sf
from utility.constants import *

from utility.constants import *
from utility.menu_banter import *


class baseTesting(unittest.TestCase):
    
    def setUp(self):
        lineString = "move 200		400		100		50		0	0	0	0.0		400		300		1"
        space = pm.Space()
        line = lineString.split()
        dynamic_body = pm.Body(pm.inf, pm.inf)
        dynamic_body.position = int(line[1]), int(line[2])
        
        my_shape = pm.Poly.create_box(dynamic_body, (int(line[3]),int(line[4])))
        my_shape.friction = float(line[8])
        my_shape.collision_type = 2
        space.add(my_shape)
        
        my_graphic = sf.RectangleShape()
        my_graphic.size = (int(line[3]), int(line[4]))
        my_graphic.origin = my_graphic.size / 2
        my_graphic.fill_color = sf.Color(int(line[5]),int(line[6]),int(line[7]))
        my_graphic.position = (int(line[1]), int(line[2]))
        
        self.block = MovingBlock(dynamic_body, my_shape, my_graphic,
                pm.Vec2d(int(line[9]), int(line[10])), float(line[11]))

    def tearDown(self):
        self.block = None
        
    def testForNone(self):
        self.assertFalse(None, self.block)

    def testMovingBlockTest(self):
        # test to see if block actually moves
        initial_x, initial_y = self.block.body.position
        self.block.step(20)
        self.assertFalse(self.block.body.position == (initial_x, initial_y))


if __name__ == '__main__':
    unittest.main()
