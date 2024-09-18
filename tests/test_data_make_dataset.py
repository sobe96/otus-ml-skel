import pytest
import os
import pandas as pd

from titanic.data.make_dataset import *

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR_PATH = os.path.dirname(SCRIPT_PATH)
RAW_DATA_FOLDER = os.path.join(SCRIPT_DIR_PATH, "..", "data", "raw")
TRAIN_PATH = os.path.join(RAW_DATA_FOLDER, "train.csv")

@pytest.mark.parametrize('datapath', [None, ])
def test_none_path(datapath):
    df1 = load_titanic(datapath)
    df2 = pd.read_csv(TRAIN_PATH, index_col="PassengerId")
    assert df1.equals(df2)