""" IMPORTING DIFFERENTIATE & ADDING A DIRECTORY TO SEARCH PATH """
import os
newdirectory = os.path.abspath("..")
import sys
if (str(newdirectory) in sys.path)==False:
    sys.path += [str(newdirectory)]
import symbolic.differentiate as dif

def test_import():
    assert 0