def main():   
    
    print("Welcome to the Unit Converter!")
    
    
    def cm_to_meter(cm):
        return cm / 100

    def meter_to_cm(m):
        return m * 100

    def gram_to_kg(g):
        return g / 1000

    def kg_to_gram(kg):
        return kg * 1000
    
    def metre_to_feet(metre):
        return metre * 3.28084

    def feet_to_metre(feet):
        return feet / 3.28084

    def km_to_mile(km):
        return km * 0.621371

    def mile_to_km(mile):
        return mile / 0.621371

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    print("Select the operation you want to perform:")
    print("1. Centimeters to Meters")
    print("2. Meters to Centimeters")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")
    print("5. Metre to feet")
    print("6. Feet to metre")
    print("7. Km to mile")
    print("8. Mile to kilometre")
    print("9. Fahrenheit to Celsius")
    print("10. Celsius to Fahrenheit")
    
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cm = float(input("Enter length in centimeters: "))
        meter = cm_to_meter(cm)
        print("Length in meters:", meter)
        
    elif choice == 2:
        meter = float(input("Enter length in meters: "))
        cm = meter_to_cm(m)
        print("Length in centimeters:", cm)
        
    elif choice == 3:
        gram = float(input("Enter weight in grams: "))
        kg = g_to_kg(g)
        print("Weight in kilograms:", kg)
        
    elif choice == 4:
        kg = float(input("Enter weight in kilograms: "))
        gram = kg_to_gram(kg)
        print("Weight in grams:", gram)

    elif choice == 5:
        metre = float(input("Enter length in metres: "))
        feet = metre_to_feet(metre)
        print("Length in feet:", feet)

    elif choice == 6:
        feet = float(input("Enter length in feet: "))
        metre = feet_to_metre(feet)
        print("Length in metres:", meter)
    
    elif choice == 7:
        km = float(input("Enter distance in kilometers: "))
        mile = km_to_mile(km)
        print("Distance in miles:", mile)

    elif choice == 8:
        mile = float(input("Enter distance in miles: "))
        km = mile_to_km(mile)
        print("Distance in kilometers:", km)

    elif choice == 9: 
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius:", celsius)

    elif choice == 10:
        celsius = float(input("Enter temperature in Celsius: "))
        farenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", farenheit)

    else:
        print("Invalid input")
        
        
        
main()    