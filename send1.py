def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# 读取输入文件
input_content = read_file('test.txt')

# 将内容转换为大写
output_content = input_content.upper()

# 将结果写入输出文件
write_file('output.txt', output_content)

print("文件处理完成。")
