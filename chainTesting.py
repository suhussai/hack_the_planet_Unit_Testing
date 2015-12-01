import unittest        
import sfml as sf
from utility.constants import *

from chain import Chain

class chainTest(unittest.TestCase):    
    def setUp(self):
        self.space = pm.Space()

    def tearDown(self):
        self.space = None
        pass

    def testNone(self):
        chain1 = Chain(self.space, 20, pm.Vec2d(250, 0))
        self.assertFalse(None, chain1)
        self.assertFalse(None, chain1.get_end())
        self.assertFalse(None, chain1.get())
        
