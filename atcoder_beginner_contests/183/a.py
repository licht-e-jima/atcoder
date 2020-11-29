def relu(x) -> int:
    return x if x >= 0 else 0

def main():
    x = int(input())
    print(relu(x))

if __name__ == '__main__':
    main()
