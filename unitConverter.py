def cm_to_meter(cm):
    return cm / 100

def meter_to_cm(m):
    return m * 100

def gram_to_kg(g):
    return g / 1000

def kg_to_gram(kg):
    return kg * 1000

def main():
    print("Welcome to the Unit Converter!")
    print("1. Centimeters to Meters")
    print("2. Meters to Centimeters")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")
    
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice == 1:
        cm = float(input("Enter length in centimeters: "))
        meter = cm_to_meter(cm)
        print("Length in meters:", meter)
    elif choice == 2:
        meter = float(input("Enter length in meters: "))
        cm = meter_to_cm(m)
        print("Length in centimeters:", cm)
    elif choice == 3:
        g = float(input("Enter weight in grams: "))
        kg = g_to_kg(g)
        print("Weight in kilograms:", kg)
    elif choice == 4:
        kg = float(input("Enter weight in kilograms: "))
        gram = kg_to_gram(kg)
        print("Weight in grams:", gram)
    else:
        print("Invalid choice! try again")

main()
