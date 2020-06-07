import pandas as pd

PATH = 'data/goteborg/'

def convert(filename, month):
  data = pd.read_csv(
                  PATH + 'raw' + filename + '.csv',
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
  data.belopp = data.belopp.str.replace(' ', '')
  data.belopp = data.belopp.str.replace(',', '.')

  data.to_csv(PATH + 'formatted' + filename + '-formatted.csv', index=False)

convert('/2020/leverantorsfakturor-202001', '202001')
convert('/2020/leverantorsfakturor-202002', '202002')
convert('/2020/leverantorsfakturor-202003', '202003')
convert('/2020/leverantorsfakturor-202004', '202004')
