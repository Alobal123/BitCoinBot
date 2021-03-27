import pandas as pd
from pandas.util.testing import assert_frame_equal

from Data.data_set import DataSet


class TestDataset:
    def test_data_set(self):
        dataset = DataSet('test_resources/test_1')
        expected = pd.read_csv('test_resources/expected.csv')
        print(dataset.get_data(range=2))
        print(expected)
        assert_frame_equal(dataset.get_data(range=2), expected)
