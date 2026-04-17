2. 擬似サンプル入力

ステップ1で作ったセル群について、未定義の変数・config・ハイパーパラメータに「教材用の擬似サンプル値」を与えてください。

- configについては、configインスタンスを最初に作成するものとする。
- if/elseの条件分岐がある場合、条件分岐ごとに適切な値を与える。
- if/elseの条件分岐に関連したサンプル値については、条件分岐のmarkdownセルの直前に、どういうケースかを示すmarkdownセルおよびサンプル値を定義するコードセルを追加する。

# 例

## 例1

元のセル
```markdown
#### 現在の学習ステップが、線形ウォーミングアップ段階にある場合
CODE: `if current_step < warmup_steps:`
```

```python
warmup_progress_ratio = current_step / warmup_steps
```

期待される形

```markdown
#### ▼ 直線ウォーミングアップ段階のケースのサンプル値
```

```python
# 直線ウォーミングアップ段階でのサンプル値
current_step = 500

```

```markdown
#### 現在の学習ステップが、線形ウォーミングアップ段階にある場合
CODE: `if current_step < warmup_steps:`
```


```python
warmup_progress_ratio = current_step / warmup_steps
```

## 例2


元のセル
```python
max_learning_rate = config.max_learning_rate
```

```python
min_learning_rate = config.min_learning_rate
```

期待されるセル

Config
```python
class Config:
   Max_learning_rate = 2e-4
   min_learning_rate = 2e-5 
```

```python
config = Config()
```

```python
max_learning_rate = config.max_learning_rate
```

```python
min_learning_rate = config.min_learning_rate
```
