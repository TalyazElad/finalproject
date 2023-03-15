import argparse
import os
import sys
import pdb

import cv2
from joblib import load

from brisque import brisque
from niqe import niqe
from pique import pique

def runner(path):
    im = cv2.imread(path)
    if im is None:
        print("Failed to read image file")
        raise BrokenPipeError

    else:
        score = niqe(im)
        return("{}".format(score))


# runner("C:\\Users\\eladtal\\PycharmProjects\\streamlit\\uploaded\\uploaded_frame419.jpg")

def pique_runner(path):
    im = cv2.imread(path)
    if im is None:
        print("Failed to read image file")
        raise BrokenPipeError

    else:
        score, _, _, _ = pique(im)
        return("{}".format(score))