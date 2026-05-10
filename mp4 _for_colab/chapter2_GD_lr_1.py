from manim import *
import numpy as np

# 画面のサイズ設定(標準の16:9)
config.pixel_height = 720
config.pixel_width = 1280
config.frame_height = 7.0
config.frame_width = 12.4

class GradientDescentDiverge(Scene):
    def construct(self):
        # コンテキスト:フォントサイズ設定
        equation_font_size = 36
        label_font_size = 32
        
        # --------------------------------------------------------------------------
        # ① タイトルと学習率の設定を表示
        # --------------------------------------------------------------------------
        main_title = Tex("Gradient Descent (Learning Rate = 1)").scale(1.1).to_edge(UP)
        self.play(Write(main_title))

        # 数式(損失関数と更新式)
        eq_group = VGroup(
            MathTex(r"L = 2.5(w - 2)^2"),
            MathTex(r"w \leftarrow w - 1 \cdot {L'}")
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL).shift(DOWN * 0.5)
        
        self.play(FadeIn(eq_group))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ② 画面右上にダッシュボードを作成
        # --------------------------------------------------------------------------
        w_tracker = ValueTracker(0.0)
        epoch_tracker = ValueTracker(0)
        loss_function = lambda w: 2.5 * (w - 2)**2

        # リアルタイムで値が更新されるテキスト群
        # 修正箇所: 数値が爆発的に大きくなるため、見やすいようにカンマ区切りで表示
        dashboard = always_redraw(lambda: VGroup(
            Tex(f"Epoch: {int(epoch_tracker.get_value())}", color=YELLOW),
            Tex(f"w = {w_tracker.get_value():,.1f}", color=WHITE),
            Tex(f"Loss = {loss_function(w_tracker.get_value()):,.0f}", color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.5))
        
        self.play(FadeIn(dashboard))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ③ wL座標平面とグラフの展開
        # --------------------------------------------------------------------------
        # 修正箇所: 発散の様子を捉えるため、座標軸のスケールを劇的に拡大
        axes = Axes(
            x_range=[-40, 40, 10],   # w軸: -40から40 (10刻み)
            y_range=[0, 3000, 500],  # L軸: 0から3000 (500刻み)
            axis_config={"color": WHITE, "include_tip": True},
            x_axis_config={"label_direction": DOWN, "tip_shape": StealthTip},
            y_axis_config={"label_direction": LEFT, "tip_shape": StealthTip},
        ).scale(0.64).shift(DOWN * 1.5)

        w_label = axes.get_x_axis_label(Tex("weight")).set_color(WHITE).set_font_size(label_font_size)
        L_label = axes.get_y_axis_label(Tex("Loss")).set_color(WHITE).set_font_size(label_font_size)

        self.play(Create(axes), FadeIn(w_label), FadeIn(L_label))

        # グラフの描画 (拡大した軸に合わせて描画範囲を拡大)
        graph = axes.plot(loss_function, color=WHITE, x_range=[-35, 39])
        self.play(Create(graph))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ④ グラフ上の点と接線
        # --------------------------------------------------------------------------
        # 修正箇所: wとLが数百万規模になると描画エンジン(Cairo)がエラーを起こすため、
        # 画面外の安全な位置(±1000)で座標の移動を制限するヘルパー関数
        def get_safe_p(w):
            safe_w = np.clip(w, -1000, 1000)
            safe_l = np.clip(loss_function(w), -10000, 50000)
            return axes.c2p(safe_w, safe_l)

        dot = always_redraw(lambda: 
            Dot(color=YELLOW, radius=0.08).move_to(get_safe_p(w_tracker.get_value()))
        )
        self.play(FadeIn(dot))

        # 接線の関数にも safe 座標を適用
        def get_custom_tangent():
            w = w_tracker.get_value()
            dw = 0.001
            p_current = get_safe_p(w)
            p_next = get_safe_p(w + dw)
            angle = np.arctan2(p_next[1] - p_current[1], p_next[0] - p_current[0])
            return Line(LEFT * 1.0, RIGHT * 1.0, color=BLUE).set_angle(angle).move_to(p_current)

        tangent_line = always_redraw(get_custom_tangent)
        self.play(Create(tangent_line))
        self.wait(1)

        # --------------------------------------------------------------------------
        # ⑤ 提示されたPythonの出力に沿ってアニメーション
        # --------------------------------------------------------------------------
        # 発散していく強烈な数値ステップ
        w_steps = [10.0, -30.0, 130.0, -510.0, 2050.0, -8190.0, 32770.0, -131070.0, 524290.0, -2097150.0]

        for i, target_w in enumerate(w_steps):
            epoch = i + 1
            
            # 発散の勢いを表現するため、徐々に動きを加速させる
            current_run_time = max(0.2, 0.8 - i * 0.1)
            
            self.play(
                w_tracker.animate.set_value(target_w),
                epoch_tracker.animate.set_value(epoch),
                run_time=current_run_time,
                rate_func=smooth
            )
            
            # 最初の2エポック(画面内に収まる範囲)はじっくり見せる
            if i < 2:
                self.wait(0.5)

        self.wait(3)

if __name__ == "__main__":
    from manim import config, scene
    import sys
    sys.argv = ["manim", "-p", "-ql", __file__]
    from manim import main
    main()