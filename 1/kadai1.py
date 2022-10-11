"""
ファイル: kadai1.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/10/11(火)
内容: 日本語ニュース記事ファイルからカタカナ文字列の抽出
"""

import datetime
from genericpath import exists
import sys
import re

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


if __name__ == "__main__":
  # コマンドライン引数が足りない場合終了
  if len(sys.argv) < 2: sys.exit("Arguments are too short")

  # ファイルが存在しない場合終了
  if not exists(sys.argv[1]): sys.exit("File does not exist")

  file_name = sys.argv[1]
  printMyInfo(1, "日本語ニュースからカタカナ文字列の抽出", [file_name])

  dic = dict() # カタカナと出現頻度の辞書
  with open(file_name) as f:
    for line in f:
      words = re.findall(r'[\u30A1-\u30FF]+', line) # その行のカタカナをすべて抽出してリスト化

      # 辞書に追加
      for word in words:
        if word in dic: dic[word] += 1
        else: dic[word] = 1

  # 結果を出力
  count_all = 0 # カタカナ文字列総数
  for word, count in dic.items():
    print(f"{word} {count}")
    count_all += count
  print(f"\nカタカナ文字列総数 = {count_all}")
