import unittest        
import sfml as sf
from utility.constants import *

from utility.menu_banter import *

class banterTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNone(self):
        banter = make_menu_banter("testing", (2,2))
        self.assertFalse(None, banter)
        
    def testString(self):
        banter = make_menu_banter("testing2", (3,3))
        self.assertTrue(banter.string == "testing2")

    def testPosition(self):
        banter = make_menu_banter("testing2", (3,3))
        self.assertTrue(banter.position == (3,3))

    
