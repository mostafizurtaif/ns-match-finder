def sanitize_ns(string):
    new_string = ''
    sanitized = False
    numbers = [str(num) for num in range(0, 10)]

    for char in string:
        if char not in numbers:
            sanitized = True
            continue
        new_string += char

    return [new_string, sanitized]

