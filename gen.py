stringos = ['arnet','Arnet','ARNET','fiber','Fiber','FIBER','fibertel','Fibertel','FIBERTEL','FiberTel','metro','Metro','METRO','metrotel','Metrotel','MetroTel','METROTEL','telecentro','Telecentro','TeleCentro','TELECENTRO','tele','Tele','TELE']

i=0

for telco in stringos:
  for length in range(max(0,8-len(telco)),8):
    for num in range(99999999):
      i += 1
      print telco + str(num).zfill(length)
