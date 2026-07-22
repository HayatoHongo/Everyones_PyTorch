ステップ2までのセル群に対して、各セルの直後に「理解促進用のprint文」を挿入してください。

ルール:
- そのセルで新しく計算されたスカラー/テンソル/配列/変数があるなら print する
- テンソルなら print_formatted_tensor(“x”, x) を使う
- スカラー/配列/変数なら、print(“x”, x) を使う
- x=10 のような、明らかな文はそのまま
- x = config.x のような、少しわかりづらい定義文にはprint文を適用する

# 例

# 例1
元のコードセル
```python
decay_step_index = current_step - warmup_steps
```

期待される応答

```python
decay_step_index = current_step - warmup_steps
print(“decay_step_index”, decay_step_index)
```

# 例2

元のコードセル
```python
current_step=500
```

期待される応答（変更しない）

```python
current_step=500
```
