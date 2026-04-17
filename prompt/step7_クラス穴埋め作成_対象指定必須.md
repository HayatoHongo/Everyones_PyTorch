あなたのタスクは、【対象となるクラスや関数】を定義している大きな1つのセルを特定します。そして、そのセルを「Options→穴埋めコード→答え(折りたたみ)」の3セル構成に置き換えることです。

🔘 **Options**: 余計な選択肢があるかもしれません。同じ選択肢を2回以上使うかもしれません。

`A`　`B`...

の形式にすること。

### ⚠️ 注意事項

-  穴埋めにおける _ の長さは、元のスクリプトの変数名と似たような長さにすること。短い変数名は __ 、中くらいの長さなら _______、長ければ______________、さらに長ければ ______________________
- 長すぎる穴埋めは用意しないこと。
- 等式`=`を含む行について、左側の変数については穴埋めにしないこと。右側については穴埋めにして良い。
- 余計な選択肢を追加すること。ただし、少量にとどめること。
- 禁止事項：選択肢に対して、記号や番号（例：A, B.., 1,2 ...）を併記してはいけません。
- ########## NEW ########## という範囲の記載がある場合は、その範囲の内部だけ穴埋めを作成すること。
それ以外の部分で穴埋めを作成してはいけません。
- 穴埋めを作成した行については、# TODO: FILL を必ず併記すること。
- スクリプトは全文で出力すること。
- 数字（例：0, 1, -1）の穴埋めにおける_の長さは2つ分とする。__
- `self`は必ず独立させること。`self.x`のような形式の選択肢は禁止されている。


# 例:

例1

対象となるコードセル

```python
class AttentionHead(nn.Module):
   def __init__(self, head_size, config):
       super().__init__()
       self.key_fc= nn.Linear(config.embedding_dim, head_size, bias=False)
       self.query_fc = nn.Linear(config.embedding_dim, head_size, bias=False)
       self.value_fc = nn.Linear(config.embedding_dim, head_size, bias=False)


       # ドロップアウト
       self.dropout = nn.Dropout(config.dropout_rate)
       self.head_size = head_size


       ############ NEW ############
       self.relative_position_embedding_layer = RelativePositionEmbedding() # TODO: FILL
       ############ NEW ############


   def forward(self, input_tensor):
       B, T, C = input_tensor.shape  # バッチ、トークン長、埋め込みチャネル


       Key = self.key_fc.forward(input_tensor)     # (B, T, head_size)
       Query = self.query_fc.forward(input_tensor)   # (B, T, head_size)
       Value = self.value_fc.forward(input_tensor)   # (B, T, head_size)


       # Attentionスコアを計算中 (QK^T) / sqrt(embedding_dim)
       attention_weights_before_mask = Query @ Key.transpose(-2, -1) * self.head_size**(-0.5)


       ############ NEW ############
       relative_position_bias_matrix = self.relative_position_embedding_layer( # TODO: FILL
           query_len = T, # TODO: FILL
           key_len = T, # TODO: FILL
           device_type=input_tensor.device)  # (T, T)
       attention_weights_before_mask = attention_weights_before_mask + relative_position_bias_matrix  # TODO: FILL
       ############ NEW ############


       # マスク適用済み
       mask = torch.triu(torch.ones(T, T), diagonal=1).to(input_tensor.device)
       masked_attention_weights = attention_weights_before_mask.masked_fill(mask == 1, float('-inf'))


       # ソフトマックス → ドロップアウト → 重み付き和
       attention_weights = F.softmax(masked_attention_weights, dim=-1)
       attention_weights = self.dropout(attention_weights)


       out = attention_weights @ Value  # (B, T, head_size)
       return out

```

期待される穴埋め用セルと、markdownの回答セル

```markdown
🔘 **Options**: 余計な選択肢があるかもしれません。同じ選択肢を2回以上使うかもしれません。


`RelativePositionEmbedding`　`Query`　`Key`　`size`　`T`　`B`　`C`　`shape`　`relative_position_bias_matrix`　`self.dropout`　`self.key_fc`　`transpose`　`input_tensor`　`F.relu`　`F.softmax`


```

