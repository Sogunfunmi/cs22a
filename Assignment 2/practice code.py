def main():     #include this line in every program
    
    Celsius = input("Temperature in Celsius? ")
    x = float(Celsius)

    F = ((x * 9/5) +32)
    
    print(F, "Degrees Fahrenheit")

main()          #Call to main() is also required at the end of every program
