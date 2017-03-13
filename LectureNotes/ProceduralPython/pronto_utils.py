# Python 2:
# from urllib import urlretrieve
# Python 3:
from urllib.request import urlretrieve
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib as mpl


DATA_URL = "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"


def download_if_needed(url, filename, force_download=False):
    """
    Download url to filename if filename does not exist
    """
    if force_download or not os.path.exists(filename):
        print("Downloading file from {0} to {1}".format(url, filename))
        urlretrieve(url, filename)
    else:
        print("File {0} already exists; not downloading".format(filename))


def load_trip_data(filename='open_data_year_one.zip'):
    """Load trip data from the zipfile; return as DataFrame"""
    download_if_needed(DATA_URL, filename)
    zf = zipfile.ZipFile(filename)
    return pd.read_csv(zf.open('2015_trip_data.csv'))


def plot_totals_by_birthyear():
    df = load_trip_data()
    totals_by_birthyear = df.birthyear.value_counts().sort_index()
    return totals_by_birthyear.plot(linestyle='steps')


# Unit tests below here

def test_trip_data():
    df = load_trip_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (142846, 12)


def test_plot_totals_by_birthyear():
    mpl.use('Agg')
    ax = plot_totals_by_birthyear()

    # Some tests of the output that dig into the
    # matplotlib internals
    assert len(ax.lines) == 1

    line = ax.lines[0]
    x, y = line.get_data()
    assert np.all((x > 1935) & (x < 2000))
    assert y.mean() == 1456
