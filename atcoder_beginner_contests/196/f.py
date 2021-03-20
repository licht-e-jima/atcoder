def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)

    import numpy as np
    S_np = np.array(list(map(int, S)))
    T_np = np.array(list(map(int, T)))

    print(min([
        np.sum(S_np[i:i+T_len] != T_np)
        for i in range(S_len-T_len+1)
    ]))

if __name__ == '__main__':
    main()
