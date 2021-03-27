import pandas as pd
from pandas.util.testing import assert_frame_equal

from Data.data_set import DataSet


class TestDataset:
    def test_data_set(self):
        dataset = DataSet('test_resources/test_1')
        expected = pd.read_csv('test_resources/expected.csv')
        assert_frame_equal(dataset.get_data(interval=2), expected)

        print(dataset.get_training_split(2,3))