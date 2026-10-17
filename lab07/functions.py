def sum_digits(number):
    sum=0
    for numb in str(abs(number)):
        sum+=int(numb)
    return sum

def average(numbers):
    return sum(numbers)/len(numbers) if numbers else None

def normalize_text(text):
    result= text.lower().strip()
    while "  " in result:
        result = result.replace("  ", ' ')
    return result

def select_numbers(numbers, threshold):
    result = []
    for numb in numbers:
        if 0<= numb <= threshold:
            result.append(numb)
    return result
