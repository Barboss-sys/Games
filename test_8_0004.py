
"""
Эта программа демонстрирует Лексимезацию(токенизацию)
строковых литералов
"""

def main():
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
    

def display_tokens(data, delimiter):
    token = str(data).split(delimiter)
    for i in token:
        print(f'Ликсема: {i}')


if __name__ == '__main__':
    main()


