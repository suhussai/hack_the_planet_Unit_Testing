import unittest        
import sfml as sf
from utility.constants import *

from particles import Particles

class particlesTest(unittest.TestCase):    
    def setUp(self):
        self.particles1 = Particles(20,1, (200,2))

    def tearDown(self):
        self.Particles1 = None

    def testNone(self):
        self.assertFalse(None, self.particles1)
        
    def testEmitter(self):
        emitter = (20,30)
        self.assertFalse(emitter == self.particles1._emitter)

        self.particles1.set_emitter(emitter)
        self.assertTrue(emitter == self.particles1._emitter)
        
    def testUpdate(self):
        pass

    def testResetParticle(self):
        pass
        
    def testGet(self):
        self.assertFalse(None, self.particles1.get())
        
        
        

