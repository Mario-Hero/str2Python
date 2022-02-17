#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 28.01.2022, Shenzhen
# My Github site: https://github.com/Mario-Hero
import os.path
import random
import base64
import sys

import obfuscate_str

VAR_START_STR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
VAR_STR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
NUM_STR = '0123456789'
EXE_LIST = ['+', '-', '*', '%', '//']


def randomVarName():
    varName = random.choice(VAR_START_STR)
    for i in range(random.randint(0, 10)):
        varName += random.choice(VAR_STR)
    # print(varName)
    return varName


def obfuscate_strMethod(inputString):
    varName = '___'
    return obfuscate_str.mk_var(inputString, varName).replace("\n", ";") + ';print(' + varName + ')'


def randomIntStr():
    return str(random.randint(1, 100))


def ordMethod(inputString):
    returnStr = 'print(\'%c\' * ' + str(len(inputString)) + ' % ('
    for w in inputString:
        num = ord(w)
        while True:
            # print('target: ' + str(num))
            cal = randomIntStr()
            for i in range(1, random.randint(2, 5)):
                cal += random.choice(EXE_LIST) + randomIntStr()
            # print('equation: ' + cal)
            result = eval(cal)
            fixNumber = int(num - result)
            if abs(result) > 10 * num or abs(result) * 10 < num:
                continue
            # print('result: ' + str(int(result)))
            if int(result + fixNumber) == num + 1:
                fixNumber -= 1
            elif int(result + fixNumber) == num - 1:
                fixNumber += 1
            if fixNumber < 0:
                cal += str(fixNumber)
            else:
                cal += '+' + str(fixNumber)
            # cal = 'int(' + cal + ')'
            # print('final equation: ' + cal)
            # print('final result: ' + str(int(eval(cal))) + '\n')
            returnStr += cal + ','
            break
    returnStr = returnStr[:-1] + '))'
    return returnStr


def asciiMethod(inputString):
    pwd = list(map(ord, inputString))
    outputPwd = '['
    for i in range(len(pwd) - 1):
        outputPwd += str(pwd[i]) + ','
    outputPwd += str(pwd[-1]) + ']'
    return 'print(\'\'.join(map(chr,' + outputPwd + ')))'
    # print(''.join(map(chr, pwd)))


def asciiMethod2(inputString):
    # pwd = list(map(ord, inputString))
    pwd = ''
    for w in inputString:
        num = ord(w)
        if num >= 10000:
            pwd += str(num)
        elif num >= 1000:
            pwd += '0' + str(num)
        elif num >= 100:
            pwd += '00' + str(num)
        elif num >= 10:
            pwd += '000' + str(num)
        else:
            pwd += '0000' + str(num)
    # for i in range(0, len(pwd), 5):
    # print(chr(int(pwd[i:i + 5])), end='')
    return 'for i in range(0,' + str(len(pwd)) + ',5):print(chr(int(\'' + pwd + '\'[i:i+5])),end=\'\')'
    # return 'print(\'\'.join(map(chr,' + str(pwd) + ')))'
    # print(''.join(map(chr, pwd)))


def asciiMethod3(inputString):
    # pwd = list(map(ord, inputString))
    pwd = ''
    delta = ''
    for w in inputString:
        offset = random.randint(0, 9)
        num = ord(w) + offset
        if num >= 10000:
            pwd += str(num)
        elif num >= 1000:
            pwd += '0' + str(num)
        elif num >= 100:
            pwd += '00' + str(num)
        elif num >= 10:
            pwd += '000' + str(num)
        else:
            pwd += '0000' + str(num)
        delta += str(offset)
    return 'for i in range(0,' + str(len(pwd)) + ',5):print(chr(int(\'' + pwd + '\'[i:i+5])-int(\'' + delta + '\'[int(i/5)])),end=\'\')'
    # return 'print(\'\'.join(map(chr,' + str(pwd) + ')))'
    # print(''.join(map(chr, pwd)))


def divideMethod(inputString):
    for methodi in range(20):
        try:
            pwd = ''
            for w in inputString:
                while True:
                    b = random.randint(1, 100) * (random.randint(0, 1) * 2 - 1)
                    wpart = ord(w) + b
                    wpart2 = ord(w) - b
                    pwd += chr(wpart) + chr(wpart2)
                    break
            varName = randomVarName()
            print(pwd)
            returnStr = varName + '=\'' + pwd + '\';\nfor i in range(0,len(' + varName + '),2):print(chr(int((ord(' + varName + '[i]) + ord(' + varName + '[i+1]))/2)),end=\'\')'
            # returnStr = 'for i in range(0,' + str(len(pwd)) + ',2):print(chr(int((ord(\'' + pwd + '\'[i]) + ord(\'' + pwd + '\'[i+1]))/2)),end=\'\')'
            return returnStr
        except:
            continue
    return ''


def minusMethod(inputString):  # 错误的。无法实现
    for methodi in range(20):
        pwd = ''
        line1 = ''
        line2 = ''
        for w in inputString:
            while True:
                try:
                    b = random.randint(1, 10) * (random.randint(0, 1) * 2 - 1)
                    c = ord(w) + b
                    pwd += chr(b) + chr(c)
                    print(chr(b) + chr(c))
                    # print(pwd)
                    line2 += chr(b)
                    line1 += chr(c)
                    break
                except:
                    continue
        returnStr = 'for i in range(' + str(len(line1)) + '):print(chr(int(ord(\'' + line1 + '\'[i]) - ord(\'' + line2 + '\'[i]))),end=\'\')'
        print(returnStr)
        # returnStr = varName + '=\'' + pwd + '\';\nfor i in range(0,len(' + varName + '),2):print(chr(int((ord(' + varName + '[i]) + ord(' + varName + '[i+1]))/2)),end=\'\')'
        # returnStr = 'for i in range(0,' + str(len(pwd)) + ',2):print(chr(int((ord(\'' + pwd + '\'[i]) + ord(\'' + pwd + '\'[i+1]))/2)),end=\'\')'
        return returnStr
    return ''


