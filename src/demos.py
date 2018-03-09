import pandas as pd
import numpy as np 
import os

raw_data_path = os.path.join('data','raw')
train_file_path = os.path.join(raw_data_path,'train.csv')
test_file_path = os.path.join(raw_data_path,'test.csv')

train_df = pd.read_csv(train_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_file_path, index_col='PassengerId')

#type(train_df)
#train_df.info()
#test_df.info()

test_df['Survived'] = -888
df = pd.concat((train_df, test_df),axis=0)
#df.info()

print(df.head())
print(df.tail())
