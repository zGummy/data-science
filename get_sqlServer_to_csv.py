import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=windows.net;'
                      'Database=DB;'
                      'UID=usr_name;'
                      'PWD=password;'
                      'Trusted_Connection=no;')

sql_query = pd.read_sql_query(''' 
                              SELECT COD_MATRICULA,NOM_PESSOA,COD_INDICADOR,INDICADOR_NOME,NOM_OPERACAO,RESULTADO,META,DAT_DIA 
                              FROM DB_PROVA.prova.TB_PRODUTIVIDADE 
                              ORDER BY DAT_DIA, INDICADOR_NOME
                              '''
                              ,conn) 

df = pd.DataFrame(sql_query)
df.to_csv (r'exported_data.csv', index = False) 