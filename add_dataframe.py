import pandas as pd
def addframe(df,xlWriter):
    df.to_excel(
        excel_writer=xlWriter,
        index=False,
        header=True)