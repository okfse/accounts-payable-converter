import pandas as pd

PATH = 'data/orebro/'

def convert(filename, month):
  data = pd.read_excel(
                  PATH + 'raw' + filename + '.xlsx',
                  names=['forvaltning', 'leverantor', 'leverantor_id', 'faktura_nr', 'konto_nr', 'belopp'],
                  header=0
                  )

  data.dropna(inplace=True)

  data = data[['faktura_nr', 'leverantor', 'leverantor_id', 'forvaltning', 'konto_nr', 'belopp']]

  data.insert(0, 'kopare', 2120001967)
  data.insert(1, 'kopare_text', 'Örebro Kommun')
  data.insert(7, 'konto_text', '')
  data.insert(9, 'datum', pd.to_datetime(month, format='%Y%m'))
  data.insert(10, 'grund', '')
  data.insert(11, 'avtal', '')
  data.insert(12, 'kommun_id', 1880)

  data.leverantor_id = data.leverantor_id.str.replace('-', '')
  data.leverantor_id = data.leverantor_id.apply(lambda x: x if x.isnumeric() else '')
  data.konto_text = data.konto_nr.str[6:]
  data.konto_nr = data.konto_nr.str[:5]

  data.to_csv(PATH + 'formatted' + filename + '-formatted.csv', index=False)

convert('/2020/leverantörsfakturor 2020-05', '202005')
convert('/2020/leverantörsfakturor 2020-06', '202006')
convert('/2020/leverantörsfakturor 2020-07', '202007')
convert('/2020/leverantörsfakturor 2020-08', '202008')
convert('/2020/leverantörsfakturor 2020-09', '202009')
convert('/2020/leverantörsfakturor 2020-10', '202010')
