def solution(s: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    _s = s.split(".")
    result = ""
    l = len(_s[0])
    for i in range(l):
        if _s[0][i] == 0:
            _s[0] = _s[0][1:-1]
    l = len(_s[0])
    for i in range(l):
        if i > 0 and i % 3 == 0:
            result = f"{_s[0][l-i-1]},{result}"
        else:
            result = f"{_s[0][l-i-1]}{result}"
    if len(_s) == 2:
        result = f"{result}."
        l = len(_s[1])
        for i in range(l):
            if i > 0 and i % 3 == 0:
                result = f"{result},{_s[1][i]}"
            else:
                result = f"{result}{_s[1][l-i-1]}"
    print(result)
    return result


if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')