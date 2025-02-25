# # Implementation & testing of the ArrayStack class

from QueueClass import ArrayQueue
from TEST_CODE import *
import os

'''
Testing details can be found in TEST_CODE.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():
    
    testQ = ArrayQueue()

    # TEST 1 - Test privacy
    # BEFORE TESTING: implement __init__, __is_empty(), __resize()
                                #Methods can just contain pass
    TEST_privacy(testQ)


    # TEST 2 - Test queue creation
    # BEFORE TESTING: implement __len__, __str__, .__first()
    TEST_new_q(testQ)
    

    # TEST 3 - Test enqueue
    # BEFORE TESTING: implement .enqueue(), .__resize()
    TEST_enqueue(testQ)


    # TEST 4 - Test dequeue
    # BEFORE TESTING: implement .dequeue()
    TEST_dequeue(testQ)


    # TEST 5 - Test Enqueue Again
    # BEFORE TESTING: implement .top()
    TEST_enqueue2(testQ)


    # TEST 6 - Test Resize
    # BEFORE TESTING: implement .__resize()
    TEST_resize(testQ)


    # TEST 7 - Test docstrings
    # BEFORE TESTING: implement all methods & docstrings
    TEST_docs(testQ)




if __name__ == "__main__":
    os.system("clear")
    main()