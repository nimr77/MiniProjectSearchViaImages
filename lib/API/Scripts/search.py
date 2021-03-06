# -*- coding: utf-8 -*-
# import the necessary packages
from utils.colordescriptor import ColorDescriptor
from utils.glcmdescriptor import glcmDescriptor
from utils.shapedescriptor import shapeDescriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--index", required = True,
# 	help = "Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required = True,
# 	help = "Path to the query image")
# ap.add_argument("-r", "--result-path", required = True,
# 	help = "Path to the result path")
# args = vars(ap.parse_args())
# initialize the image descriptor


def Search(imagePath):
    """
    docstring
    """
    cd = ColorDescriptor((8, 12, 3))
    gd = glcmDescriptor()
    sh = shapeDescriptor()

    # load the query image and describe it, the imgs search
    query = cv2.imread(imagePath)
    #features = cd.describe()

    features_cd = cd.describe(query)
    features_gd = gd.describe(query)
    features_sh = sh.describe(query)

    features = []
    for i in features_cd:
        features.append(i)

    for j in features_gd:
        features.append(j)

    for t in features_sh:
        features.append(t)

    # perform the search
    # here we will send the images , as input from the API
    searcher = Searcher(imagePath)
    results = searcher.search(features)
    # loop over the results
    return results
