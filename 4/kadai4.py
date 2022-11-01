"""
ファイル: kadai4.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/1(火)
内容: クラスの継承，2次元図形
"""

import datetime
import sys
from random import uniform
from Circle import Circle
from Triangle import Triangle
from Trapezoid import Trapezoid

def printMyInfo(kadai_n, kadai_name, files):
  """
  名前，学籍番号，日時，課題ファイル名を出力
  kadai_n: 課題番号
  kadai_name: 課題の内容
  files: 入力ファイルのリスト
  """

  print(f"%% {'*' * 50}")
  print(f"%% 佐藤優太, B223330")
  print(f"%% 日付: {datetime.datetime.now()}")
  print(f"%% 課題{kadai_n}: {kadai_name}")

  if len(files) == 1:
    print(f"%%入力ファイル: {files[0]}")
  else:
    for i, file in enumerate(files): print(f"%%入力ファイル{i + 1}: {file}")

  print(f"%% {'*' * 50}")

if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 2: sys.exit("Arguments are too short")

  # 図形の発生回数Nのチェック
  N = int(sys.argv[1])
  if not 2 <= N <= 20: sys.exit("The range of N must be between 2 and 20 inclusive")

  XRANGE = 580.0
  YRANGE = 700.0
  shape_list = []
  for _ in range(N):
    # 円を生成
    shape_list.append(Circle(uniform(0, 1), uniform(0, 1), uniform(0, 1), uniform(0, XRANGE), uniform(0, YRANGE), uniform(0, 0.25 * XRANGE)))

    # 三角形を生成
    shape_list.append(Triangle(uniform(0, 1), uniform(0, 1), uniform(0, 1), uniform(0, XRANGE), uniform(0, YRANGE), uniform(0, XRANGE), uniform(0, YRANGE), uniform(0, XRANGE), uniform(0, YRANGE)))

    # 台形を生成
    x1 = uniform(0, XRANGE)
    x2 = uniform(0, XRANGE)
    x3 = uniform(0, XRANGE)
    x4 = uniform(0, XRANGE)
    if x1 > x2: x1, x2 = x2, x1 # x1 < x2になるようにする
    if x3 > x4: x3, x4 = x4, x3 # x3 < x4になるようにする
    y1 = uniform(0, YRANGE)
    y3 = uniform(0, YRANGE)
    if y1 > y3: y1, y3 = y3, y1 # y1 < y2になるようにする
    shape_list.append(Trapezoid(uniform(0, 1), uniform(0, 1), uniform(0, 1), x1, y1, x2, y1, x3, y3, x4, y3))

  # ヘッダー部分を記述
  print(f"%%!PS")
  print(f"%%File: kadai4.ps")
  printMyInfo(4, "クラスの継承，2次元図形", [])

  sum_s = [0, 0, 0] # 総面積: [円, 三角形, 台形]
  sum_l = [0, 0, 0] # 総周囲長: [円, 三角形, 台形]
  for i in range(0, 3 * N, 3):
    for j in range(3):
      sum_s[j] += shape_list[i + j].area()      # 面積を求めて加算
      sum_l[j] += shape_list[i + j].perimeter() # 周囲長を求めて加算
      shape_list[i + j].ps_print()              # psファイルに記述

  # 総面積と総周囲長を記述
  print(f"%% {'*' * 30}")
  print(f"%% 円の総面積は{sum_s[0]:.1f}です")
  print(f"%% 三角形の総面積は{sum_s[1]:.1f}です")
  print(f"%% 台形の総面積は{sum_s[2]:.1f}です")
  print(f"%% {'*' * 30}")
  print(f"%% 円の総周囲長は{sum_l[0]:.1f}です")
  print(f"%% 三角形の総周囲長は{sum_l[1]:.1f}です")
  print(f"%% 台形の総周囲長は{sum_l[2]:.1f}です")
  print(f"%% {'*' * 30}")
  print("showpage")
