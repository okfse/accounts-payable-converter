import pandas as pd
import os
from sqlalchemy import *
from sshtunnel import SSHTunnelForwarder


METABASE_TEST = '135.181.196.245'
METABASE = 'bi.openup.open-knowledge.se'

# Create an SSH tunnel
tunnel = SSHTunnelForwarder(
    (METABASE_TEST, 22),
    ssh_username='root',
    ssh_private_key='~/.ssh/id_rsa',
    ssh_private_key_password=os.environ.get('SSH_PRIVATE_KEY_PASSWORD'),
    remote_bind_address=('localhost', 5432),
)

tunnel.skip_tunnel_checkup = False

# Start the tunnel
tunnel.start()
tunnel.check_tunnels()
print(tunnel.tunnel_is_up)

DATABASE_URL = 'postgresql+psycopg2://metabase:' + os.environ.get('DATABASE_PASSWORD') + '@' + tunnel.local_bind_host + ':' + str(tunnel.local_bind_port) +'/data'

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
result_set = engine.execute("SELECT * FROM leverantorsreskontra WHERE kopare_text='Länsstyrelsen i Blekinge län'")
for r in result_set:
    print(r)


def import_data(filename):
  print('Importing ' + filename + '...')
  data = pd.read_csv(filename)

  data.to_sql('leverantorsreskontra',
              con = engine,
              if_exists = 'append',
              index = False,
              chunksize = 10000)

  print('Successfully imported ' + filename + '!')

# import_data('data/digg/formatted/2018 DIGG leverantörsfakturor-formatted.csv')
tunnel.close()
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201908-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201907-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201906-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201905-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201904-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201903-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201902-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201901-formatted.csv')
#
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201812-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201811-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201810-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201809-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201808-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201807-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201806-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201805-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201804-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201803-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201802-formatted.csv')
# import_data('data/goteborg/formatted/2019/leverantorsfakturor-201801-formatted.csv')
