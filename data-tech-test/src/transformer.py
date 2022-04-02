from posixpath import split
from typing import (
    List,
    Tuple,
)

import numpy
import pandas as pd
from pandas.testing import assert_frame_equal
from datetime import datetime
class Transformer:

    def __init__(self):
        self

    def read_orders(self) -> pd.DataFrame:
        orders = pd.read_csv('orders.csv', header=0)
        return orders

    def enrich_orders(self, orders: pd.DataFrame, col_name: str, value: List[str]) -> pd.DataFrame:
        orders[col_name]=value
        return orders

    def split_customers(self, orders: pd.DataFrame, threshold: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        low_df=orders.loc[orders['amount']<threshold]
        high_df=orders.loc[orders['amount']>threshold]

        return (low_df,high_df)

    def test__split_customers(self, df1: pd.DataFrame,df2: pd.DataFrame):
        assert_frame_equal(df1,df2)

if __name__ == '__main__':
    transformer = Transformer()
    data = transformer.read_orders()
   
    countries = ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']
    data = transformer.enrich_orders(data, 'Country', countries)
    avarage= data["amount"].mean()
    
    print("\n")
    print("What was the average order amount across all customers? ",avarage,"\n")
    print("Which customer placed the highest order amount? ")
    print(data.query("amount==amount.max()"),"\n")
    print("Which customer placed the lowest order amount? ")
    print(data.query("amount==amount.min()"),"\n")
    print("Which customer placed the earliest order? ")
    print(data.query("date==date.min()"),"\n")


    data['date']=data['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    data['year/month']=data['date'].apply(lambda x:  "%d/%d" % ( x.year,x.month))
    print("Month with most orders: ",data["year/month"].value_counts().index[0])
    print("\n")
    threshold = avarage # Change this value
    low_spending_customers, high_spending_customers = transformer.split_customers(data, threshold)
    transformer.test__split_customers(low_spending_customers,high_spending_customers)


