#!/usr/bin/env python3

# ================= 代码实现开始 =================

''' 请在这里定义你需要的全局变量 '''
ans, allone = 0, 0

# 一个n×n的棋盘，在棋盘上摆n个皇后，求满足任意两个皇后不能在同一行、同一列或同一斜线上的方案数
# n：上述n
# 返回值：方案数
def dfs

def getAnswer(n):
    global ans, allone
    ans = 0
    allone = (1 << n) - 1
    dfs(0, 0, 0)
    return ans
    
    ''' 请在这里设计你的算法 '''

# ================= 代码实现结束 =================

print(getAnswer(int(input())))