"""
ファイル: Circle.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/1(火)
内容: クラスの継承，2次元図形
"""

from Shape import Shape
import math

class Circle(Shape):
  """
  円クラス
  """

  def __init__(self, R, G, B, x, y, radius):
    super().__init__(R, G, B) # 色
    self.x = x                # 中心のx座標
    self.y = y                # 中心のy座標
    self.radius = radius      # 半径

  def area(self):
    s =  math.pi * self.radius ** 2
    print(f"%% 円: 面積 = {s:.1f}")
    s /= 10 ** 3
    return s

  def perimeter(self):
    l = 2 * math.pi * self.radius
    print(f"%% 円: 周囲長 = {l:.1f}")
    l /= 10 ** 3
    return l

  def ps_print(self):
    super().ps_print()
    print("newpath")
    print(f"{self.x:.1f} {self.y:.1f} {self.radius:.1f} 0 360 arc")
    print("stroke\n")
