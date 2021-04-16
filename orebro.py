# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

PATH = 'data/orebro/'

def convert(filename):
  data = pd.read_excel(
                  PATH + 'raw/' + filename + '.xlsx',
                  names=['datum', 'forvaltning', 'leverantor', 'leverantor_id', 'faktura_nr', 'konto_nr', 'belopp', 'empty'],
                  header=0
                  )

  data.drop(columns=['empty'], inplace=True)
  data.dropna(inplace=True)

  data = data[['faktura_nr', 'leverantor', 'leverantor_id', 'forvaltning', 'konto_nr', 'belopp', 'datum']]

  data.insert(0, 'kopare', 2120001967)
  data.insert(1, 'kopare_text', 'Örebro Kommun')
  data.insert(7, 'konto_text', '')
  data.insert(10, 'grund', '')
  data.insert(11, 'avtal', '')
  data.insert(12, 'kommun_id', 1880)
  data.insert(13, 'verksamhet_kod', np.NaN)
  data.insert(14, 'ansvar_kod', np.NaN)
  data.insert(15, 'projekt_kod', np.NaN)
  data.insert(16, 'objekt_kod',  np.NaN)
  data.insert(17, 'aktivitet_kod', np.NaN)
  data.insert(18, 'verksamhet_text', '')
  data.insert(19, 'ansvar_text', '')
  data.insert(20, 'projekt_text', '')
  data.insert(21, 'aktivitet_text', '')
  data.insert(22, 'objekt_text', '')
  data.insert(23, 'valuta', '')

  data.leverantor_id = data.leverantor_id.str.replace('-', '')
  data.leverantor_id = data.leverantor_id.apply(lambda x: x if x.isnumeric() else '')
  data.konto_text = data.konto_nr.str[6:]
  data.konto_nr = data.konto_nr.str[:5]
  data.datum = pd.to_datetime(data.datum, format='%Y-%m-%d')

  data.faktura_nr.astype('object', copy=False)
  data.leverantor.astype('object', copy=False)
  data.leverantor_id.astype('object', copy=False)
  data.konto_nr.astype('Int64', copy=False)
  data.konto_text.astype('object', copy=False)
  data.belopp.astype('float64', copy=False)
  data.kopare_text.astype('object', copy=False)
  data.kommun_id.astype('Int64', copy=False)
  data.valuta.astype('object', copy=False)
  data.ansvar_kod.astype('Int64', copy=False)
  data.verksamhet_kod.astype('Int64', copy=False)
  data.aktivitet_kod.astype('Int64', copy=False)
  data.projekt_kod.astype('Int64', copy=False)
  data.objekt_kod.astype('Int64', copy=False)

  data.to_csv(PATH + 'formatted/' + filename + '-formatted.csv', index=False)

convert('Leverantörsfakturor 2021-01')
convert('Leverantörsfakturor 2021-02')
convert('Leverantörsfakturor 2021-03')
