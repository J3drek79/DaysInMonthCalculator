miesiac = int(input("Podaj numer miesiąca: \n"))
rok = int(input("Podaj rok: \n"))
    
if((miesiac == 2) and ((rok % 4 == 0)  or ((rok % 100 == 0) and (rok % 400 == 0)))):
    print("Liczba dni w miesiacu to: 29");
elif(miesiac == 2):
    print("Liczba dni w miesiacu to: 28");
elif(miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac == 7 or miesiac == 8 or miesiac == 10 or miesiac == 12):
    print("Liczba dni w miesiacu to: 31");
else:
    print("Liczba dni w miesiacu to: 30");
