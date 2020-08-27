import unittest
from qry import qry


class test2(unittest.TestCase):
    obj = qry()

    def add(self):
        actual_result = self.obj.add_employee("11","Ronaldo","ronal@ronaldo.ronaldo.ronaldo","Male"," 7777777","07/07/07","Ronaldo highway-77","Sales","Absent","Cheque" )
        answer = True
        self.assertTrue(answer, actual_result)
