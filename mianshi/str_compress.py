def compress_str(s):
    # 存储原始长度
    origin_len = len(s)
    result_list = [s[0], 1]
    # 将字符和个数存储到字典中
    for i in range(2, origin_len):
        if result_list[-2] != s[i]:
            result_list.append(s[i])
            result_list.append(1)
        else:
            result_list[-1] += 1
    if len(result_list) < origin_len:
        compressed_str = ''
        for i in range(len(result_list)//2):
            compressed_str += '%s%s' % (result_list[i*2], result_list[i*2 + 1])
        return compressed_str
    else:
        return s

if __name__ == '__main__':
    print(compress_str('abbbbbccccdddcccccc'))