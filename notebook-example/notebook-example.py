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
# # Jupyter Notebook - Annotated Example
# An example of what a notebook might look like if you're working in a team and might need to hand this over to someone else.

# %% [markdown]
# ## Purpose of this notebook
# Exploratory data analysis (EDA). This involves:
# - loading up some data (stolen vehicles in NZ over a 6 month period)
# - investigating the data
# - visualising the data
#
# Included is some examples of some magic methods you can use in Jupyter.

# %% [markdown]
# ## Notes

# %% [markdown]
# **Data Sources**
# - Stolen Vehicle Counts https://www.police.govt.nz/can-you-help-us/stolen-vehicles
#
# **Notes on the data**
# - some vehicle makes and models are missing or have been misclassified. For the purposes of this demo this has not been attempted to be rectified
# - the vehicle thefts data only spans a 6 month timeframe, so isn't a huge dataset to draw too many conclusions from
#
# **Next Steps**
# - define rules for handling erroneous or missing data
# - get car counts for different models currently in NZ, to compare the theft rates against availability rates
# - get population counts and area sizes to compare rates of theft with population density

# %% [markdown]
# # Setup

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# useful for local files, if they are likely to be changing
# %load_ext autoreload
# %autoreload 2

from util.datamorph_example import generate_datamorph_example

# %% [markdown]
# If you're running in Colab:
# - open Google colab
# - upload the example notebook
# - set the `in_colab` parameter to True below
# - on the left open the files menu
# - upload the colab-upload.zip archive from the repo
# - now you can run the cell below to unzip that file

# %%
in_colab = False

# %%
if in_colab:
    # !unzip -o colab-upload.zip

# %% [markdown]
# # Data Load

# %% [markdown]
# ## Stolen Vehicles

# %%
thefts = pd.read_csv('data/stolen_vehicles.csv')
thefts

# %%
thefts.dtypes

# %%
thefts.describe()

# %%
thefts.describe(include='object')


# %%
def add_date_cols(df: pd.DataFrame) -> pd.DataFrame:
    df['date_stolen'] = pd.to_datetime(df['date_stolen'], format="%d/%m/%Y")
    df['month_stolen'] = df['date_stolen'].dt.month
    df['dow_stolen'] = df['date_stolen'].dt.strftime('%a')
    df['ndow_stolen'] = df['date_stolen'].dt.strftime('%w')
    df['dom_stolen'] = df['date_stolen'].dt.strftime('%-d')
    df['woy_stolen'] = df['date_stolen'].dt.strftime('%U')
    df['is_weekend'] = df['dow_stolen'].isin(['Sat', 'Sun'])
    return df

thefts = add_date_cols(df=thefts)
thefts

# %% [markdown]
# **Instruction**: go back and run the dtypes cell above

# %%
thefts['month_location_total'] = thefts.groupby(['location', 'month_stolen'])['id'].transform('count')
thefts.rename(columns={'location': 'location_stolen'}, inplace=True)
thefts

# %% [markdown]
# **Instruction**: run cell above twice

# %% [markdown]
# ## Add on Vehicle Categories

# %%
vehicle_cats = pd.read_csv('data/vehicle_categories.csv')
vehicle_cats

# %%
data = thefts.merge(vehicle_cats, on="type", how="left")
data

# %% [markdown]
# # Data Investigation
# We need to:
# - get a feel for the data
# - understand any issues that we see in the data that might impact any analysis or modelling that we want to do

# %%
# Check how successful the data merges were
data[pd.isnull(data['category'])]

# %%
data = data[~pd.isnull(data['make'])]
data = data[~pd.isnull(data['type'])]

# %%
# if you want to do some further investigation, check out things like:
# - the different types of Honda CIVIC in the dataset
# - what vehicles have been logged with the make of "Motorcycle" or "Moped"
# - what type of vehicles are those with the type "Mobile Machine"

data[data['year'] == 0]

# %% [markdown]
# # Data Visualisation

# %% [markdown]
# ## Why is this important?
# Lets look at the interesting Data Morph project by Stefanie Molin.
#
# https://github.com/stefmolin/data-morph
#
# (This project is inspired by the Datasaurus Dozen, and based on the work completed in Data Morph (DOI: 10.5281/zenodo.7834197) and Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing by Justin Matejka and George Fitzmaurice (ACM CHI 2017)).

# %%
if in_colab:
    # %pip install data-morph-ai

# %% [markdown]
# **The Datasaurus Dozen**
#
# What do all af these datasets have in common?
#
# ![Datasaurus](./data_morph/examples/datasaurus-dozen.png)
#
# ![Datasaurus](https://drive.google.com/uc?export=view&id=1MPHA5qkaZZ4uYNq5FMu5YsuyzqHcpaeN)
#
# Credit to (https://juliasilge.com/blog/datasaurus-multiclass/) for this image

# %%
# Run this to generate the gif below that transforms the panda to the star
# It does take a while but shows you a progress bar

#generate_datamorph_example()

# %% [markdown]
# **Dataset One**
#
# ![Panda](./data_morph/examples/panda-to-star-image-start.png)
#
# ![Panda](https://drive.google.com/uc?export=view&id=1ilFTXUl8HKLfQ3I5WlH5bVRdHyINK3zi)

# %% [markdown]
# **Dataset Two**
#
# ![Star](./data_morph/examples/panda-to-star-image-end.png)
#
# ![Star](https://drive.google.com/uc?export=view&id=1KCKxJKFNnu90Rstv-lteSqVTgvL1_AF3)

# %% [markdown]
# **Morphing**
#
# ![Panda to Star](./data_morph/examples/panda_to_star-example.gif)
#
# ![Panda to Star](https://drive.google.com/uc?export=view&id=1N7bpmwX5iAiP5chMVFVOIeBVXSzj-0dG)

# %%
# %pinfo generate_datamorph_example

# %%
# generate_datamorph_example??

# %% [markdown]
# ## Back to Data Visualisation

# %%
fig, axs = plt.subplots(figsize=(10,5), nrows=1, ncols=2)
plt.subplots_adjust(wspace=0.5)

data.groupby('type').size().sort_values().plot(kind='barh', ax=axs[0])
data.groupby('category').size().sort_values().plot(kind='barh', ax=axs[1])
plt.show()

# %%
sns.set_style("whitegrid")
chart = sns.countplot(data=data, x="dow_stolen", hue="is_weekend", legend=False, order=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], palette="Set2")
chart.set(ylabel="Vehicles Stolen", xlabel="Day of the Week")
plt.show()

# %%
subset = data.copy()
#subset = data[data['year'] > 0]
chart = sns.boxplot(data=subset, x="category", y="year", hue="category")
plt.xticks(rotation=30)
plt.show()

# %% [markdown]
# # Other Useful Magic Methods

# %%
# %%time

print('hello')
for i in range(1000): np.random.random_sample()
time.sleep(5)
print('complete')

# %%
print('hello')
# %time for i in range(1000): np.random.random_sample()
time.sleep(5)
print('complete')

# %%
# %whos

# %%
# %history -n

# %%
# %recall 27-28

# %%
str(datetime.now())
