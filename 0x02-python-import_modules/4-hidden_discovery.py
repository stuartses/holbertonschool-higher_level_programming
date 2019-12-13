#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    for i in range(len(str)):
        if str[i][0] != "_" and str[i][1] != "_":
            print(str[i])
