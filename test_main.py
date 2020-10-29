import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "you have plotted the wrong number of coordinates on your graph" )
        for i in range( len(this_x) ) :
             self.assertTrue( np.abs(i + 2 - this_x[i])<1e-7, "the x-coordinates for your graph are not correct" )
  
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
 
        samples = 100*[0]
        for i in range(100) : 
            ssum, ssum2 = 0, 0 
            for j in range(200) :
                myvar = np.random.uniform(0,1)
                ssum, ssum2 = ssum + myvar, ssum2 + myvar*myvar
            mean = ssum / 200 
            samples[i] = (200/199)*( ssum2 / 200 - mean*mean ) 
    
        samples.sort()
        self.assertTrue( this_y[-1]>samples[1] and this_y[-1]<samples[98], "the y-coordinates in your graph appear to be incorrect" )
