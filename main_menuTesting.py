import unittest        
import sfml as sf
from utility.constants import *

from menu.main_menu import *

class mainMenuTest(unittest.TestCase):
    
    def setUp(self):
        self.window = sf.RenderWindow(sf.VideoMode(100, 100), "Hack the Planet")
        self.window.close()
        self.game_state = draw_main_menu(self.window)
        
    def tearDown(self):
        self.window = None
        
    def testGameState(self):
        self.assertFalse(None,self.window)
