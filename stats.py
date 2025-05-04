def count_words(book_text):
    book_text_list = book_text.split()
    return len(book_text_list)

def order_counted_chars(dic):
    def criterio_orden(tupla):
        return tupla[1] 
    ordenado = sorted(dic.items(), key=criterio_orden, reverse=True)
    diccionario_ordenado = dict(ordenado)
    return diccionario_ordenado

def print_dictionary(dic):
    lines = []
    for key,value in dic.items():
        lines.append(f"{key}: {value}")
    result = "\n".join(lines)
    return result

def count_characters(book_text):
    lower_book_text = book_text.lower()
    letter_dict = {}
    assert isinstance(lower_book_text,str)
    for letter in lower_book_text:
        if not letter.isalpha():
            continue
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    letter_dict_ordered = order_counted_chars(letter_dict)
    result = print_dictionary(letter_dict_ordered)
    return result
 
