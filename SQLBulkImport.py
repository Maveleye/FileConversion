import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

def main(inputfile):
    df = pd.read_csv(inputfile, index_col=False)

    params = urllib.parse.quote_plus('Driver={SQL Server Native Client 11.0};'
                              'Server={(localdb)\ProjectsV13};'
                              'Database=TwitchStream;'
                              'Trusted_Connection=yes;')

    engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)

    df.to_sql('CO_Production_Reports', engine)

if __name__ == '__main__':
    main('C:/Users/gingi/Downloads/2018_prod_reports.csv')
