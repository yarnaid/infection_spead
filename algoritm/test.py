import unittest 
import Codethuattoan

class TestCode(unittest.TestCase):
    def test_ReadConfig(self):
       
        self.assertEqual(Codethuattoan.ReadConfig('config.ini'), [0.001 ,0.1 ,1.0, 0.001 ,1000.0 ,1.0, 0.0 ,100])
    def test_rungeKutta(self):
        self.assertEqual(Codethuattoan.rungeKutta(1000 , 1 , 0) , [999.9989996253158, 1.0009003371740595, 0.00010003751011400939] )
    

if __name__ == '__main__':
    unittest.main()
    
        


