#coding=utf-8

import unittest
from com.dm.auto.testcase.myPageTestcase import MyPageTestcase
from com.dm.auto.testcase.HTMLTestRunner import HTMLTestRunner
import os

def runAll():

    result_path = os.path.abspath(os.path.join(os.path.curdir,"results","Android测试报告.html"))
    print(result_path)
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyPageTestcase))
    with open(result_path,'wb') as f:
        runner = HTMLTestRunner(stream=f, title='Android测试报告', description='测试报告 详细信息')
        runner.run(suite)

if __name__ == "__main__":
    runAll()