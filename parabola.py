from manim import *

class ParabolicMotion(Scene):
    def construct(self):
        # Create axes with numbers
        axes = Axes(
            x_range=[0, 10, 1],   # [start, end, step]
            y_range=[0, 6, 1],
            x_length=10,
            y_length=6,
            tips=True,
            axis_config={
                "include_numbers": True,
                "numbers_to_exclude": [],
                "font_size": 24
            },
        )
        labels = axes.get_axis_labels("x", "y")
        self.play(Create(axes), Write(labels))

        # Parabola function
        def parabola_func(x):
            return -0.2 * x**2 + 2 * x

        # Create trajectory path
        trajectory = axes.plot(parabola_func, x_range=[0, 10], color=WHITE)

        # Starting point for the ball
        start_point = axes.c2p(0, parabola_func(0))

        # Create bigger ball
        ball = Dot(point=start_point, color=RED).scale(3)

        # Trail VMobject
        trail = VMobject(color=YELLOW, stroke_width=4)
        trail.set_points_as_corners([start_point.copy()])

        self.add(ball, trail)

        # Update trail while ball moves
        def update_trail(mob):
            new_point = ball.get_center()
            trail.points = np.vstack([trail.points, [new_point]])

        trail.add_updater(update_trail)

        # Animate ball along the parabola
        self.play(
            MoveAlongPath(ball, trajectory),
            run_time=4,
            rate_func=linear,
        )

        trail.remove_updater(update_trail)
        self.wait(1)
