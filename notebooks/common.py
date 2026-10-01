# common.py - shared setup for all notebooks
import duckdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Display settings
pd.set_option('display.width', 200, 'display.max_columns', 60, 'display.max_colwidth', 45)
pd.options.display.float_format = '{:,.2f}'.format

# Project paths
RAW   = Path('../data/raw/DataCoSupplyChainDataset.csv')
CLEAN = Path('../data/clean')
DB    = '../data/dataco.duckdb'
FIG   = '../reports/figures/'

def connect(read_only=True):
    """Open the project database. Use read_only=False only in notebook 02, which builds it."""
    return duckdb.connect(DB, read_only=read_only)