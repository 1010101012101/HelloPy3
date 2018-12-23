import statsmodels.api as sm


def data_sunspots():
    return sm.datasets.sunspots.load_pandas()