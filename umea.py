import pandas as pd

PATH = 'data/umea/'

def convert(filename):
  data = pd.read_csv(
                  PATH + 'raw' + filename + '.csv',
                  sep=';',
                  names=['datum', 'forvaltning', 'leverantor', 'leverantor_id', 'konto_nr', 'konto_text', 'belopp', 'faktura_nr'],
                  header=0
                  )

  data.dropna(inplace=True)

  data = data[['faktura_nr', 'leverantor', 'leverantor_id', 'forvaltning', 'konto_nr', 'konto_text', 'belopp', 'datum']]

  data.insert(0, 'kopare', 2120002627)
  data.insert(1, 'kopare_text', 'Umeå Kommun')
  data.insert(10, 'grund', '')
  data.insert(11, 'avtal', '')
  data.insert(12, 'kommun_id', 2480)

  data.datum = pd.to_datetime(data.datum, format='%Y%m')

  data.leverantor_id = data.leverantor_id.apply(lambda x: '' if '*' in x else x)
  data.leverantor_id = data.leverantor_id.str.replace('-', '')
  data.leverantor = data.leverantor.astype(str)
  data.leverantor = data.leverantor.apply(lambda x: 'ANONYMERAD' if '*' in x else x)

  data.to_csv(PATH + 'formatted' + filename + "-formatted.csv", index=False)

#convert("leverantorsfakturor-2017")
#convert("leverantorsfakturor-2018")
#convert("leverantorsfakturor-2019")
convert("/leverantorsfakturor-2020")
