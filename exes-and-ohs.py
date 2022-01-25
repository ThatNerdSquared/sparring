def xo(s):
    if (s.count('x') + s.count('X') == s.count('o') + s.count('O')):
        return True
    else:
        return False
