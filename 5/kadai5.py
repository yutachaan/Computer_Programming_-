"""
ファイル: kadai5.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/8(火)
内容: 行列演算およびデコレータ関数利用例
"""

import datetime
import numpy as np
import sys

def printMyInfo(kadai_n, kadai_name, files):
  """
  名前，学籍番号，日時，課題ファイル名を出力
  kadai_n: 課題番号
  kadai_name: 課題の内容
  files: 入力ファイルのリスト
  """

  print(f"{'*' * 50}")
  print(f"佐藤優太, B223330")
  print(f"日付: {datetime.datetime.now()}")
  print(f"課題{kadai_n}: {kadai_name}")

  if len(files) == 1:
    print(f"入力ファイル: {files[0]}")
  else:
    for i, file in enumerate(files): print(f"入力ファイル{i + 1}: {file}")

  print(f"{'*' * 50}")

def divzero_warning(func):
  """
  行列Bの要素に0が含まれるかどうか調べるデコレータ関数
  """

  def inner(A, B):
    for row in B.mat:
      for v in row:
        if v == 0.0: return None
    return func(A, B)
  return inner

def print_matrix(A):
  """
  行列を出力
  """

  for row in A:
    print("| ", end="")
    for v in row:
      print(f"{v:.4f}", end=" ")
    print("|")


class Matrix:
  """
  行列クラス
  """

  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.mat = np.random.uniform(-10, 10, (row, col)) # row行col列で各要素が-10以上10以下の行列を生成

  def __add__(self, other):
    """
    加算の演算子オーバーロード
    """

    # サイズが異なる場合エラーを出して終了
    if self.row != other.row or self.col != other.col:
      print("The matrices must have the same size")
      return self.mat

    return self.mat + other.mat

  def __sub__(self, other):
    """
    減算の演算子オーバーロード
    """

    # サイズが異なる場合エラーを出して終了
    if self.row != other.row or self.col != other.col:
      print("The matrices must have the same size")
      return self.mat

    return self.mat - other.mat

  def __mul__(self, other):
    """
    乗算の演算子オーバーロード
    """

    # サイズが異なる場合エラーを出して終了
    if self.row != other.row or self.col != other.col:
      print("The matrices must have the same size")
      return self.mat

    return self.mat * other.mat

  @divzero_warning
  def __truediv__(self, other):
    """
    除算の演算子オーバーロード
    """

    # サイズが異なる場合エラーを出して終了
    if self.row != other.row or self.col != other.col:
      print("The matrices must have the same size")
      return self.mat

    return self.mat / other.mat


if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 4: sys.exit("Arguments are too short")

  M = int(sys.argv[1])
  N = int(sys.argv[2])
  flag = int(sys.argv[3])

  # 各値が適切でなければ終了
  if M < 3: sys.exit("The value of M must be 3 or more")
  if N >= 5: sys.exit("The value of N must be 5 or more")
  if flag != 0 and flag != 1: sys.exit("The value of flag must be 0 or 1")

  # 行列を生成
  A = Matrix(M, N)
  B = Matrix(M, N)
  if flag: B.mat[0][0] = 0

  # M, N, flag, 各行列, 各演算後の行列の値を出力
  printMyInfo(5, "行列演算およびデコレータ関数利用例", [])
  print(f"入力された値: M={M}, N={N}, flag={flag}")

  print("A:")
  print_matrix(A.mat)

  print("B:")
  print_matrix(B.mat)

  C = A + B
  print("C=A+B:")
  print_matrix(C)

  C = A - B
  print("C=A-B:")
  print_matrix(C)
  C = A * B
  print("C=A*B:")
  print_matrix(C)

  C = A / B
  print("C=A/B:")
  if C is not None: print_matrix(C)
  else: print("ZeroDivisionError")
