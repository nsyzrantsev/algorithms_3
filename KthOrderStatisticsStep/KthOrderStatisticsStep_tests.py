from KthOrderStatisticsStep import KthOrderStatisticsStep
from unittest import TestCase
import random

class KthOrderStatisticsStepTest(TestCase):

    def test_k(self):
        arr = [3,5,2,4,1]
        self.assertEqual([0,4], KthOrderStatisticsStep(arr, 0, len(arr)-1, 4))
