# 注意事項
図についてはローカルで作成して、markdownセルで挿入します。

# 要求
グラフや図を挿入したい。

markdownセルの解説や、あるいはコードセル、コードの実行結果などについて、
図やグラフで解説したらわかりやすいものを5つ探す。
その5つについて図やグラフを作成する。可視化してわかりやすくするということだね。
抽象的なイメージ図ではないことに注意する。

- 後からの編集が容易なSVG図を優先する。PNGでしか作成できない場合は、PNGでも良い。
- 国際化を意識する
- 日本語のキャプションは避ける。文字化けするから。
- 英語のキャプションもなるべく記号メインにしたり、簡単な英単語に寄せてたりする。

ローカルで図を作成したら、colabでもレンダリングできるように、Github上に画像だけをpushして。
それ以外はコンフリクトが発生するのでpushしない。
なお、githubの認証が必要であれば、ユーザーに認証を求めること。

markdownセルに図を挿入する際については、github上のリモートのURLリンクを用いてください。

例:
![cross entropy overview](https://raw.githubusercontent.com/HayatoHongo/Everyones_PyTorch/main/ColabGPT/images/chapter09-cross-entropy-overview.png)
