import random
import time

def ejamPieKoka():
  print("Ejam līdz kokam...")
  time.sleep(1)
  print("Esam pie koka! Kas tālāk?")
  purinamKoku()

def purinamKoku():
  print("Purinam koku...")
  skaits = random.randrange(0, 30)
  print("Nokrita ", skaits, " āboli")
  lasamAbolus(skaits)

def lasamAbolus(skaits):
  for i in range(1, skaits+1):
    print("Paņemam ābolu...", i)
    time.sleep(1)
  else:
    print("Visi āboli salasīti!")
  darbsIzdarits()

def darbsIzdarits():
  print("Labs darbiņš!")

ejamPieKoka()
