import random
wykonanePróby = 0
print('Czesc jak masz na imię')
mojeImie = input()
liczba = random.randint(1,20)
print('Słuchaj, ' + mojeImie + ', myslę o liczbie z przedziału od 1 do 20')
for wykonanePróby in range(1,20):
  print('Spróbuj  odgadnąć.')
  próbaOdgadnięcia = input()
  próbaOdgadnięcia = int(próbaOdgadnięcia)
  if(próbaOdgadnięcia<liczba):
    print("Twoja liczba jest za mała.")
  if(próbaOdgadnięcia>liczba):
    print("Twoja liczba jest za duża")
  if(próbaOdgadnięcia==liczba ):
    break;
if(próbaOdgadnięcia==liczba):
  wykonanePróby = str(wykonanePróby+1)
  print('Swietna robota, '+mojeImie+' udalo Ci sie odgadnąć w '+wykonanePróby+' probach!')

if(próbaOdgadnięcia!=liczba):
  liczba = str(liczba)
  print('Niestety nie. Liczba, ktora mialem na mysli')