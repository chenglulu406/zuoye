import math
def jx():
    width = input('矩形宽=？')
    length = input("矩形长=？")
    area2=width * length
    return area2
    def zjsjx():
    width = input('直角三角形直角边1=？')
    length = input("直角三角形直角边2=？")
    area4=width * length / 2.0
    return area4
    def yx():    
    r = input("圆的半径=？")
    area1 = 3.14 * r ** 2
    return area1
    def pxsbx():
    width = input('平行四边形底=？')
    length = input("平行四边形高=？")
    area3=width * length
    return area3
    def dbsjx():
    a = input('等边三角形边长=？')
    from math import sqrt
    b = sqrt((a*a)-(a/2)**2)
    area5=0.5 * a * b
    return area5
    def ty():
    a = input('椭圆半长轴=？')
    b = input("椭圆半短轴=？")
    area6=math.pi*a*b
    return are                                                                                                               
    print '图形列表[1.圆,2.矩形(正方形)，3.平行四边形，4.直角三角形，5.等边三角形,6.椭圆]'                                                                                                                    
    print '请依照列表输入各图形尺寸'
    m=jx()+zjsjx()+yx()+px                                                                                                                    
    sbx()+dbsjx()+ty()                                                                                                                    
    print '总面积%s' %(m)                                                                                                                     
    print '平均面积%s'%(m/6)                                                                                                                   
                                                                                                                      
                                                                                                                        
