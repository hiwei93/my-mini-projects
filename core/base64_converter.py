import base64


def encode(text: str, encoding: str = 'utf-8') -> str:
    b = text.encode(encoding)
    r = base64.b64encode(b)
    return r.decode(encoding)


def decode(text: str, encoding: str = 'utf-8') -> str:
    b = text.encode(encoding)
    r = base64.b64decode(b)
    return r.decode(encoding)


if __name__ == '__main__':
    print(decode(encode('hello')))