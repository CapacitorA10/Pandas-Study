import numpy as np
import pandas as pd
mydata = pd.read_csv("pandas_test.csv")

## prod_code별로 pivot

pivoted = pd.pivot_table(mydata,index=['fact_num','WW'],columns='prod_code' ,values=['Resistance','Watt','Weight'])
rst_idx = pivoted.reset_index()
pd.DataFrame.to_csv(pivoted,'pandas실습2.csv')
