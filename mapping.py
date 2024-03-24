# 使用栅格地图
import numpy as np
import matplotlib.pyplot as plt

"""
创建栅格地图
0-代表可以通行 1-代表障碍物
"""

class Map:
    def __init__(self,width,height,mapping=False,show=False,ticks=False):
        # 地图的宽度和长度
        self.width=width
        self.height=height
        # 创建一个空白的地图
        self.grid=np.zeros((self.height,self.width),dtype=int)

        # 是否显示网格
        self.show=show
        # 是否显示网格的刻度
        self.ticks=ticks
        if mapping:
            self.base_map()

    # 添加障碍物
    def add_obstacle(self,*args):
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
        
    
    def base_map(self):
        self.add_obstacle((0,100), (99,100))
        self.add_obstacle((0,100), (0,1))
        self.add_obstacle((0,1), (0,100))
        self.add_obstacle((99,100), (0,100))

        self.add_obstacle((18,23),(0,40))
        self.add_obstacle((88,83),(0,45))
        self.add_obstacle((58,63),(55,100))
        self.add_obstacle((84,100),(84,88))
        self.add_obstacle((34,39),(30,70))

    def add_path(self,path):
        for p in path:
            x0,y0=p
            self.grid[x0][y0]=0.3


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
    Mymap = Map(100, 100,mapping=True)



    # 添加一些障碍物 多个点一次性添加
    # Mymap.add_obstacle((0,100), (99,100))
    # Mymap.add_obstacle((0,100), (0,1))
    # Mymap.add_obstacle((0,1), (0,100))
    # Mymap.add_obstacle((99,100), (0,100))

    # Mymap.add_obstacle((20,21),(0,40))
    # Mymap.add_obstacle((80,81),(0,45))
    # Mymap.add_obstacle((59,60),(55,100))
    # Mymap.add_obstacle((88,100),(85,86))
    # Mymap.add_obstacle((37,38),(30,70))

    mapMsg=Mymap.getMap()
    print(mapMsg)

    # 显示地图
    Mymap.display()

