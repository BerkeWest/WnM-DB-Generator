import pandas as pd
import numpy as np
import warnings
import add_dataframe
import sqlite3

def main():
    warnings.filterwarnings("ignore")
    df=pd.read_csv(r'C:\Users\berke\Downloads\WnM Veri Seti\Database Generator\WnM_datatset.txt',sep="/")

    con = sqlite3.connect('WnM_data.db')
    df.to_sql(name="user_data",con=con,if_exists= "replace", index=False)
    con.commit()

    xlWriter = pd.ExcelWriter("WnM_data_excel.xlsx",engine='xlsxwriter')
    workbook  = xlWriter.book

    add_dataframe.addframe(df,xlWriter)
    workbook.close()
    print(df)