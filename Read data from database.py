import pandas as pd

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

auth_provider = PlainTextAuthProvider(username=CASSANDRA_USER, password=CASSANDRA_PASS)
cluster = Cluster(contact_points=[CASSANDRA_HOST], port=CASSANDRA_PORT,
    auth_provider=auth_provider)

session = cluster.connect(CASSANDRA_DB)
session.row_factory = dict_factory

query = "SELECT * FROM Table"

df = pd.DataFrame()

for row in session.execute(query):
    df = df.append(pd.DataFrame())
    
# problem: The dataframe took more than 10x space (in RAM) compared to the space the data was occupying in the original DB.
# Using an H2O dataframe is more efficient (in my case it took 2x-3x space in RAM).
# Also look at this post. If you can read data in chunks, that could help.

pandas.read_sql_query(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None, dtype=None)

********************************************************************************************************************************
# Pandas now has built-in support for chunked loading.
# You could simply try to read the input table chunk-wise and assemble your full dataframe from the individual pieces afterwards, like this:

import pandas as pd
import pandas.io.sql as psql
chunk_size = 10000
offset = 0
dfs = []
while True:
  sql = "SELECT * FROM MyTable limit %d offset %d order by ID" % (chunk_size,offset) 
  dfs.append(psql.read_frame(sql, cnxn))
  offset += chunk_size
  if len(dfs[-1]) < chunk_size:
    break
full_df = pd.concat(dfs)

#It might also be possible that the whole dataframe is simply too large to fit in memory, 
# in that case you will have no other option than to restrict the number of rows or columns you're selecting.
********************************************************************************************************************************
# Fastest way to read Cassandra data into pandas with automatic iteration of pages. 
# Create dictionary and add each to it by automatically iterating all pages. Then, create dataframe with this dictionary.

import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

auth_provider = PlainTextAuthProvider(username=CASSANDRA_USER, password=CASSANDRA_PASS)
cluster = Cluster(contact_points=[CASSANDRA_HOST], port=CASSANDRA_PORT,
    auth_provider=auth_provider)

session = cluster.connect(CASSANDRA_DB)
session.row_factory = dict_factory

sql_query = "SELECT * FROM {}.{};".format(CASSANDRA_DB, CASSANDRA_TABLE)

dictionary ={"column1":[],"column2":[]}

for row in session.execute(sql_query):
    dictionary["column1"].append(row.column1)
    dictionary["column1"].append(row.column1)

df = pd.DataFrame(dictionary)
