'''
解决八皇后问题
    如何能够再8*8的国际象棋棋盘上放置八个皇后，
    使得任何一个皇后都无法直接吃掉其他都皇后？
    (任意两个皇后不能处于同一条横行、纵行或斜线上)

'''
import copy
from operator import length_hint

chessboard = []
for i in range(1, 9):
    for j in range(1, 9):
        item = (i, j)
        chessboard.append(item)
print(chessboard)

can_place = copy.copy(chessboard)

def eight_queens():
    while True:
        new_place = yield can_place
        for item in chessboard:
            if (item[0] == new_place[0] \
            or item[1] == new_place[1] \
            or ((item[1] - item[0]) == (new_place[1] - new_place[0])) \
            or ((item[1] + item[0]) == (new_place[1] + new_place[0]))) \
            and item in can_place :
                can_place.remove(item) 
        print('本次下子位置', new_place)
        print('下次可以下子的位置为：', can_place)

queens = eight_queens()
queens.__next__()        
queens.close()

route = list()

# 没有实现退回重溯的功能
while can_place:
    can_place = copy.copy(chessboard)
    for item in can_place:
        new_place = item
        can_place2 = queens.send(item)
        route = route.append(new_place)
        if length_hint(route) < 8:
            route = list()
            continue
        else:
            print(route)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    