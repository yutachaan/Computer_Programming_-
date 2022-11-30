"""
ファイル: kadai7.py
作者: 佐藤優太
学籍番号: B223330
作成日付: 2022/11/30(水)
内容: 文書ベクトルの類似度を用いた文書検索
"""

import numpy as np
import datetime
import time
import random

class News:
  def __init__(self, number, subject, classId, feature):
    self.number     = number  # ニュースの番号
    self.subject    = subject # 文書タイトル
    self.classId    = classId # 属するクラス
    self.feature    = feature # 特徴量ベクトル
    self.similarity = 0       # コサイン類似度

  def Similarity(self, y):
    """
    コサイン類似度を求める
    y: self.featureとのコサイン類似度を求める特徴量ベクトル
    """

    x2 = 0
    y2 = 0
    xy = 0
    for i in range(len(self.feature)):
      x2 += self.feature[i] ** 2
      y2 += y[i] ** 2
      xy += self.feature[i] * y[i]

    self.similarity = xy / np.sqrt(x2 * y2)


def printMyInfo(kadai_n, kadai_name, files):
  """
  名前，学籍番号，日時，課題ファイル名を出力
  kadai_n: 課題番号
  kadai_name: 課題の内容
  files: 入力ファイルのリスト
  """

  print('*' * 50)
  print(f"佐藤優太, B223330")
  print(f"日付: {datetime.datetime.now()}")
  print(f"課題{kadai_n}: {kadai_name}")

  if len(files) == 1:
    print(f"入力ファイル: {files[0]}")
  else:
    for i, file in enumerate(files): print(f"入力ファイル{i + 1}: {file}")

  print('*' * 50)


def out_res(query_news, news_list):
  """
  ある一つのクエリと検索対象データセットとのコサイン類似度を計算し，クエリの番号・文書タイトル・属するクラスと，それに類似する上位10個の文書タイトル・コサイン類似度・属するクラスを出力
  上位10文書にクエリ文書のクラスと同じクラスが含まれている割合を出力
  query_news: クエリ
  news_list: 検索対象データセット
  """

  # 検索対象データセットの各ニュースとクエリのコサイン類似度を計算
  for news in news_list: news.Similarity(query_news.feature)

  # 検索対象データセットをコサイン類似度でソート
  news_list.sort(reverse=True, key=lambda x: x.similarity)

  # 類似度上位10文書のうちクエリと同じクラスの数をカウント
  count = 0
  for i in range(10):
    if query_news.classId == news_list[i].classId: count += 1

  # 結果を出力
  print(f"QueryID={query_news.number} class=[{query_news.classId}] {query_news.subject}")
  print("-" * 50)
  for i in range(10):
    print(f"Rank{i + 1}({news_list[i].number}) {news_list[i].similarity:.3f} {news_list[i].subject} class=[{news_list[i].classId}]")
  print(f"クエリと同じクラスがランク10位までに見つかった割合 = {(count * 10):.1f}%")
  print(f"{'*' * 50}\n\n")


if __name__ == "__main__":
  # 乱数の初期値を現在時刻とする
  random.seed(time.time())

  # 各ファイルを読み込む
  news_feature = np.load("20news2000.npy")           # 検索対象データの特徴量ベクトル
  query_news_feature = np.load("20news400query.npy") # クエリデータの特徴量ベクトル

  subject = []        # 検索対象データの文書タイトル
  with open("Subject.txt") as f:
    subject = [s.strip() for s in f.readlines()]

  query_subject = []  # クエリデータの文書タイトル
  with open("QuerySubject.txt") as f:
    query_subject = [s.strip() for s in f.readlines()]

  class_id = []       # 検索対象データの属するクラス
  with open("ClassId.txt") as f:
    class_id = [int(s.strip()) for s in f.readlines()]

  query_class_id = [] # クエリデータの属するクラス
  with open("QueryClassId.txt") as f:
    query_class_id = [int(s.strip()) for s in f.readlines()]

  # 検索対象データをNewsクラスの値として格納
  news_list = []
  for i in range(news_feature.shape[0]):
    news_list.append(News(i, subject[i], class_id[i], news_feature[i]))

  # クエリデータをNewsクラスの値として格納
  query_news_list = []
  for i in range(query_news_feature.shape[0]):
    query_news_list.append(News(i, query_subject[i], query_class_id[i], query_news_feature[i]))

  # クエリIDをランダムに5つ生成
  query_id_set = []
  while True:
    for _ in range(5):
      query_id_set.append(random.randint(0, 399))
    class_id_query_id_set = [query_news_list[x].classId for x in query_id_set]

    # クエリIDが重複している場合や，すべてのクエリのクラスが同じ場合はもう一度生成し直す
    if len(query_id_set) == len(set(query_id_set)) and len(set(class_id_query_id_set)) > 1: break

    query_id_set = []

  printMyInfo(7, "文書ベクトルの類似度を用いた文書検索", [])

  # 各クエリIDに対して結果を出力
  for x in query_id_set: out_res(query_news_list[x], news_list)
