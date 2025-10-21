def leiadinheiro(teste):
    val = False
    while not val:
        num = str(input(teste)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[0;32mERRO: "{num}" é um preço invalido!\033[m')
        else:
            val = True
            return float(num)

