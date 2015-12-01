import unittest        
import sfml as sf
from utility.constants import *

from menu.game_over_menu import *

class gameOverMenuTest(unittest.TestCase):
    
    def setUp(self):
        self.window = sf.RenderWindow(sf.VideoMode(100, 100), "Hack the Planet")
        self.game_state = draw_game_over_menu(self.window)
        
    def tearDown(self):
        self.window = None
        
    def testGameState(self):
        self.assertTrue(MAIN_MENU == self.game_state)
