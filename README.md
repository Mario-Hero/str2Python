# str2Python 字符串转Python

能把文本转换为“输出该文本的Python脚本”的Python脚本（加密了，但没完全加密）。

A Python script that converts text into a python program which outputs the text.

## 依赖 Dependency

Python 3

## 用法 Usage

下载项目，打开str2Python.py，输入要转换的字符，回车即可。或者拖入txt文件到str2Python.py，会自动转换并保存为另一个txt文件。 

Download project, open str2Python.py, enter the text needed to be converted and press enter. Or drag a TXT file into the script, which will automatically convert it and saved as another TXT file.

## 举例子 Example

输入“针不戳”，回车，可能有以下结果：

Enter "针不戳" and press enter. The following results may be obtained:

<br>

===Test output===

针不戳

===Result===

for i in range(0,15,5):print(chr(int('380251998225143'[i:i+5])-int('114'[int(i/5)])),end='')

===Result===

print('%c' * 3 % (41%91+7*97*60-2757,79+95*41+16007,39-73*38+27874))

===Result===

print(''.join(map(chr,[38024,19981,25139])))

===Result===

for w in r'釰䭵徛':print(chr(int((ord(w)--664)/ 1 )),end='')

===Result=== @[Python String Obfuscator](https://github.com/d4em0n/nostr)

`_=((()==())+(()==()));__=(((_<<_)<<_)*_);___=('c%'[::(([]!=[])-(()==()))])*(_+(()==()))%(((((((((_<<_)<<_)<<_)<<_)<<_)<<_)<<_)+(((((((_<<_)<<_)<<_)<<_)<<_)*_)+((((((_<<_)<<_)<<_)<<_)*_)+((((_<<_)<<_)<<_)+(_<<_))))),((((((((_<<_)<<_)<<_)<<_)<<_)<<_)*_)+((((((_<<_)<<_)<<_)<<_)<<_)+((((((_<<_)<<_)<<_)<<_)*_)+(((((_<<_)<<_)<<_)<<_)+((_<<_)+((_*_)+(()==()))))))),((((((((_<<_)<<_)<<_)<<_)<<_)<<_)*_)+(((((((_<<_)<<_)<<_)<<_)<<_)<<_)+(((((_<<_)<<_)<<_)<<_)+(((_<<_)<<_)+(((_<<_)*_)+(_+(()==()))))))));print(___)`

===Result===

import base64;print(base64.b64decode('6ZKI5LiN5oiz').decode('utf8'))

## 感谢 Thanks to

其中一个方法来自：[Python String Obfuscator](https://github.com/d4em0n/nostr)

## License

The project is released under MIT License.
