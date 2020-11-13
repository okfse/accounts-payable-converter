import pandas as pd
from sqlalchemy import *
from sshtunnel import SSHTunnelForwarder

# Create an SSH tunnel
tunnel = SSHTunnelForwarder(
    ('bi.openup.open-knowledge.se', 22),
    ssh_username='root',
    ssh_private_key='~/.ssh/id_rsa',
    remote_bind_address=('localhost', 5432),
    local_bind_address=('localhost', 5432), # could be any available port
)

# Start the tunnel
tunnel.start()

DATABASE_URL = 'postgresql+psycopg2:///metabase:metabase@' + tunnel.local_bind_host + ':' + str(tunnel.local_bind_port) + '/data'
LOCAL_URL = 'postgresql://localhost/openup_data'

engine = create_engine(DATABASE_URL)

def import_data(filename):
  print('Importing ' + filename + '...')
  data = pd.read_csv(filename)

  data.to_sql('leverantorsreskontra',
              con = engine,
              if_exists = 'append',
              index = False,
              chunksize = 10000)

  print('Successfully imported ' + filename + '!')

import_data('data/goteborg/formatted/2019/leverantorsfakturor-201908-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201907-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201906-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201905-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201904-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201903-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201902-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201901-formatted.csv')

import_data('data/goteborg/formatted/2019/leverantorsfakturor-201812-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201811-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201810-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201809-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201808-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201807-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201806-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201805-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201804-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201803-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201802-formatted.csv')
import_data('data/goteborg/formatted/2019/leverantorsfakturor-201801-formatted.csv')
