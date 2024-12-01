import os
import argparse
import pandas as pd

# Arguments
parser = argparse.ArgumentParser(description='Inputs for sales calculation data')
parser.add_argument('filename' , type=str, help='Input Filename')
args = parser.parse_args()

# Reading csv file from DataFolder
curr_path = os.getcwd()
filePath = f'{curr_path}\\DataFolder\\{args.filename}'
df = pd.read_csv(filePath)

# Transformations from string to actual dtypes
df['Date'] = pd.to_datetime(df['Date'])
df['Sales'] = pd.to_numeric(df['Sales'] , errors='coerce')
df['month'] = df['Date'].dt.month

#print(df)
df_monthly_sales = df.groupby('month')['Sales'].agg(['sum' , 'count'])

df_monthly_sales['average'] = round(df_monthly_sales['sum'] / df_monthly_sales['count'],2)

print(df_monthly_sales[['sum','average']])