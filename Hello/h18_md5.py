import hashlib


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())
    pass


if __name__ == "__main__":
    calc_md5("123456")