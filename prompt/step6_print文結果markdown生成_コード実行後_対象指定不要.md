print 文が含まれるセルについて、その正しい結果を記載する。
なお、すでにファイルはコード実行済みであるため、出力をそのまま参照すること。特に環境を作成して実行する必要はない。
保存されている実行出力を読み取り、その直後に「Check Point」用のMarkdownセル（例の形式）を自動挿入します。
絶対に自分でコードを実行してはいけません。
例をもとにすること。


例えば、print(\"max_learning_rate\", max_learning_rate)の実行結果は以下のように、"outputs"の"text"の中に保存されている。0.0002

```
{
   "cell_type": "code",
   "execution_count": 36,
   "id": "920b20f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "max_learning_rate 0.0002\n"
     ]
    }
   ],
   "source": [
    "print(\"max_learning_rate\", max_learning_rate)"
   ]
  },
```

# 例

例1: 通常の変数の場合

対象コードセル
```python
max_learning_rate = config.max_learning_rate
print("max_learning_rate", max_learning_rate)
```

出力markdownセル
```markdown
**`Check Point`** <label><input type="checkbox">max_learning_rate 0.001<label>
```


例2: テンソルの場合

対象コードセル
```python
# Attentionスコアを計算中 (QK^T) / sqrt(embedding_dim)
attention_weights_before_mask = # TODO: THINK_BY_YOURSELF
print_formatted_tensor("attention_weights_before_mask", attention_weights_before_mask)
```

出力markdownセル
```markdown
**`Check Point`**
<label><input type="checkbox">↓以下と答えが一致したらチェックをつける</label>


```
attention_weights_before_mask
Tensor Size: [1, 3, 3]
tensor([
        [
          [ -0.16,   0.09,   0.27],
          [ -0.61,   0.32,   0.69],
          [ -0.15,   0.08,   0.05]
        ]
      ])
```
```
