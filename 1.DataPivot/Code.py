import numpy as np
import pandas as pd
mydata = pd.read_csv("pandas_test.csv")

## prod_code별로 pivot
#pivoted = pd.pivot_table(mydata,index='fact_num', columns='WW' ,values=['Resistance','Watt','Weight'], aggfunc='mean')
pivoted = mydata.pivot_table(index='Factory', columns='WW' ,values=mydata.columns[2:], aggfunc=np.min)
rst_idx = pivoted.reset_index()
pd.DataFrame.to_csv(pivoted,'pandas실습2.csv')
