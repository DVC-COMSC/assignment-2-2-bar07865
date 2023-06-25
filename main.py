def main():
    
    celcius = int(input("Enter temperature in celcius:"))
    fahrenheit = (9/5)* celcius + 32

    print(f'Fahrenheit: \t {fahrenheit:.2f}')

    return celcius, fahrenheit


if __name__ == '__main__':
    main()
