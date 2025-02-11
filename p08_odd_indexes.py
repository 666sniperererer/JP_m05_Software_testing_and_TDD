

def odd_indexes(string):
    return str(string)[1::2]

if __name__ == '__main__':
    print(odd_indexes("řetězec"))
    print(odd_indexes(456))
