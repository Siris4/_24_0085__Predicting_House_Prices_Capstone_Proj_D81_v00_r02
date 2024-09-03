import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

pd.options.display.float_format = '{:,.2f}'.format

# Corrected file path with raw string literal
data = pd.read_csv(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\r00_env_START\boston.csv', index_col=0)

data_shape = data.shape
print("The shape of the dataset is:", data_shape)

column_names = data.columns.tolist()
print("The column names are", column_names)

nan_values = data.isnull().sum()
print("NaN values in each column:\n", nan_values)

columns_with_nan = data.isnull().any().sum()
print("Number of columns with NaN values: ", columns_with_nan)

duplicate_rows = data.duplicated().sum()
print("Number of duplicate rows:", duplicate_rows)

average_ptratio = data['PTRATIO'].dropna().mean()
print(f"The average Student to Teacher ratio is {average_ptratio}.")

home_price = (data['PRICE'].dropna().mean() * 1000)
print(f"The average home price was ${home_price}")

if 'RM' in data.columns:
    max_rooms = data['RM'].max()
    print("The maximum number of rooms are:", max_rooms)

    min_rooms = data['RM'].min()
    print("The minimum number of rooms are:", min_rooms)

