def execute():
    binarydat = input("Enter Your Binary Value: ")

    decimal_value = int(binarydat, 2)
    
    try:
        text_value = chr(decimal_val)
        
        if decimal_value < 32:
            text_value = "(Invis)"
    except:
        text_value = "(Invalid Character)"

    print(f"Decimal: {decimal_value}")
    print(f"ASCII: {text_value}")

execute()