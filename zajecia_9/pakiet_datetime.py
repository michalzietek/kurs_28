import datetime
#from datetime import datetime, timedelta
data_string = "2024-03-04 18:08:00"

data_format = "%Y-%m-%d %H:%M:%S"

data = datetime.datetime.strptime(data_string, data_format)
nowa_subskrypcja = data + datetime.timedelta(days=60)
print(nowa_subskrypcja)
roznica_czasu = datetime.datetime.now() - data
print(roznica_czasu)
print(datetime.datetime.now())
print(data)
print(type(data))
