import os
import logging
import columns as columns
import pandas as pd
logging.basicConfig(filename='detail.log', level= logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:%(filename)s:%(pathname)s')
try:
    if os.path.getsize('C:/Users/FENIL/Desktop/test.txt') == 0:
        raise Exception('No Content in file')
    df = pd.read_csv('C:/Users/FENIL/Desktop/test.txt', header= None, index_col= False)
    df = df.sort_values(df.columns[0])
    logging.debug("Sorting Content of file")
    df.to_csv('C:/Users/FENIL/Desktop/abc.txt', header= None , index= False)
    logging.debug("New file created and data printed")
except OSError:
        logging.debug("There is no file named",)

