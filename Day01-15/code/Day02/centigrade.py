"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.2f华氏度 = %.2f摄氏度' % (f, c))
#字符串   %代替符号 .1f一位浮点数