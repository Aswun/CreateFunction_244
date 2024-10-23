def KonversiSuhu():
    temperature = float(input("Masukan suhu: "))
    unit = input("Masukkan unit ('C' atau 'F') : ")
    
    if unit.upper() == 'C':
        fahrenheit = (temperature * 9/5) + 32
        return f"{temperature}°C = {fahrenheit}°F"
    elif unit.upper() == 'F':
        celcius = (temperature - 32) * 5/9
        return f"{temperature}°F = {celcius}°C"
    else:
        print("Unit tidak valid. Gunakan 'C' atau 'F'.")

#CkeF = KonversiSuhu(25, 'c')
#FkeC = KonversiSuhu(77, 'f')
#print(f"25 Celsius adalah {CkeF} Fahrenheit")
#print(f"77 Fahrenheit adalah {FkeC} Celsius")
print(KonversiSuhu())