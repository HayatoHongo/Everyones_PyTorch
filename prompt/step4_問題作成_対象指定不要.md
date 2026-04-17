Step3で作成したコードセルについて
markdown形式の解説
コード穴埋め問題
を作成してください。

以下の形式に該当する場合に限り、問題を作成します。
- 該当しない場合は、問題を作成しません。
- 1つのコードセルに対して、問題は1つのみとします。
- markdownセルは新規で作成します。
- コードセルは既存のセルに # TODO を追記します。
- 解説は簡潔さと分かりやすさを両立します。
- print文は削除しないでください。

形式
出力 = インスタンス.メソッド(引数)
出力 = 関数(引数)
インスタンス = クラス(引数)
新しい変数 = 古い変数.メソッド(引数)
四則演算を含む式: 出力 = 式
例1:
入力コードセル
```python
torch.manual_seed(123)
bias_embedding_table = nn.Embedding(num_relative_positions, 1)
```

出力するmarkdownセルとコードセル
```markdown
```python
インスタンス: 相対位置を表す整数（インデックス）を入力として、それぞれに対応するバイアス（1次元ベクトル）を返す埋め込みテーブル
クラス: nn.Embedding
引数: 入力次元, 出力次元
```
```
```python
torch.manual_seed(123)
bias_embedding_table = nn.Embedding(num_relative_positions, 1) # TODO: インスタンス = クラス(引数)
```


例2

入力コードセル

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size = 0.2, random_state = 42) 
```

出力するmarkdownセルとコードセル
```markdown
```python
出力:  X_train, X_test, y_train, y_test（説明/目的変数のデータのtrain/testペア）
関数: train_test_split
引数: X（説明変数のデータ）, y（目的変数のデータ）,  test_size=0.2, random_state=42
```
```

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size = 0.2, random_state = 42)  # TODO: 出力 = 関数(引数)
```

例3

入力コードセル
```python
label_embed_linear = label_embedding(label_one_hot)  # (B,10) → (B,16)
print_formatted_tensor("label_embed_linear", label_embed_linear)
```

出力されるmarkdownセルとコードセル

```markdown
```python
出力: label_embed_linear（ラベル埋め込みテンソル）
インスタンス: label_embedding
メソッド: forward（省略可能）
引数: label_one_hot
```
- `label_embedding`レイヤーに `label_one_hot`を入力して、順伝播した出力を得る。
-  テンソルの形状は(B, 10)から(B, 16)に変化する。
```

```python
label_embed_linear = label_embedding.forward(label_one_hot) # TODO: 出力 = インスタンス.メソッド(引数)
print_formatted_tensor("label_embed_linear", label_embed_linear)
```

例4
入力コードセル
```python
config = Config()
```



```markdown
```python 
インスタンス: config （学習率の最大値・最小値、ウォームアップステップ数などの設定値）
クラス: Config
引数: デフォルト値（なし）
```
```python
config = Config() # TODO: インスタンス = クラス(引数)
```

例5
元のコードセル
```python
cosine_decay_ratio = 0.5 * (1.0 + cosine_decay_value)
```

出力されるmarkdownセルとコードセル
```markdown
```python
出力: cosine_decay_ratio（コサイン減衰スケジュールの進捗率）
式: 0.5 * (1.0 + cosine_decay_value)
```
- `cosine_decay_value` は通常 `cos()` によって得られる -1〜1 の値になります。
- その値を 0.5 * (1 + x) の形で変換することで、範囲を 0〜1 にスケーリングしています。
```

```python
cosine_decay_ratio = 0.5 * (1.0 + cosine_decay_value) # TODO: 出力 = 式
print(“cosine_decay_ratio”, cosine_decay_ratio)
```
