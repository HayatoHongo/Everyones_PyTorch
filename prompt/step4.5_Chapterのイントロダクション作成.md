チャプター番号について、ファイル名を参考にしながら、タイトルとして一番先頭につける。

また、コードセルの中に、NEWやDELETEで、前回との差分を可視化したコードセル（差分セル（NEW／DELETE））があるので、
これを参考にして、ファイル全体のイントロダクションを作成する。


例: ファイル名 ColabGPT_Chapter09_交差エントロピー.ipynb

# **Chapter 9: 交差エントロピー**

## スコアから確率分布へ

前回までは、1つの数字画像に対して、  
『1らしさ』『2らしさ』…『9らしさ』といった10個のスコアを出し、  
最も大きいスコアのクラスに分類してきました。

10クラスに分類するなら、モデルにはスコアではなく、  
各クラスに属する確率を出してほしいところです。  
たとえば、『1である確率』『2である確率』…『9である確率』を出力します。  
これら10個の確率を並べたものが、確率分布です。

次回以降のChapterでは、モデルがスコアではなく、確率分布を出力するようになります。  
学習では、モデルが出力した確率分布を、正解の確率分布に近づけていきます。

言い換えると、モデルの予測する確率分布と、正解の確率分布のずれを小さくしていくわけです。

では、確率分布どうしのずれを、どのように数値で表せばよいのでしょうか？

Chapter 9では、このずれを定量化するための指標である、交差エントロピーを紹介します。

---

参照したコードセル

```python
# 勾配の式を自分で書くのをやめて、PyTorchに自動計算してもらう
# loss.backward() の登場！
import torch

data = torch.load("mnist_7x7_shuffled.pt")
X = data["X"]
Y = data["Y"]

########## NEW ##########
# requires_grad=True にすると、PyTorchがWの勾配を追跡してくれる
W = torch.zeros(49, 10, requires_grad=True)
########## NEW ##########
"""DELETE
W = torch.zeros(49, 10)
"""

lr = 1.0

num_epochs = 1000
for epoch in range(num_epochs):

    # 予測する
    Y_pred = X @ W

    # 損失を計算する
    Y_prob = torch.softmax(Y_pred, dim=1)
    loss = torch.mean(torch.sum(-Y * torch.log(Y_prob), dim=1))

    ########## NEW ##########
    # 勾配をすべて None でリセット
    # この処理は毎回必要
    W.grad = None
    ########## NEW ##########

    ########## NEW ##########
    # 勾配計算を自分で書く代わりに、
    # lossから逆向きにたどって勾配を自動計算してもらう
    # 結果は W.grad に入る
    loss.backward()
    ########## NEW ##########

    """DELETE
    Total_grad = X.T @ (Y_prob - Y)
    Mean_grad = Total_grad / 1000
    """

    ########## NEW ##########
    # 重みを更新する
    # （勾配の追跡を一時停止して、Wの値だけを書き換える）
    with torch.no_grad():
        W -= lr * W.grad
    ########## NEW ##########

    """DELETE
    # 重みを更新する
    W = W - lr * Mean_grad
    """

    print("epoch", epoch, "loss", loss)
```


