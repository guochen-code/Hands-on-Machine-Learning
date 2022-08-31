
keysapce table name and colmn name cannot have upper case letter !!!!!! pain!!!!!!!!!!!!!!

unmatched column/value: not specify which column name here. large chance, not define one column, but has value of this column in the value list
example:

statement = f"INSERT INTO <keyspacename>.<tablename> (col1,col2,col3) VALUES (1,2,3,4) "


****************************************************************************************************************************************************************
from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import time
import pandas as pd


try:
  # connect to database by creating a session
  ssl_context = SSLContext(PROTOCOL_TLSv1_2)
  ssl_context.load_verify_locations('sf-class2-root.crt')
  ssl_context.verify_mode = CERT_REQUIRED
  auth_provider = PlainTextAuthProvider(username='xxxxuser-xx-xxxxx',
                                        password='xxxxxxxxxxxxx')
  cluster = Cluster(['cassandra.us-east-1.amazonaws.com'], ssl_context=ssl_context,
                    auth_provider=auth_provider, port=9142)
  session = cluster.connect()

  # 0-22 !!!!!!!!!

  df_ml_lst=list(df_ml.iloc[0,:])
  my_time = int(time.time())
  print(df_ml_lst)

  try:
      statement = f"INSERT INTO <keyspacename>.<tablename> (col1,col2,col3) VALUES (1,2,3,4) "
      user_lookup_stmt = session.prepare(statement)
      user_lookup_stmt.consistency_level = ConsistencyLevel.LOCAL_QUORUM
      session.execute(user_lookup_stmt)
  except Exception as err:
      print('database insert error:', err)
      cluster.close()
      
except Exception as err:
  print(f"database error for {opla_job}:", err)
  cluster.close()

***********************************************************************************************************************************************************
  data type ascii: max size: 204.8KB