def linearMethod(inputString):
    for methodi in range(20):
        try:
            k = 1
            b = int(random.randint(1, 1000) * ((random.randint(0, 1) * 2) - 1))
            pwd = ''
            for w in inputString:
                pwd += chr(k * ord(w) + b)
            print(pwd)
            print('k:' + str(k) + ' b:' + str(b))
            returnStr = 'for w in r\'' + pwd + '\':print(chr(int((ord(w)-' + str(b) + ')/ ' + str(k) + ' )),end=\'\')'
            exec(returnStr)
            return returnStr
        except:
            continue
    return ''


def base64Method(inputString):
    orig = inputString.encode('utf8')
    pwd = base64.b64encode(orig).decode('utf8')
    # print(pwd)  # base64加密
    # print(base64.b64decode(pwd).decode('utf8'))  # base64解密
    return 'import base64;print(base64.b64decode(\'' + pwd + '\').decode(\'utf8\'))'


def smallGaussMethod(inputString):
    pwd = ''
    n = len(inputString)
    if n % 2 == 1:
        inputString += ' '
        n += 1
    for i in range(int(n / 2)):
        pwd += inputString[i] + inputString[-i - 1]
    # print(pwd)
    varName = randomVarName()
    return varName + '=\'' + pwd + '\';print(' + varName + '[::2] + ' + varName + '[::-2])'
    # print(res)


def smallGaussMethod2(inputString):
    pwd = ''
    n = len(inputString)
    if n % 2 == 1:
        inputString += ' '
        n += 1
    pwd = inputString[::2] + inputString[::-2]
    varName = randomVarName()
    return varName + '=\'' + pwd + '\';\nfor i in range(' + str(
        int(n / 2)) + '):\n    print(' + varName + '[i] + ' + varName + '[-i-1],end=\'\')'


def smallGaussMethod3(inputString):
    pwd = ''
    n = len(inputString)
    if n % 2 == 1:
        inputString += ' '
        n += 1
    for i in range(int(n / 2), -1, -1):
        pwd += inputString[-i - 1] + inputString[i]
    # print(pwd)
    varName = randomVarName()
    return varName + '=\'' + pwd + '\';print(' + varName + '[::-2] + ' + varName + '[::2])'
    # print(res)


def utf8Method(inputString):  # 无法加密英文
    pwd = inputString.encode('gbk')
    print(pwd.decode('gbk'))
    print(pwd)
    return 'print(' + str(pwd) + '.decode(\'gbk\'))'


def upsideDown(inputString):
    return 'print(\'' + inputString[::-1] + '\'[::-1])'


def upsideDown2(inputString):
    pwd = ''
    for w in inputString:
        pwd += w + random.choice(inputString)
    pwd = pwd[::-1]
    return 'print(\'' + pwd + '\'[::-2])'


def getResult(inputMain):
    for i in range(20):
        method = random.randint(0, 12)
        if method == 0:
            result = obfuscate_strMethod(inputMain)
        elif method == 1:
            result = asciiMethod(inputMain)
        elif method == 2:
            result = upsideDown(inputMain)
        elif method == 3:
            result = base64Method(inputMain)
        elif method == 4:
            result = divideMethod(inputMain)
        elif method == 5:
            result = asciiMethod2(inputMain)
        elif method == 6:
            result = smallGaussMethod(inputMain)
        elif method == 7:
            result = smallGaussMethod2(inputMain)
        elif method == 8:
            result = smallGaussMethod3(inputMain)
        elif method == 9:
            result = asciiMethod3(inputMain)
        elif method == 10:
            result = ordMethod(inputMain)
        elif method == 11:
            result = upsideDown2(inputMain)
        else:
            result = linearMethod(inputMain)
        if result:
            print('Method: ' + str(method))
            return result
    return ''


def loadCommand(inputAddr):
    if inputAddr != 'quit' and inputAddr != 'exit':
        if inputAddr:
            resultCommand = getResult(inputAddr)
            print('\n===Test output===')
            exec(resultCommand)
            print('\n===Result===')
            print(resultCommand)
        return True
    return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please input text:')
        while True:
            inputAddr = input('>')
            inputAddr = inputAddr.strip().lower()
            if not loadCommand(inputAddr):
                break
    elif len(sys.argv) == 2:
        inputAddr = sys.argv[1]
        if inputAddr.endswith('.txt') and os.path.exists(inputAddr):
            parentFolder, fileName = os.path.split(inputAddr)
            newName = fileName[:-4] + '_tran_1.txt'
            with open(inputAddr, 'r', encoding='utf-8') as f:
                inputAddr = f.read()
                if inputAddr:
                    resultPython = getResult(inputAddr)
                    if resultPython:
                        iname = 2
                        while os.path.exists(os.path.join(parentFolder, newName)):
                            newName = fileName[:-4] + '_tran_' + str(iname) + '.txt'
                            iname += 1
                        print('Save as ' + newName)
                        newF = open(os.path.join(parentFolder, newName), 'w', encoding='utf-8')
                        newF.write(resultPython)
                        newF.close()
            os.system('pause')
        else:
            loadCommand(inputAddr)
    else:
        loadCommand(' '.join(sys.argv[1:]).strip().lower())
