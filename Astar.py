"""
Astar 算法
"""

import numpy as np
from mapping import Map
import matplotlib.pyplot as plt

def AStar(width=100,height=100,start=(4,4),end=(95,95)):
    width=width
    height=height
    Mymap=Map(width,height,mapping=True)
    maps=Mymap.getMap()
    star={'位置':start,'代价':700,'父节点':start}#起点
    end={'位置':end,'代价':0,'父节点':end}#终点

    openlist=[]#open列表，存储可能路径
    closelist=[star]#close列表，已走过路径
    step_size=3#搜索步长。
    #步长太小，搜索速度就太慢。步长太大，可能直接跳过障碍，得到错误的路径
    #步长大小要大于图像中最小障碍物宽度
    # 可能运动的四个方向增量 上 下 左 右
    add=([0,step_size],[0,-step_size],[step_size,0],[-step_size,0],)
    while 1:
        s_point=closelist[-1]['位置']#获取close列表最后一个点位置，S点
        # 添加可探索的四个位置
        for i in range(len(add)):
            x=s_point[0]+add[i][0]#检索超出图像大小范围则跳过
            if x<0 or x>=width:
                continue
            y=s_point[1]+add[i][1]
            if y<0 or y>=height:#检索超出图像大小范围则跳过
                continue
            G=abs(x-star['位置'][0])+abs(y-star['位置'][1])#计算代价
            H=abs(x-end['位置'][0])+abs(y-end['位置'][1])#计算代价
            F=G+H
            if H<20:#当逐渐靠近终点时，搜索的步长变小
                step_size=1
            addpoint={'位置':(x,y),'代价':F,'父节点' :s_point}#更新位置
            count=0
            for i in openlist:
                if i['位置']==addpoint['位置']:
                    count+=1
            for i in closelist:
                if i['位置']==addpoint['位置']:
                    count+=1
            if count==0:#新增点不在open和close列表中
                if maps[y,x]!=1:#非障碍物 
                        openlist.append(addpoint)
        
        t_point={'位置':(-1,-1),'代价':10000,'父节点':(-1,-1)}
        # 寻找代价最小点作为下一个探索的点
        for j in range(len(openlist)):
            if openlist[j]['代价']<t_point['代价']:
                t_point=openlist[j]
        for j in range(len(openlist)):#在open列表中删除t点
            if t_point==openlist[j]:
                openlist.pop(j)
                break
        # 在close列表中加入t点
        closelist.append(t_point)
        if t_point['位置']==end['位置']:#找到终点！！
            print("找到终点")
            break
    print(closelist)
    
    # 逆向搜索找到路径 ？？？
    road=[]
    road.append(closelist[-1])
    point=road[-1]
   
    while 1:
        for i in closelist:
            if i['位置']==point['父节点']:#找到父节点
                point=i
                road.append(point)
        if point==star:
            print("路径搜索完成")
            break
    # 绘制路径
    x=[i['位置'][0] for i in road]
    y=[i['位置'][1] for i in road]
    plt.scatter([x[0],x[-1]],[y[0],y[-1]],c="red")
    plt.plot(x,y)
    Mymap.display()

if __name__ == "__main__":
    AStar()

        
 