```python
class AttentionHead(nn.Module):
   def __init__(self, head_size, config):
       super().__init__()
       self.key_fc= nn.Linear(config.embedding_dim, head_size, bias=False)
       self.query_fc = nn.Linear(config.embedding_dim, head_size, bias=False)
       self.value_fc = nn.Linear(config.embedding_dim, head_size, bias=False)


       # ドロップアウト
       self.dropout = nn.Dropout(config.dropout_rate)
       self.head_size = head_size


       ############ NEW ############
       self.relative_position_embedding_layer = _________________________________()  # TODO: FILL
       ############ NEW ############


   def forward(self, input_tensor):
       B, T, C = input_tensor.shape  # バッチ、トークン長、埋め込みチャネル


       Key = self.key_fc.forward(input_tensor)     # (B, T, head_size)
       Query = self.query_fc.forward(input_tensor)   # (B, T, head_size)
       Value = self.value_fc.forward(input_tensor)   # (B, T, head_size)


       # Attentionスコアを計算中 (QK^T) / sqrt(embedding_dim)
       attention_weights_before_mask = Query @ Key.transpose(-2, -1) * self.head_size**(-0.5)


       ############ NEW ############
       relative_position_bias_matrix = _____________________________________________( # TODO: FILL
           query_len = __, # TODO: FILL
           key_len = __, # TODO: FILL
           device_type=input_tensor.device)  # (T, T)
       attention_weights_before_mask = attention_weights_before_mask + _____________________________  # TODO: FILL
       ############ NEW ############


       # マスク適用済み
       mask = torch.triu(torch.ones(T, T), diagonal=1).to(input_tensor.device)
       masked_attention_weights = attention_weights_before_mask.masked_fill(mask == 1, float('-inf'))


       # ソフトマックス → ドロップアウト → 重み付き和
       attention_weights = F.softmax(masked_attention_weights, dim=-1)
       attention_weights = self.dropout(attention_weights)


       out = attention_weights @ Value  # (B, T, head_size)
       return out
```

```markdown
<details>
<summary>クリックして答えを表示/非表示する</summary>


```python
class AttentionHead(nn.Module):
   def __init__(self, head_size, config):
       super().__init__()
       self.key_fc= nn.Linear(config.embedding_dim, head_size, bias=False)
       self.query_fc = nn.Linear(config.embedding_dim, head_size, bias=False)
       self.value_fc = nn.Linear(config.embedding_dim, head_size, bias=False)


       # ドロップアウト
       self.dropout = nn.Dropout(config.dropout_rate)
       self.head_size = head_size


       ############ NEW ############
       self.relative_position_embedding_layer = RelativePositionEmbedding()
       ############ NEW ############


   def forward(self, input_tensor):
       B, T, C = input_tensor.shape  # バッチ、トークン長、埋め込みチャネル


       Key = self.key_fc.forward(input_tensor)     # (B, T, head_size)
       Query = self.query_fc.forward(input_tensor)   # (B, T, head_size)
       Value = self.value_fc.forward(input_tensor)   # (B, T, head_size)


       # Attentionスコアを計算中 (QK^T) / sqrt(embedding_dim)
       attention_weights_before_mask = Query @ Key.transpose(-2, -1) * self.head_size**(-0.5)


       ############ NEW ############
       relative_position_bias_matrix = self.relative_position_embedding_layer(
           query_len = T,
           key_len = T,
           device_type=input_tensor.device)  # (T, T)
       attention_weights_before_mask = attention_weights_before_mask + relative_position_bias_matrix
       ############ NEW ############


       # マスク適用済み
       mask = torch.triu(torch.ones(T, T), diagonal=1).to(input_tensor.device)
       masked_attention_weights = attention_weights_before_mask.masked_fill(mask == 1, float('-inf'))


       # ソフトマックス → ドロップアウト → 重み付き和
       attention_weights = F.softmax(masked_attention_weights, dim=-1)
       attention_weights = self.dropout(attention_weights)


       out = attention_weights @ Value  # (B, T, head_size)
       return out
```
```
