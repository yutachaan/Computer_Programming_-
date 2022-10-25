"""
ファイル: kadai3.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/10/25(火)
内容: RS_tarin.csvから単回帰クラスを作成し学習，その後，RS_test.csvを読み込み，単位面積価格を予測
"""

import datetime
import sys
from genericpath import exists
import csv

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


class RealEstate:
  """
  不動産クラス
  """

  def __init__(self, id, howOld, howFar, value):
    self.id = id         # 物件番号
    self.howOld = howOld # 築年数
    self.howFar = howFar # 最寄駅からの距離
    self.value = value   # 単位面積あたりの価格


class Regression:
  """
  回帰クラス
  """

  def __init__(self, xlist, ylist):
    self.a = 0.0              # 係数
    self.b = 0.0              # 係数
    self.R2 = 0.0             # 寄与率
    self.xm = 0.0             # 説明変数の平均値
    self.ym = 0.0             # 目的変数の平均値
    self.xlist = xlist        # 説明変数データ
    self.ylist = ylist        # 目的変数データ
    self.samples = len(xlist) # データのサンプル数

  def compMean(self):
    """
    xlistとylistからxmとymを計算
    """

    for x in self.xlist: self.xm += x
    self.xm /= self.samples

    for y in self.ylist: self.ym += y
    self.ym /= self.samples

  def doRegression(self):
    """
    単回帰を計算し，predicted, a, b, R2を計算
    """

    self.compMean()

    sxx = 0.0
    syy = 0.0
    sxy = 0.0
    pym = 0.0
    sypy = 0.0
    spypy = 0.0

    for i in range(self.samples):
      sxx += (self.xlist[i] - self.xm) ** 2
      syy += (self.ylist[i] - self.ym) ** 2
      sxy += (self.xlist[i] - self.xm) * (self.ylist[i] - self.ym)

    # aとbを求める
    self.a = sxy / sxx
    self.b = self.ym - self.a * self.xm

    # predictedを求める
    predicted = []
    for i in range(self.samples):
      predicted.append(self.a * self.xlist[i] + self.b)
      pym += predicted[i]
    pym /= self.samples

    # R2の各項を求める
    for i in range(self.samples):
      spypy += (predicted[i] - pym) ** 2
      sypy += (self.ylist[i] - self.ym) * (predicted[i] - pym)

    # R2を求める
    self.R2 = (sypy ** 2) / (syy * spypy)


  def predict(self, x):
    """
    未知の説明変数データxを与えて目的変数の値を予測し返す
    x: 説明変数
    """

    return self.a * x + self.b


if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 4: sys.exit("Arguments are too short")

  # ファイルが存在しない場合終了
  if not exists(sys.argv[1]): sys.exit(f"File does not exist: {sys.argv[1]}")
  if not exists(sys.argv[2]): sys.exit(f"File does not exist: {sys.argv[2]}")

  file_train = sys.argv[1] # 訓練データファイル
  file_test = sys.argv[2]  # テストデータファイル
  mode = sys.argv[3]       # O: 築年数で予測， F: 最寄駅距離で予測

  printMyInfo(3, "RS_tarin.csvから単回帰クラスを作成し学習，その後，RS_test.csvを読み込み，単位面積価格を予測", [file_train, file_test])

  # 訓練データを読み込む
  train_data = []
  with open(file_train) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
      train_data.append(RealEstate(int(row[0]), float(row[1]), float(row[2]), float(row[3])))

  # 築年数，最寄駅距離，単位面積価格をそれぞれ別のリストとして保持
  train_howOld = [row.howOld for row in train_data]
  train_howFar = [row.howFar for row in train_data]
  train_value = [row.value for row in train_data]

  # テストデータを読み込む
  test_data = []
  with open(file_test) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
      test_data.append(RealEstate(int(row[0]), float(row[1]), float(row[2]), float(row[3])))

  if mode == "O":
    print("築年数で予測します")
    x = test_data[9].howOld
    reg = Regression(train_howOld, train_value)
    reg.doRegression()

    # yを予測し，絶対誤差を求める
    y = reg.predict(x)      # 予測値
    yt = test_data[9].value # 真値
    e = abs(y - yt)         # 絶対誤差

    print(f"a = {reg.a:.2f}")
    print(f"b = {reg.b:.2f}")
    print(f"R2 = {reg.R2:.2f}\n")
    print(f"物件番号410の単位面積価格の予測値は{y:.2f}です")
    print(f"物件番号410の単位面積価格の真値は{yt:.2f}です")
    print(f"予測値と真値の絶対誤差は{e:.2f}です\n")

  elif mode == "F":
    print("最寄駅距離で単回帰します")
    x = test_data[9].howFar
    reg = Regression(train_howFar, train_value)
    reg.doRegression()

    # yを予測し，絶対誤差を求める
    y = reg.predict(x)      # 予測値
    yt = test_data[9].value # 真値
    e = abs(y - yt)         # 絶対誤差

    print(f"a = {reg.a:.2f}")
    print(f"b = {reg.b:.2f}")
    print(f"R2 = {reg.R2:.2f}\n")
    print(f"物件番号410の単位面積価格の予測値は{y:.2f}です")
    print(f"物件番号410の単位面積価格の真値は{yt:.2f}です")
    print(f"予測値と真値の絶対誤差は{e:.2f}です\n")
