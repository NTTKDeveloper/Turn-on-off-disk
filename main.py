# -*- coding: utf-8 -*-
import subprocess as sp

print('Bật hay tắt ổ đĩa F:Khanh')
print('1.Bật')
print('2.Tắt')
option = input()

if option == '1':
    result = sp.check_output('diskpart /s turn_on.txt')
    print('Đã bật ổ đĩa')
elif option == '2':
    result = sp.check_output('diskpart /s turn_off.txt')
    print('Đã tắt ổ đĩa')

