from manim import *
import numpy as np

# 画面のサイズ設定(標準の16:9)
config.pixel_height = 720
config.pixel_width = 1280
config.frame_height = 7.0
config.frame_width = 12.4

class GradientDescentSmallLR(Scene):
    def construct(self):
        # コンテキスト:フォントサイズ設定
        equation_font_size = 36
        label_font_size = 32
        
        # --------------------------------------------------------------------------
        # ① タイトルと学習率の設定を表示
        # --------------------------------------------------------------------------
        # 修正箇所: 学習率を 0.001 に変更
        main_title = Tex("Gradient Descent (Learning Rate = 0.001)").scale(1.1).to_edge(UP)
        self.play(Write(main_title))

        # 数式(損失関数と更新式)
        # 修正箇所: 更新式の学習率を 0.001 に変更
        eq_group = VGroup(
            MathTex(r"L = 2.5(w - 2)^2"),
            MathTex(r"w \leftarrow w - 0.001 \cdot {L'}")
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).shift(DOWN * 0.5)
        
        self.play(FadeIn(eq_group))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ② 画面右上にダッシュボードを作成 (枠線なし)
        # --------------------------------------------------------------------------
        w_tracker = ValueTracker(0.0)
        epoch_tracker = ValueTracker(0)
        loss_function = lambda w: 2.5 * (w - 2)**2

        # リアルタイムで値が更新されるテキスト群
        dashboard = always_redraw(lambda: VGroup(
            Tex(f"Epoch: {int(epoch_tracker.get_value())}", color=YELLOW),
            Tex(f"w = {w_tracker.get_value():.3f}", color=WHITE),
            Tex(f"Loss = {loss_function(w_tracker.get_value()):.6f}", color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.5))
        
        self.play(FadeIn(dashboard))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ③ wL座標平面とグラフの展開 (前回の被らないレイアウトを維持)
        # --------------------------------------------------------------------------
        # グラフのスケールと位置は比較のため前回と同じ(0.64倍、DOWN * 1.5)
        axes = Axes(
            x_range=[-1, 4.5, 1], # w軸: -1から4.5
            y_range=[0, 11, 1],   # L軸: 0から11 (1刻み)
            axis_config={"color": WHITE, "include_tip": True},
            x_axis_config={"label_direction": DOWN, "tip_shape": StealthTip},
            y_axis_config={"label_direction": LEFT, "tip_shape": StealthTip},
        ).scale(0.58).shift(DOWN * 1.5)

        w_label = axes.get_x_axis_label(Tex("weight")).set_color(WHITE).set_font_size(label_font_size)
        L_label = axes.get_y_axis_label(Tex("Loss")).set_color(WHITE).set_font_size(label_font_size)

        self.play(Create(axes), FadeIn(w_label), FadeIn(L_label))

        # グラフの描画
        graph = axes.plot(loss_function, color=WHITE, x_range=[-0.3, 4.2])
        self.play(Create(graph))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ④ グラフ上の点と接線(初期値 w=0.0)
        # --------------------------------------------------------------------------
        dot = always_redraw(lambda: 
            Dot(color=YELLOW, radius=0.08).move_to(
                axes.c2p(w_tracker.get_value(), loss_function(w_tracker.get_value()))
            )
        )
        self.play(FadeIn(dot))

        # 接線のズレを解消するカスタム関数
        def get_custom_tangent():
            w = w_tracker.get_value()
            dw = 0.001
            p_current = axes.c2p(w, loss_function(w))
            p_next = axes.c2p(w + dw, loss_function(w + dw))
            angle = np.arctan2(p_next[1] - p_current[1], p_next[0] - p_current[0])
            return Line(LEFT * 1.0, RIGHT * 1.0, color=BLUE).set_angle(angle).move_to(p_current)

        tangent_line = always_redraw(get_custom_tangent)
        self.play(Create(tangent_line))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ⑤ 提示されたPythonの出力に沿ってアニメーション
        # --------------------------------------------------------------------------
        # lr=0.001 のときの w の推移データ
        w_steps = [0.010, 0.020, 0.030, 0.040, 0.050, 0.059, 0.069, 0.079, 0.088, 0.098]

        for i, target_w in enumerate(w_steps):
            epoch = i + 1
            
            # 今回は「進みが遅いこと」を強調するため、等速(linear)で一定のリズムで進める
            self.play(
                w_tracker.animate.set_value(target_w),
                epoch_tracker.animate.set_value(epoch),
                run_time=0.5,
                rate_func=linear
            )

        self.wait(3)

if __name__ == "__main__":
    from manim import config, scene
    import sys
    sys.argv = ["manim", "-p", "-ql", __file__]
    from manim import main
    main()