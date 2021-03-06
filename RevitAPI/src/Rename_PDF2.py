#===============================================================================
# Set up
#===============================================================================
# Standard:
from config.config import *
import re
import logging.config
import unittest

import os

from collections import defaultdict
import sys

import csv
#===============================================================================
# Other modules
#===============================================================================

#===============================================================================
# Logging
#===============================================================================
print(ABSOLUTE_LOGGING_PATH)
logging.config.fileConfig(ABSOLUTE_LOGGING_PATH)
myLogger = logging.getLogger()
myLogger.setLevel("DEBUG")

#===============================================================================
# Main script
#===============================================================================
logging.info("Python version : {}".format(sys.version))

def rename():
    logging.debug("Start")
    
    folder = r"C:\Users\jon\Desktop\PDF Print"
    os.chdir(folder)
    
    for i,filename in enumerate(os.listdir(folder)):
        #if filename.startswith("cheese_"):
        #    os.rename(filename, filename[7:])
        #new_name = filename.replace("C_PDF IKEA_DATA_DATA - Sheet - ","")
        #new_name = filename.replace("C_Users_jon_Documents_DATA - Sheet - ","")
        #new_name = filename.replace("C_Users_jon_Documents_DATA - Sheet - ","")
        new_name = filename.replace("C_Users_jon_Desktop_PDF Print_161014_IKEA_MEP_LOCAL - Sheet - ","")
        
        new_name = new_name.replace("--","")

        print(filename)
        print(new_name)
        print("***")
        
        #full_path
        if 1:
            try:
                os.rename(filename, new_name)
            except FileExistsError:
                print("File exists")
                pass
        
        #print(i,filename)
        
    logging.debug("Done")


if __name__ == '__main__':
    rename()
    
