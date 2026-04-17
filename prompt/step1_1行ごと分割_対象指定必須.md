次の【対象となるクラスや関数】の1つの大きなコードセルを
「教育向けの小さなJupyterセル」に分割してください。

分割ルール:
1) インデントを発生させるような def/class/if/for/while/with/try はコードとして書かない。
- Markdownセルの見出しに変換する。
- class/defは ### 3つの小見出しにする。それ以外の if elseなどは #### 4つの小見出しにする。
- defであれば、~関数を定義する、if/elseであれば もしも ~ の場合　のように、わかりやすい表現を用いる。
- 元セルは残したまま、その直前にルール通りの小セル群（見出しMarkdown＋1行コードセル中心）を差し込みます。
- 解説は記載しない。
2) コードは基本的に1行=1コードセル（不可分なら最大3行まで）
3) 元コードの順序と意味を維持する（並べ替えはしない）
4) 返り値(return)はMarkdownで小見出しなしで「最終的に返す値」を説明し、コードセルでは`x` などの最終変数を“置く”だけでよい
5) 元のコードセルを削除せず、そのまま残す


# 例
import math

def get_learning_rate(current_step, config):
   max_learning_rate = config.max_learning_rate
   min_learning_rate = config.min_learning_rate
   warmup_steps = config.warmup_steps
   total_training_steps = config.total_training_steps


   if current_step < warmup_steps:
       # --- Linear Warmup ---
       warmup_progress_ratio = current_step / warmup_steps
       learning_rate = max_learning_rate * warmup_progress_ratio


   else:
       # --- Cosine Decay ---
       decay_step_index = current_step - warmup_steps
       decay_total_steps = total_training_steps - warmup_steps
       decay_progress_ratio = decay_step_index / decay_total_steps


       cosine_decay_value = math.cos(math.pi * decay_progress_ratio)
       cosine_decay_ratio = 0.5 * (1.0 + cosine_decay_value)


       learning_rate_range = max_learning_rate - min_learning_rate
       learning_rate = min_learning_rate + cosine_decay_ratio * learning_rate_range


   return learning_rate


```markdown
### 学習率を計算する関数を定義する 
CODE: `def get_learning_rate(current_step, config)`
```


import math

max_learning_rate = config.max_learning_rate

min_learning_rate = config.min_learning_rate

warmup_steps = config.warmup_steps

total_training_steps = config.total_training_steps


```markdown
#### 現在の学習ステップが、線形ウォーミングアップ段階にある場合
CODE: `if current_step < warmup_steps:`
```
warmup_progress_ratio = current_step / warmup_steps

learning_rate = max_learning_rate * warmup_progress_ratio

```markdown
#### 現在の学習ステップが、コサイン減衰段階にある場合
CODE: `else:`
```
decay_step_index = current_step - warmup_steps

decay_total_steps = total_training_steps - warmup_steps

decay_progress_ratio = decay_step_index / decay_total_steps

cosine_decay_value = math.cos(math.pi * decay_progress_ratio)

cosine_decay_ratio = 0.5 * (1.0 + cosine_decay_value)

learning_rate_range = max_learning_rate - min_learning_rate

learning_rate = min_learning_rate + cosine_decay_ratio * learning_rate_range


```markdown
最終的に返す値
CODE: `return learning_rate`
```
learning_rate
