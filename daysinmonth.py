def dnimiesiaca_func():
  miesiac = int(input("Podaj numer miesiąca: \n"))
  rok = int(input("Podaj rok: \n"))

  if((miesiac == 2) and ((rok % 4 == 0)  or ((rok % 100 == 0) and (rok % 400 == 0)))):
      print("Liczba dni w miesiącu to: 29");
  elif(miesiac == 2):
      print("Liczba dni w miesiącu to: 28");
  elif(miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac == 7 or miesiac == 8 or miesiac == 10 or miesiac == 12):
      print("Liczba dni w miesiącu to: 31");
  elif(miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11):
      print("Liczba dni w miesiącu to: 30");
  else:
      print("Podałeś nieprawidłową wartość. Użyj liczb z zakresu 1-12.");

dnimiesiaca_func()
