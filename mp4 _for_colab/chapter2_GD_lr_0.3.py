from manim import *
import numpy as np

# 画面のサイズ設定(標準の16:9)
config.pixel_height = 720
config.pixel_width = 1280
config.frame_height = 7.0
config.frame_width = 12.4

class GradientDescentLR(Scene):
    def construct(self):
        # コンテキスト:フォントサイズ設定
        equation_font_size = 36
        label_font_size = 32
        
        # --------------------------------------------------------------------------
        # ① タイトルと学習率の設定を表示
        # --------------------------------------------------------------------------
        main_title = Tex("Gradient Descent (Learning Rate = 0.3)").scale(1.1).to_edge(UP)
        self.play(Write(main_title))

        # 数式(損失関数と更新式)
        eq_group = VGroup(
            MathTex(r"L = 2.5(w - 2)^2"),
            MathTex(r"w \leftarrow w - 0.3 \cdot {L'}")
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).shift(DOWN * 0.5)
        
        self.play(FadeIn(eq_group))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ② 画面右上にPythonの出力を模したダッシュボードを作成
        # --------------------------------------------------------------------------
        w_tracker = ValueTracker(0.0)
        epoch_tracker = ValueTracker(0)
        loss_function = lambda w: 2.5 * (w - 2)**2

        # リアルタイムで値が更新されるテキスト群 (ご要望通り、枠線なし)
        dashboard = always_redraw(lambda: VGroup(
            Tex(f"Epoch: {int(epoch_tracker.get_value())}", color=YELLOW),
            Tex(f"w = {w_tracker.get_value():.3f}", color=WHITE),
            Tex(f"Loss = {loss_function(w_tracker.get_value()):.6f}", color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.5))
        
        self.play(FadeIn(dashboard))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ③ wL座標平面とグラフの展開
        # --------------------------------------------------------------------------
        # 修正箇所: グラフのサイズを8割(0.64)に縮小し、見切れない程度に下へ移動(DOWN * 1.5)
        # L軸の目盛りを1刻みに変更
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

        # 修正箇所: 色を白に、描画開始位置を w = -0.3 に変更
        graph = axes.plot(loss_function, color=WHITE, x_range=[-0.3, 4.2])
        self.play(Create(graph))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ④ グラフ上の点と接線(初期値 w=0.0)
        # --------------------------------------------------------------------------
        # スケールダウンに合わせて点のサイズも微調整
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
            # グラフの縮小に合わせて接線の長さも調整 (1.5 -> 1.0)
            return Line(LEFT * 1.0, RIGHT * 1.0, color=BLUE).set_angle(angle).move_to(p_current)

        tangent_line = always_redraw(get_custom_tangent)
        self.play(Create(tangent_line))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ⑤ 提示されたPythonの出力に沿ってアニメーション
        # --------------------------------------------------------------------------
        w_steps = [3.000, 1.500, 2.250, 1.875, 2.062, 1.969, 2.016, 1.992, 2.004, 1.998]

        for i, target_w in enumerate(w_steps):
            epoch = i + 1
            
            # 徐々に移動速度を速くして、テンポ良く見せる
            current_run_time = max(0.4, 1.2 - i * 0.1)
            
            self.play(
                w_tracker.animate.set_value(target_w),
                epoch_tracker.animate.set_value(epoch),
                run_time=current_run_time,
                rate_func=smooth
            )
            
            if i < 3:
                self.wait(0.5)

        self.wait(3)

if __name__ == "__main__":
    from manim import config, scene
    import sys
    sys.argv = ["manim", "-p", "-ql", __file__]
    from manim import main
    main()