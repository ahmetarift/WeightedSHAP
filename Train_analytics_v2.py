# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: 'Python 3.9.12 (''base'': conda)'
#     language: python
#     name: python3
# ---

# %%
import sys, os
import numpy as np
import pickle 
np.random.seed(2022)
sys.path.append('../')
import weightedSHAP
