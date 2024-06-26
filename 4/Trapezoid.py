"""
ファイル: Trapezoid.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/1(火)
内容: クラスの継承，2次元図形
"""

from Shape import Shape
import math

class Trapezoid(Shape):
  """
  台形クラス
  """

  def __init__(self, R, G, B, x1, y1, x2, y2, x3, y3, x4, y4):
    super().__init__(R, G, B) #色

    # 4頂点の座標
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.x3 = x3
    self.y3 = y3
    self.x4 = x4
    self.y4 = y4

  def area(self):
    s =  ((self.x2 - self.x1) + (self.x4 - self.x3)) * (self.y3 - self.y1) / 2
    print(f"%% 台形: 面積 = {s:.1f}")
    s /= 10 ** 3
    return s

  def perimeter(self):
    # 各線分の長さを求める
    d1 = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
    d2 = math.sqrt((self.x2 - self.x4) ** 2 + (self.y2 - self.y4) ** 2)
    d3 = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
    d4 = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)

    # 周囲長を求める
    l = d1 + d2 + d3 + d4
    print(f"%% 台形: 周囲長 = {l:.1f}")
    l /= 10 ** 3
    return l

  def ps_print(self):
    super().ps_print()
    print("newpath")
    print(f"{self.x1:.1f} {self.y1:.1f} moveto")
    print(f"{self.x2:.1f} {self.y2:.1f} lineto")
    print(f"{self.x4:.1f} {self.y4:.1f} lineto")
    print(f"{self.x3:.1f} {self.y3:.1f} lineto")
    print("closepath")
    print("stroke\n")
