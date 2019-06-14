def chunker(seq, chunk_size=1000):
    # взято здесь: https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length
    return [seq[ind:ind + chunk_size] for ind in range(0, len(seq), chunk_size)]

def count_abc(input_string, chunk_size=1000):
    char_dict = dict([(char, 0) for char in 'abc'])
    result = []
    for chunk in chunker(input_string, chunk_size=chunk_size):
        for char in char_dict:
            char_dict[char] += chunk.count(char)
        result.append(f"a: {char_dict['a']}, b: {char_dict['b']}, c: {char_dict['c']}")

    # итог не выводится если длина строки была меньше 1000 символов
    # (для соответствия первому примеру в задаче)
    if len(input_string) >= chunk_size:
        result.append(f"a: {char_dict['a']}, b: {char_dict['b']}, c: {char_dict['c']}")
    return '\n'.join(result)

def main():
    while True:
        input_string = input('Enter a string to count letters "a, b, c": ')
        print(count_abc(input_string))

if __name__ == '__main__':
    main()
