'''
字符编码的原理，字符编码发展过程

    因为计算机识别的是机器语言，人类编程时使用的是人类的字符，所以需要进行字符编码，
使得计算机和人类之间能通过编程顺畅的沟通。
    最早期是美国人设计的ASCII码，仅能表示机器语言与英文字符和数字之间的对应关系；
    然后中国人、日本人、韩国人等各个国家的人都开始基于本国语言规定编码，于是出现了
GBK、Shift_JIS、Euc_kr等编码；
    后来各国之间有自己的编码不利于沟通交流，于是出现了能够兼容万国语言的字符编码
Unicode，Unicode存在内存中，负责将存在硬盘中的各国编码转化成Unicode；
    最后，为了优化硬盘占用，节省IO操作时间，出现了对Unicode的优化：UTF-8（硬盘）.
    
'''


'''
python2和python3中字符串类型的区别
    
    写程序时，默认保存的代码是UTF-8编码的：
    python3解释器默认使用UTF-8编码来读代码；
    python2解释器默认使用ASCII码来读代码；执行时会先以unicode读入内存，存在内存中

'''


'''
保证不乱码的核心

    文件用什么编码保存的，就用什么编码读取。
    
'''


