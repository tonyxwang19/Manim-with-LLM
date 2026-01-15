from manim import *

class AreaUnderOneOverX(Scene):
    def construct(self):
        # Title
        title = Text("Area Under the Curve 1/x", font_size=48)
        subtitle = Text("From x = 1 to x = 3", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        
        # Move title to top
        self.play(
            title.animate.to_edge(UP, buff=0.5),
            subtitle.animate.next_to(title, DOWN, buff=0.3).scale(0.8)
        )
        
        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 2, 0.5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": [1, 2, 3],
                "decimal_number_config": {"num_decimal_places": 0}
            },
            y_axis_config={
                "numbers_to_include": [0.5, 1, 1.5],
                "decimal_number_config": {"num_decimal_places": 1}
            }
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Position axes
        axes_group = VGroup(axes, axes_labels)
        axes_group.scale(0.9).to_edge(LEFT, buff=1)
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        
        # Define the function 1/x
        def func(x):
            return 1/x
        
        # Create the curve
        curve = axes.plot(func, x_range=[0.5, 3.5], color=GREEN)
        curve_label = MathTex("y = \\frac{1}{x}", color=GREEN)
        curve_label.next_to(curve, RIGHT, buff=0.5)
        
        self.play(Create(curve), Write(curve_label))
        self.wait(1)
        
        # Highlight the region from x=1 to x=3
        vertical_line_1 = axes.get_vertical_line(axes.i2gp(1, curve), color=YELLOW)
        vertical_line_3 = axes.get_vertical_line(axes.i2gp(3, curve), color=YELLOW)
        
        x_label_1 = MathTex("x = 1", color=YELLOW).next_to(vertical_line_1, DOWN, buff=0.1)
        x_label_3 = MathTex("x = 3", color=YELLOW).next_to(vertical_line_3, DOWN, buff=0.1)
        
        self.play(
            Create(vertical_line_1),
            Create(vertical_line_3),
            Write(x_label_1),
            Write(x_label_3)
        )
        self.wait(1)
        
        # Create the area under the curve
        area = axes.get_area(curve, x_range=[1, 3], color=[BLUE, TEAL], opacity=0.5)
        self.play(FadeIn(area))
        self.wait(2)
        
        # Move the curve group to make room for explanation
        curve_group = VGroup(axes, axes_labels, curve, curve_label, 
                            vertical_line_1, vertical_line_3, x_label_1, x_label_3, area)
        self.play(curve_group.animate.scale(0.8).to_edge(LEFT, buff=0.5))
        
        # Show the integral expression
        integral_text = Text("The area is given by:", font_size=36)
        integral_expression = MathTex(
            "\\text{Area} = \\int_{1}^{3} \\frac{1}{x} \\, dx",
            font_size=48
        )
        integral_group = VGroup(integral_text, integral_expression)
        integral_group.arrange(DOWN, buff=0.5)
        integral_group.to_edge(RIGHT, buff=1)
        
        self.play(Write(integral_text))
        self.wait(1)
        self.play(Write(integral_expression))
        self.wait(2)
        
        # Show the antiderivative
        antiderivative_text = Text("The antiderivative of 1/x is:", font_size=36)
        antiderivative = MathTex(
            "\\int \\frac{1}{x} \\, dx = \\ln|x| + C",
            font_size=48,
            color=YELLOW
        )
        antiderivative_group = VGroup(antiderivative_text, antiderivative)
        antiderivative_group.arrange(DOWN, buff=0.5)
        antiderivative_group.next_to(integral_group, DOWN, buff=1)
        
        self.play(Write(antiderivative_text))
        self.wait(1)
        self.play(Write(antiderivative))
        self.wait(2)
        
        # Apply the Fundamental Theorem of Calculus
        ftc_text = Text("Applying the Fundamental Theorem:", font_size=36)
        ftc_expression = MathTex(
            "\\text{Area} = \\ln|3| - \\ln|1|",
            font_size=48,
            color=GREEN
        )
        ftc_group = VGroup(ftc_text, ftc_expression)
        ftc_group.arrange(DOWN, buff=0.5)
        ftc_group.next_to(antiderivative_group, DOWN, buff=1)
        
        self.play(Write(ftc_text))
        self.wait(1)
        self.play(Write(ftc_expression))
        self.wait(2)
        
        # Simplify using logarithm properties
        simplify_text = Text("Simplifying using log properties:", font_size=36)
        simplify_expression = MathTex(
            "\\text{Area} = \\ln\\left(\\frac{3}{1}\\right) = \\ln(3)",
            font_size=48,
            color=RED
        )
        simplify_group = VGroup(simplify_text, simplify_expression)
        simplify_group.arrange(DOWN, buff=0.5)
        simplify_group.next_to(ftc_group, DOWN, buff=1)
        
        self.play(Write(simplify_text))
        self.wait(1)
        self.play(Write(simplify_expression))
        self.wait(2)
        
        # Show numerical approximation
        approx_text = Text("Numerical approximation:", font_size=36)
        approx_value = MathTex(
            "\\ln(3) \\approx 1.0986",
            font_size=48,
            color=ORANGE
        )
        approx_group = VGroup(approx_text, approx_value)
        approx_group.arrange(DOWN, buff=0.5)
        approx_group.next_to(simplify_group, DOWN, buff=1)
        
        self.play(Write(approx_text))
        self.wait(1)
        self.play(Write(approx_value))
        self.wait(3)
        
        # Highlight the final answer
        final_box = SurroundingRectangle(approx_value, color=GREEN, buff=0.2)
        self.play(Create(final_box))
        self.wait(2)
        
        # Fade out everything except the final answer and curve
        keep_group = VGroup(curve_group, approx_group, final_box)
        fade_group = VGroup(
            integral_group, antiderivative_group, ftc_group, simplify_group,
            title, subtitle
        )
        
        self.play(FadeOut(fade_group))
        
        # Move the final answer to a better position
        self.play(
            approx_group.animate.scale(1.2).move_to(ORIGIN + RIGHT * 3),
            final_box.animate.scale(1.2).move_to(approx_group)
        )
        
        # Create a rectangle to represent the area numerically
        area_rectangle = Rectangle(
            width=approx_value.width * 1.5,
            height=approx_value.height * 2,
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=3
        )
        area_rectangle.move_to(approx_group)
        
        self.play(Create(area_rectangle))
        self.wait(3)
        
        # Final summary
        summary = Text(
            "The area under 1/x from 1 to 3 is exactly ln(3)",
            font_size=36,
            color=YELLOW
        )
        summary.to_edge(DOWN, buff=0.5)
        
        self.play(Write(summary))
        self.wait(3)