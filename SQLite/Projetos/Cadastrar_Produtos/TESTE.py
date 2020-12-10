from datetime import datetime

hoje = str(datetime.today().time())
data = str(datetime.today().date())
print(data)
print(hoje[:-7])