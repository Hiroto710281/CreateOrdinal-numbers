def ordinal(num):
    if num // 10 % 10 == 1:
        suffix = "th"
    elif num % 10 == 1:
        suffix = "st"
    elif num % 10 == 2:
        suffix = "nd"
    elif num % 10 == 3:
        suffix = "rd"  
    else:
        suffix = 'th'
    return str(num) + suffix

if __name__ == "__main__":
    print(ordinal(32))
    print(ordinal(13))
    print(ordinal(3))
    print(ordinal(22))