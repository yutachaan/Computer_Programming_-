"""
ファイル: kadai6.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/15(火)
内容: matplotlibを用いたYeastデータの散布図の作成
"""

import csv
import sys
import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as mc

plt.rcParams['font.family'] = 'Hiragino sans' # 日本語のフォントを設定

class Yeast:
  """
  酵母データクラス
  """

  def __init__(self, name, MCG, GVH, ALM, MIT, ERL, POX, VAC, NUC, sp):
    self.name = name # シーケンス名
    self.MCG = MCG   # McGeogh法
    self.GVH = GVH   # von Heijne法
    self.ALM = ALM   # ALOM膜のスコア
    self.MIT = MIT   # 真・非ミトコンドリアタンパク質に関するアミノ酸解析スコア
    self.ERL = ERL   # HDEL部分裂の存在
    self.POX = POX   # ペルオキシソームに関する信号
    self.VAC = VAC   # 液胞または細胞内タンパク質のアミノ酸解析スコア
    self.NUC = NUC   # 核または非核タンパク質の核局所化信号スコア
    self.sp = sp     # 10種類の酵母クラス(CYT, NUC, MIT, ME3, ME2, ME1, EXC, VAC, POX, ERL)


def extractClass(typ, data):
  """
  酵母データから，指定された酵母クラスの属性の値のみを抽出し，リストにして返す
  typ: 取り出す酵母クラスの属性
  data: 酵母データ
  """

  ext_list = []
  if   typ == "MCG":
    for row in data: ext_list.append(row.MCG)
  elif typ == "GVH":
    for row in data: ext_list.append(row.GVH)
  elif typ == "ALM":
    for row in data: ext_list.append(row.ALM)
  elif typ == "MIT":
    for row in data: ext_list.append(row.MIT)
  elif typ == "NUC":
    for row in data: ext_list.append(row.NUC)

  return ext_list


def getLabelNum(data):
  """
  酵母データの10種類の酵母クラスの値ごとに，0〜9の番号をそれぞれ割り当て，リストにして返す(カラーマップのインデックス番号として利用)
  data: 酵母データ
  """

  label_num = []
  for row in data:
    if   row.sp == "CYT": label_num.append(0)
    elif row.sp == "NUC": label_num.append(1)
    elif row.sp == "MIT": label_num.append(2)
    elif row.sp == "ME3": label_num.append(3)
    elif row.sp == "ME2": label_num.append(4)
    elif row.sp == "ME1": label_num.append(5)
    elif row.sp == "EXC": label_num.append(6)
    elif row.sp == "VAC": label_num.append(7)
    elif row.sp == "POX": label_num.append(8)
    elif row.sp == "ERL": label_num.append(9)

  return label_num


if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 3: sys.exit("Arguments are too short")

  use_type = ["MCG", "GVH", "ALM", "MIT", "NUC"] # 使用する酵母クラスの属性
  X = sys.argv[1] # X軸にとる属性
  Y = sys.argv[2] # Y軸にとる属性

  # XとYがuse_typeに含まれていない場合終了
  if X not in use_type: sys.exit("Give an appropriate yeast class to the argument X.")
  if Y not in use_type: sys.exit("Give an appropriate yeast class to the argument Y.")

  # XとYが同じ場合終了
  if X == Y: sys.exit("Give different classes to argument X and argument Y.")

  yeast_data = [] # 酵母データ
  with open("yeast.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
      yeast_data.append(Yeast(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), row[9]))

  # 酵母データから酵母クラスがXとYのものだけ取り出す
  xdata = extractClass(X, yeast_data)
  ydata = extractClass(Y, yeast_data)

  # 酵母クラスの値からラベル番号を決定
  label_num = getLabelNum(yeast_data)

  # 10種類の酵母クラスのIDと，それに対する色
  species = ["CYT", "NUC", "MIT", "ME3", "ME2", "ME1", "EXC", "VAC", "POX", "ERL"]
  colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]

  # プロットとファイル保存
  fig = plt.figure(figsize=(10, 10))
  ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])
  scatter = plt.scatter(xdata, ydata, c=label_num, s=5, cmap=mc.ListedColormap(colors))
  handles, c = scatter.legend_elements(prop="colors")
  ax.legend(handles, species, loc='best')
  plt.xlabel(X, fontsize=20)
  plt.ylabel(Y, fontsize=20)
  plt.title(f"散布図(Yeast): 佐藤優太 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", fontsize=20)
  plt.savefig(f"kadai6-yeast-plot_X_{X}_Y_{Y}.pdf")
  plt.show()
