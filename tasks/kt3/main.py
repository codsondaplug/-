import re

def get_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        pattern = r'\|'
        data = list(map(lambda line: re.split(pattern, line), lines))
        return data
        
def filtered_books(books, title_param):
    filtered_books = filter(lambda book: title_param.lower() in f"{book[1]} {book[2]}".lower(), books)
    result = list(map(lambda book: [book[0], f"{book[1]}, {book[2]}", book[3], book[4]], filtered_books))
    return result

def calculate_total_price(books):
    result = list(map(lambda book: (book[0], int(book[2]) * float(book[3])), books))
    return result

file_path = 'books.csv'  
data = get_books(file_path)
print(data)

title_param = "Python"
filtered_books = filtered_books(data, title_param)
print(filtered_books)

total_prices = calculate_total_price(filtered_books)
print(total_prices)
