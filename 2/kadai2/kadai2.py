"""
ファイル: kadai2.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/10/18(火)
内容: NumPy配列と関数 (画像NumPyファイルの処理)
"""

import datetime
import numpy as np
import math
import sys
from genericpath import exists


def printMyInfo(kadai_n, kadai_name, files):
  """
  名前，学籍番号，日時，課題ファイル名を出力
  kadai_n: 課題番号
  kadai_name: 課題の内容
  files: 入力ファイルのリスト
  """

  print("*" * 50)
  print("佐藤優太, B223330")
  print(f"日付: {datetime.datetime.now()}")
  print(f"課題{kadai_n}: {kadai_name}")

  if len(files) == 1:
    print(f"入力ファイル: {files[0]}")
  else:
    for i, file in enumerate(files): print(f"入力ファイル{i + 1}: {file}")

  print("*" * 50)


def average_RGB(image, x0, y0, h, w):
  """
  imageの(x0, y0)から縦幅h，横幅wの範囲のRGB値の平均値を計算して返す
  image: カラー画像(ndarray)
  x0, y0: 開始位置の座標
  h: 縦幅
  w: 横幅
  """

  average = np.zeros(3) # RGB値の平均値を格納
  for x in range(x0, x0 + h):
    for y in range(y0, y0 + w):
      average = np.add(average, image[x][y])
  average /= (h * w)

  return average


def Euclid(a, b):
  """
  3要素のndarray配列a, bのユークリッド距離を求める
  a, b: 3要素のndarray配列
  """

  # 引数がndarrayでない場合終了
  if not isinstance(a, np.ndarray): sys.exit("Argument 'a' must be a type ndarray")
  if not isinstance(b, np.ndarray): sys.exit("Argument 'b' must be a type ndarray")

  # 引数のndarrayの要素数が3でない場合終了
  if len(a) != 3: sys.exit("Argument 'a' must have exactly 3 elements")
  if len(b) != 3: sys.exit("Argument 'b' must have exactly 3 elements")

  # ユークリッド距離を計算
  d = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))

  return d


def FindMinMax(averageRGB):
  """
  averageRGBのavg_allと平均色が最も似ている領域のインデックスと，最も似ていない領域のインデックスを返す
  averageRGB = [avg_all, avg_LT, avg_RT, avg_LB, avg_RB, avg_CT]
  """

  # avg_allとそれ以外の要素のユークリッド距離をそれぞれ計算
  d = np.zeros(5)
  for i in range(1, 6):
    d[i - 1] = Euclid(averageRGB[0], averageRGB[i])

  # ユークリッド距離が最も小さい領域のインデックスと最も大きい領域のインデックスを取り出す
  minIndex = np.argmin(d) + 1
  maxIndex = np.argmax(d) + 1

  return minIndex, maxIndex


if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 2: sys.exit("Arguments are too short")

  # ファイルが存在しない場合終了
  if not exists(sys.argv[1]): sys.exit("File does not exist")

  file_name = sys.argv[1]
  printMyInfo(2, "NumPy配列と関数 (画像NumPyファイルの処理)", [])

  image = np.load(file_name) # 画像ファイルをロード
  h = image.shape[0] # 画像の高さ
  w = image.shape[1] # 画像の幅

  print(f"ファイル名: {file_name}")
  print(f"サイズ: 高さ = {h}, 幅 = {w}")

  avg_all = average_RGB(image,      0,      0,      h,      w)
  avg_LT  = average_RGB(image,      0,      0, h // 2, w // 2)
  avg_RT  = average_RGB(image,      0, w // 2, h // 2, w // 2)
  avg_LB  = average_RGB(image, h // 2,      0, h // 2, w // 2)
  avg_RB  = average_RGB(image, h // 2, w // 2, h // 2, w // 2)
  avg_CT  = average_RGB(image, h // 4, w // 4, h // 2, w // 2)

  averageRGB = np.array([avg_all, avg_LT, avg_RT, avg_LB, avg_RB, avg_CT])
  minIndex, maxIndex = FindMinMax(averageRGB)

  print(f"全体の平均色 = ({avg_all[0]:.3f}, {avg_all[1]:.3f}, {avg_all[2]:.3f})")

  area_name = ["Left Top", "Right Top", "Left Bottom", "Right Bottom", "Central"]

  print(f"平均色がもっとも全体に近い領域は，{area_name[minIndex - 1]}領域")
  if minIndex == 1:
    print(f"その平均色 = ({avg_LT[0]:.3f}, {avg_LT[1]:.3f}, {avg_LT[2]:.3f})")
  elif minIndex == 2:
    print(f"その平均色 = ({avg_RT[0]:.3f}, {avg_RT[1]:.3f}, {avg_RT[2]:.3f})")
  elif minIndex == 3:
    print(f"その平均色 = ({avg_LB[0]:.3f}, {avg_LB[1]:.3f}, {avg_LB[2]:.3f})")
  elif minIndex == 4:
    print(f"その平均色 = ({avg_RB[0]:.3f}, {avg_RB[1]:.3f}, {avg_RB[2]:.3f})")
  elif minIndex == 5:
    print(f"その平均色 = ({avg_CT[0]:.3f}, {avg_CT[1]:.3f}, {avg_CT[2]:.3f})")

  print(f"平均色がもっとも全体と異なる領域は，{area_name[maxIndex - 1]}領域")
  if maxIndex == 1:
    print(f"その平均色 = ({avg_LT[0]:.3f}, {avg_LT[1]:.3f}, {avg_LT[2]:.3f})")
  elif maxIndex == 2:
    print(f"その平均色 = ({avg_RT[0]:.3f}, {avg_RT[1]:.3f}, {avg_RT[2]:.3f})")
  elif maxIndex == 3:
    print(f"その平均色 = ({avg_LB[0]:.3f}, {avg_LB[1]:.3f}, {avg_LB[2]:.3f})")
  elif maxIndex == 4:
    print(f"その平均色 = ({avg_RB[0]:.3f}, {avg_RB[1]:.3f}, {avg_RB[2]:.3f})")
  elif maxIndex == 5:
    print(f"その平均色 = ({avg_CT[0]:.3f}, {avg_CT[1]:.3f}, {avg_CT[2]:.3f})")
