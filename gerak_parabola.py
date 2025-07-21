from manim import *
import numpy as np

class GerakParabola(Scene):
    def construct(self):
        # Constants
        v0 = 10  # initial velocity (m/s)
        angle_deg = 45
        angle = angle_deg * DEGREES
        g = 9.8

        # Calculations
        t_max = (v0 * np.sin(angle)) / g
        h_max = (v0**2 * (np.sin(angle))**2) / (2 * g)
        T = 2 * t_max
        R = v0 * np.cos(angle) * T

        # Axes
        axes = Axes(
            x_range=[0, R + 1, 1],
            y_range=[0, h_max + 2, 1],
            tips=True,
            axis_config={
                "include_numbers": True,
                "numbers_to_exclude": [],
                "font_size": 24
            }
        )
        x_label = axes.get_x_axis_label("x (m)")
        y_label = axes.get_y_axis_label("y (m)")
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Ball path
        path = axes.plot_parametric_curve(
            lambda t: np.array([
                v0 * np.cos(angle) * t,
                v0 * np.sin(angle) * t - 0.5 * g * t**2,
                0
            ]),
            t_range=[0, T],
            color=BLUE
        )
        self.play(Create(path), run_time=2)

        # Ball
        ball = Dot(color=RED)
        t = ValueTracker(0)

        def get_pos():
            time = t.get_value()
            return axes.coords_to_point(
                v0 * np.cos(angle) * time,
                v0 * np.sin(angle) * time - 0.5 * g * time**2
            )

        ball.add_updater(lambda b: b.move_to(get_pos()))
        self.add(ball)

        # Velocity vector arrow
        def get_velocity_vector(time):
            vx = v0 * np.cos(angle)
            vy = v0 * np.sin(angle) - g * time
            return np.array([vx, vy, 0])

        v_arrow = always_redraw(lambda: Arrow(
            start=get_pos(),
            end=get_pos() + get_velocity_vector(t.get_value()) * 0.1,
            color=YELLOW
        ))
        self.add(v_arrow)

        # Label before/at/after max height
        label = always_redraw(lambda: Text(
            "Sebelum Ketinggian Maksimum" if t.get_value() < t_max else (
                "Di Ketinggian Maksimum" if abs(t.get_value() - t_max) < 0.1 else "Setelah Ketinggian Maksimum"
            ),
            font_size=18
        ).next_to(ball, UP + RIGHT))
        self.add(label)

        # Max height marker
        max_dot = Dot(axes.coords_to_point(v0 * np.cos(angle) * t_max, h_max), color=GREEN)
        self.play(FadeIn(max_dot))

        # Show motion
        self.play(t.animate.set_value(T), run_time=6, rate_func=linear)
        self.wait()

        # Draw velocity vector at 3 specific points:
        for t_point, name in [(t_max/2, "Sebelum Ketinggian Maksimum"),
                              (t_max, "Di Ketinggian Maksimum"),
                              (t_max + t_max/2, "Setelah Ketinggian Maksimum")]:
            pos = axes.coords_to_point(
                v0 * np.cos(angle) * t_point,
                v0 * np.sin(angle) * t_point - 0.5 * g * t_point**2
            )
            vec = get_velocity_vector(t_point)
            arrow = Arrow(start=pos, end=pos + vec * 0.1, color=ORANGE)
            dot = Dot(pos, color=RED)
            label = Text(name, font_size=18).next_to(dot, UP)
            formula = MathTex(
                r"\vec{v} = \left( v_0 \cos\theta,\, v_0 \sin\theta - gt \right)"
            ).scale(0.6).next_to(arrow, RIGHT)
            self.play(FadeIn(dot), GrowArrow(arrow), Write(label), Write(formula))
            self.wait()

        self.wait()
