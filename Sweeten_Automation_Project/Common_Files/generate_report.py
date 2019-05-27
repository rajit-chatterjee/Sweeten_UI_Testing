'''
This file will generate the html report of the test cases. 
As of now we are running this file by importing the test case class.
'''

import unittest
import HtmlTestRunner as ht
import os
import Scripts.test_signup as ts
import Scripts.test_cancel_account as tc
import Scripts.test_add_project as ta
class MyTestSuite(unittest.TestCase):
  
    def test_Issue(self):
        direct = os.getcwd()
        sweeten_test = unittest.TestSuite()
        sweeten_test.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(ts.test_signup),
                             unittest.defaultTestLoader.loadTestsFromTestCase(tc.test_cancel_account),
                             unittest.defaultTestLoader.loadTestsFromTestCase(ta.test_add_project)])
        outfile = open(direct + "\SweetenTest.html", "w")
  
        runner1 = ht.HTMLTestRunner(
            stream=outfile,
            report_title='Test Report',
            descriptions='Test your script'
        )
  
        runner1.run(sweeten_test)

if __name__ == '__main__':
    unittest.main()