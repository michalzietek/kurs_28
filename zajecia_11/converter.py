import country_converter as coco
some_names = ['United Rep. of Tanzania', 'DE', 'Cape Verde', '788', 'Burma', 'COG',
              'Iran (Islamic Republic of)', 'Korea, Republic of',
              "Dem. People's Rep. of Korea"]
standard_names = coco.convert(names=some_names, to='name_short')
print(standard_names)
