# 使用栅格地图
import numpy as np
import matplotlib.pyplot as plt

"""
创建栅格地图
0-代表可以通行 1-代表障碍物
"""

class Map:
    def __init__(self,width,height,show=False,ticks=False):
        # 地图的宽度和长度
        self.width=width
        self.height=height
        # 创建一个空白的地图
        self.grid=np.zeros((self.height,self.width),dtype=int)

        # 是否显示网格
        self.show=show
        # 是否显示网格的刻度
        self.ticks=ticks

    # 添加障碍物
    def add_obstacle(self,*args):
        # print(type(args[0]))
        # print(type((1,1)))
        if type(args[0])== int:
            x=args[0]
            y=args[1]
            if 0 <= x <=self.width and 0 <= y <= self.height:
                self.grid[y][x]=1
            else:
                print("超出网格边界")
                return False
        if type(args[0]) == type((1,1)):
            x_min,x_max = args[0]
            y_min,y_max = args[1]
            if 0 <= x_min and x_max <=self.width and 0 <= y_min and y_max <= self.height:
                self.grid[y_min:y_max,x_min:x_max]=1
            else:
                print("超出网格边界")
                return False
    
    # 删除障碍物
    def delete_obstacle(self,x,y):
        
        if 0 <= x <=self.width and 0 <= y <= self.height:
            # 有障碍物时才可以删除
            if self.grid[y][x]:
                return self.grid[y][x] == 0
            else:
                print("此处没有障碍物")
        else:
            print("超出地图边界，请重新设置")
            return False
        
    
    def getMap(self):
        """用于获取地图的信息"""
        return self.grid



    # 可视化地图
    def display(self):
        plt.imshow(self.grid,cmap='binary', origin='lower')
        if self.ticks:
            plt.xticks(np.arange(0, self.width, 1))
            plt.yticks(np.arange(0, self.height, 1))
        else:
            plt.xticks([])
            plt.yticks([])

        # 是否显示网格
        if self.show:
            plt.grid(color='gray', linestyle='-', linewidth=1)
        plt.show()


if __name__=="__main__":

    # 创建一个10x10的地图
    Mymap = Map(100, 100)

    # 添加一些障碍物 多个点一次性添加
    Mymap.add_obstacle((2,3), (2,40))

    Mymap.add_obstacle((15,33), (70,71))

    # 单个点添加
    # Mymap.add_obstacle(2, 2)
    # Mymap.add_obstacle(3, 3)
    Mymap.add_obstacle(4, 4)

    mapMsg=Mymap.getMap()
    print(mapMsg)

    # 显示地图
    Mymap.display()


