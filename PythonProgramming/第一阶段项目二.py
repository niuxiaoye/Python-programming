'''
项目一

打印三级菜单如：汽车、种类、品牌、型号、可以自由发挥
可返回上一级
可随时退出程序
'''
menu = {
    '汽车':{
        '轿车':{
            '宝马':{
                '宝马760':{},
                '宝马M5':{},
                '宝马M3':{},
            },
            '奔驰':{
                '奔驰C180':{},
                '奔驰E260':{},
                '奔驰S600':{},
            },
            '奥迪':{
                '奥迪A4L':{}
            },
        },
        '越野车':{
            '保时捷':{
                '保时捷Macan':{},
                '保时捷Cayenne':{},
            },
            '路虎':{},
            '英菲尼迪':{},
        },
        '卡车':{},
        '公交车':{},
    },
    '飞机':{
        '大飞机':{
            '大1':{
                'ddd':{}
            }
        },
        '小飞机':{
            '小1':{
                'xxx':{}
            }
        },
        '直升机':{}
    },
    '大炮':{}
}

tag = True
while tag & bool(menu):
    print('可选商品名称为：')
    for key in menu:  # 打印商品根目录
        print(key)
    choice = input('输入商品名称获取一级目录\n输入 q 退出程序\n请输入: ').strip()  # 选择商品根目录
    if choice == 'q':
        tag = False
    elif choice not in menu:
        print('输入有误，请重新输入')
        continue
    else:
        while tag & bool(menu[choice]):
            print('\n%s的一级目录为：' % choice)
            for key1 in menu[choice]:  # 打印商品一级目录
                print(key1)
            choice1 = input('输入一级目录获取二级目录\n输入 b 返回上级菜单\n输入 q 退出程序\n请输入: ').strip()  # 选择商品一级目录
            if choice1 == 'q':
                tag = False
            elif choice1 == 'b':
                break
            elif choice1 not in menu[choice]:
                print('输入有误，请重新输入')
                continue
            else:
                while tag & bool(menu[choice][choice1]):
                    print('\n%s的二级目录为：' % choice1)
                    for key2 in menu[choice][choice1]:  # 打印商品二级目录
                        print(key2)
                    choice2 = input('输入一级目录获取二级目录\n输入 b 返回上级菜单\n输入 q 退出程序\n请输入: ').strip()  # 选择商品二级目录
                    if choice2 == 'q':
                        tag = False
                    elif choice2 == 'b':
                        break
                    elif choice2 not in menu[choice][choice1]:
                        print('输入有误，请重新输入')
                        continue
                    else:
                        while tag & bool(menu[choice][choice1][choice2]):
                            print('\n%s的三级目录为：' % choice2)
                            for key3 in menu[choice][choice1][choice2]:  # 打印商品三级目录
                                print(key3)
                            choice3 = input('输入 b 返回上级菜单\n输入 q 退出程序\n请输入: ').strip()  # 选择下一步操作
                            if choice3 == 'q':
                                tag = False
                            elif choice3 == 'b':
                                break
                            elif choice2 not in menu[choice][choice1]:
                                print('输入有误，请重新输入')
                                continue
                        else:
                            if not bool(menu[choice][choice1][choice2]):
                                print('\n%s的三级目录为空' % choice2)
                            tag = False                
                else:
                    if not bool(menu[choice][choice1]):
                        print('\n%s的二级目录为空' % choice1)
                        tag = False
        else:
            if not bool(menu[choice]):
                print('\n%s的一级目录为空' % choice)
                tag = False