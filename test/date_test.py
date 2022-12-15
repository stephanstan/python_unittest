#from cuboid_volume import *

import unittest
from datetime import date
from datetime import datetime
from datetime import time



class MyTestCase(unittest.TestCase):
    def test_today(self):
#        self.assertAlmostEqual(cuboid_volume(2),8)
         today = date.today()
         print("Today's date is ", today)

    def test_today_compontents(self):
         today = date.today()
         print("Today's date components: ", today.year, today.month, today.day)

    def test_today_weekdaynumber(self):
         today = date.today()
         print("Today's index value: ", today.weekday())

    def test_today_time_just_time(self):
         t = datetime.time(datetime.now() )
         print("Current time is:", t)

    def test_today_day_of_week(self):
        # Days start at 0 for monday
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        print("Today is day number %d" % wd)
        print("which is a " + days[wd])



if __name__ == '__main__':
    unittest.main()
