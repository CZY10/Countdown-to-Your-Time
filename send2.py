import random
import string

def generate_password(length):
    # 所有可能的字符
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # 如果长度小于4，我们将其设置为4，以确保密码至少包含一个大写字母，一个小写字母，一个数字和一个特殊字符
    if length < 4:
        length = 4

    # 生成密码
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)):
            break

    return password

# 生成一个长度为12的密码
password = generate_password(12)

print(f"生成的密码是：{password}")
