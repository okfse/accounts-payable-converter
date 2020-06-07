import pandas as pd

PATH = 'data/goteborg/'

def convert(filename, month):
  data = pd.read_excel(
                  PATH + 'raw' + filename + '.xlsx',
                  sep=';',
                  names=['forvaltning', 'leverantor', 'leverantor_id', 'faktura_nr', 'konto_nr', 'konto_text', 'belopp'],
                  header=0
                  )

  data.dropna(inplace=True)

  data = data[['faktura_nr', 'leverantor', 'leverantor_id', 'forvaltning', 'konto_nr', 'konto_text', 'belopp']]

  data.insert(0, 'kopare', 2120001355)
  data.insert(1, 'kopare_text', 'Göteborgs stad')
  data.insert(9, 'datum', pd.to_datetime(month, format='%Y%m'))
  data.insert(10, 'grund', '')
  data.insert(11, 'avtal', '')
  data.insert(12, 'kommun_id', 1480)

  data.leverantor_id = data.leverantor_id.astype(str)
  data.leverantor_id = data.leverantor_id.apply(lambda x: '' if 'nan' in x else x)
  data.leverantor_id = data.leverantor_id.apply(lambda x: x if x.isnumeric() else '')
  data.leverantor_id = data.leverantor_id.str.replace('-', '')
  data.leverantor = data.leverantor.astype(str)
  data.leverantor = data.leverantor.replace(',', '')

  data.to_csv(PATH + 'formatted' + filename + '-formatted.csv', index=False)

convert('/2017/leverantorsfakturor-201712', '201712')
convert('/2017/leverantorsfakturor-201711', '201711')
convert('/2017/leverantorsfakturor-201710', '201710')
convert('/2017/leverantorsfakturor-201709', '201709')
convert('/2017/leverantorsfakturor-201708', '201708')
convert('/2017/leverantorsfakturor-201707', '201707')
convert('/2017/leverantorsfakturor-201706', '201706')
convert('/2017/leverantorsfakturor-201705', '201705')
convert('/2017/leverantorsfakturor-201704', '201704')
convert('/2017/leverantorsfakturor-201703', '201703')
convert('/2017/leverantorsfakturor-201702', '201702')
convert('/2017/leverantorsfakturor-201701', '201701')
convert('/2016/leverantorsfakturor-201601', '201601')
