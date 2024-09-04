# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Juptyer Notebooks
#
# ## What are Notebooks?
#
# Jupyter Notebooks are interactive, web-based tools that allow developers and data scientists to combine code, visualizations, and narrative text in a single document. 
#
# They are ideal for data analysis, experimentation, and educational purposes. The notebook format enables users to write and execute code in cells, view outputs immediately, and create a narrative around their work, making it accessible and understandable for both technical and non-technical audiences. This makes Jupyter Notebooks a powerful platform for collaboration, teaching, and sharing insights.
#
# Useful for:
# - EDA (exploratory data analysis)
# - creating AI model POCs
# - anything where you want visibility of every step of the process or want to build up and adjust a process without needing to rerun the whole flow from the start
#
# Less useful for:
# - creating production ready code
# - working on code that a number of people will want to be editing at the same time

# %% [markdown]
# ## Colab Setup
# If you're running in Colab:
# - open Google colab
# - upload the example notebook
# - set the `in_colab` parameter to True below
# - on the left open the files menu
# - upload the colab-upload.zip archive from the repo
# - now you can run the cell below to unzip that file

# %%
in_colab = False

if in_colab:
    # !unzip -o colab-upload.zip

# %% [markdown]
# ## Playground

# %%
import numpy as np
import pandas as pd

# %%
thefts = pd.read_csv('data/stolen_vehicles.csv')
thefts

# %%
vehicle_cats = pd.read_csv('data/vehicle_categories.csv')
vehicle_cats
