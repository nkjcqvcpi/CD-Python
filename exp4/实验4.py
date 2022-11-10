import sys
import re

if __name__ == "__main__":
    with open(sys.argv[1], mode='r') as f:
        text = f.read()
    print(text)
    print(len(text))
    with open('test1.txt', mode='w') as f:
        f.write(text.replace('\n', ''))
    with open('test2.txt', mode='w') as f:
        f.write(text.replace('2012', '2015'))
    print(re.findall(r'(\w*[0-9]+)\w*', text))

import string

if __name__ == "__main__":
    a = "aAsmr3idd4bgs7Dlsf9eAF"
    num = list(filter(str.isdigit, a))
    num = ''.join(num)
    print(num)

    a = a.lower()
    cnt = {}
    for i in string.ascii_lowercase:
        cnt[i] = a.count(i)
        if a.count(i) == 0:
            del cnt[i]
    print(cnt)

    temp = []
    for i in a:
        if i not in temp:
            temp.append(i)
            print(i, end='')
    print()

    t = sorted(cnt.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print(t)
