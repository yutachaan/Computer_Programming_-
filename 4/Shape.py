"""
ファイル: Shape.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/1(火)
内容: クラスの継承，2次元図形
"""

class Shape:
  """
  2次元図形クラス
  """

  def __init__(self, R, G, B):
    # 色
    self.R = R
    self.G = G
    self.B = B

  def area(self): pass      # 面積を求める
  def perimeter(self): pass # 周囲長を求める

  def ps_print(self):
    """
    psファイルに色の情報を記述
    """
    print(f"%% 色:")
    print(f"{self.R:.1f} {self.G:.1f} {self.B:.1f} setrgbcolor")
