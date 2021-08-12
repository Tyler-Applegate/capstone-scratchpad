# Initial Prep for Capstone

import pandas as pd
import requests
import numpy as np
from datetime import timedelta, datetime

def convert_lower(df):
    '''
    This function takes in a pandas dataframe, converts all columns to lowercase, and returns the updated pandas DataFrame.
    '''
    df.columns = df.columns.str.lower()
    return df

def to_datetime(df, col):
    '''
    This function takes in a pandas DataFrame, and a target column, converts the target variable to datetime, and returns the DataFrame.
    '''
    df[col] = pd.to_datetime(df[col]).sort_values()
    return df

def index_reset(df, col):
    '''
    This function takes in a pandas DataFrame, and a target column, and sets the target variable as the index, and returns a pandas DataFrame.
    '''
    df = df.set_index(col).sort_index()
    return df

def gender_prep(df, col):
    '''
    This functions takes in a pandas DataFrame, and a target column of gender, and creates a new column, encodes the column as 0:Male, 1:Female, 2:Other, and returns the updated pandas DataFrame.
    '''
    # make an initial copy
    df['gender_encoded'] = df[col]
    
    # strip whitespace
    df['gender_encoded'] = df['gender_encoded'].str.strip()
    
    # convert all to lowercase
    df['gender_encoded'] = df['gender_encoded'].str.lower()
    
    
    
    
    
