### または #### と CODE を含む、markdownの見出しセルは、ロジックの起点となる重要なセルである。
そのセクションで行うワークフローを解説するmarkdownセルを追加する。
- return など、説明する必要がない軽微な内容であれば、一切の変化/追加を行わない。
- 中間変数にいちいち触れる必要はない
- 何を入力として、何を出力として得たいのかビジョン。
- それを出す内部のロジックを視覚的にまたは直感的に解説する
- 数式については、LaTeX表記で、かつJupyterNotebook向けに[[ではなく$$で囲む。
- 文中の数式や記号については、LaTeX表記で、かつJupyterNotebook向けに[ではなく$で囲む。
例:
# 例1
対象セル
#### 現在の学習ステップが、線形ウォーミングアップ段階にある場合
CODE: `if current_step < warmup_steps:`

追加するmarkdownセル
**Mission: 現在のステップ数に応じた、適切な学習率を計算する！**
学習率を固定にすると、学習初期では勾配が大きいため、急激にパラメータが更新されてしまい、学習が不安定化します。  
そこで、学習開始直後は0として、最大学習率に向けて *直線的に* 学習率を上げます。  
ウォームアップ段階が長いほどゆっくり学習率が上がります。
- **入力**: `current_step`（例: 500）, `warmup_steps`（例: 1000）, `max_learning_rate`（例: 2e-4）
- **出力**: `learning_rate`（ウォームアップ中の学習率）


数式で示すと

$$
learning\_rate =
max\_learning\_rate \times
\frac{current\_step}{warmup\_steps}
$$

```
learning_rate
  ^            max_learning_rate
  |          /
  |        /
  |      /
  |____/________________> current_step
      0        warmup_steps
```
例えば、 `current_step=500` はウォームアップの半分なので、学習率もだいたい **maxの半分**になります（この後のprintで確認します）。
