from multiprocessing import Queue
import unittest

from deck import deck
from hand import hand
from main import main
from simulator import multiprocess_simulator


class TestSinglePlayer(unittest.TestCase):

    # deck
    def test_deck(self):
        new_deck = deck()
        self.assertEqual(len(new_deck), 52)
    
    def test_deck_2(self):
        new_deck = deck(2)
        self.assertEqual(len(new_deck), 104)
    
    def test_deck_return_type(self):
        new_deck = deck(2)
        self.assertIsInstance(new_deck, list)
    
    def test_deck_0(self):
        with self.assertRaises(ValueError):
            deck(0)

    # hand 
    def test_hand_value(self):
        hand_return_value =  hand(deck())
        self.assertIn(hand_return_value, [1, 0, 1, -1])
    
    def test_hand_value_type(self):
        hand_return_value =  hand(deck())
        self.assertIsInstance(hand_return_value, int)
    
    # main
    def test_simulator_return_value_type(self):
        value = main(10, 1)
        self.assertIsInstance(value, str)
    
    # simulator
    def test_simulator_result(self):
        queue = Queue()
        multiprocess_simulator(1, 1, queue)
        self.assertEqual(len(queue.get()), 3)
    
    def test_simulator_result_type(self):
        queue = Queue()
        multiprocess_simulator(1, 1, queue)
        self.assertIsInstance(queue.get(), list)


if __name__ == "__main__":
    unittest.main()