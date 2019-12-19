import pandas as pd
from sklearn.model_selection import train_test_split

class PrepareData:

    def __init__(self):
        self._data = pd.read_csv('Data/DECISION_TREE_TRAIN_DATA_3.csv',index_col='CUSTOMER_ID')
        