import logging
import os
import sys

class logGen():
    @staticmethod
    def logGeneration():
       logging.basicConfig(filename = os.path.dirname(os.path.dirname(__file__))+"\\logs\\auto.log",
                        format = '%(asctime)s : %(levelname)s : %(message)s', force=True)
       logger = logging.getLogger()
       logger.setLevel(logging.INFO)
       return logger

#os.path.dirname(os.path.dirname(__file__))+"\\reports\\report1.html"

