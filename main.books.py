# TODO Найдите количество книг, которое можно разместить на дискете

# введём исходные данные
disk_size_mb = 1.44
pages = 100
lines_in_each_page = 50
chars_in_each_line = 25
bytes_in_each_char = 4

# объем одной книги в байтах
book_size = pages * lines_in_each_page * chars_in_each_line * bytes_in_each_char

# объем дискеты в байтах (1 Мб = 1024 кб = 1024 * 1024 байт)
disk_size = disk_size_mb * 1024 * 1024

# целое количество книг
count_books = int(disk_size // book_size)


print("Количество книг, помещающихся на дискету:", count_books)
