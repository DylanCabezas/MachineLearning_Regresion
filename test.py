from manim import *
import numpy as np

class RegresionLinealPolinomial(Scene):
    def construct(self):
        np.random.seed(0)

        #======================================
        # Datos
        x = np.linspace(10, 20, 100)
        y = 2*x + 1 + np.random.randn(100)*2

        #======================================
        # ESCENA 1: Título y puntos
        
        titulo = Text("Regresion Lineal y Polinomica", font_size=40).to_edge(UP)
        self.play(Write(titulo, run_time=2))

        ejes = Axes(
            x_range=[0, 25, 5],
            y_range=[0, 50, 10],
            x_length=8,
            y_length=5,
            tips=False
        ).shift(DOWN*0.5)

        nums_x = VGroup(*[Text(str(i), font_size=15).next_to(ejes.x_axis.n2p(i), DOWN) for i in range(0, 26, 5)])
        nums_y = VGroup(*[Text(str(i), font_size=15).next_to(ejes.y_axis.n2p(i), LEFT, buff=0.2) for i in range(0, 51, 10)])
        
        label_x = Text("Tamaño casa", font_size=22).next_to(ejes.x_axis.get_end(), DOWN, buff=0.4)
        label_y = Text("Precio", font_size=22).next_to(ejes.y_axis, LEFT, buff=0.7).rotate(90*DEGREES)

        puntos = VGroup(*[Dot(ejes.coords_to_point(xi, yi), color=BLUE, radius=0.05) for xi, yi in zip(x, y)])
        
        self.play(Create(ejes), FadeIn(nums_x), FadeIn(nums_y), Write(label_x), Write(label_y), run_time=3)
        self.play(FadeIn(puntos, run_time=1.5))
        self.wait(1.5)
    #======================================
        
        # ESCENA 2: Regresión lineal
        
        linea_lin = ejes.plot(lambda t: 1.9*t + 2.5, color=RED)
        formula_lin = Text("y = 1.95*x + 1.20", font_size=24, color=RED).next_to(ejes, UP, buff=0.2)

        self.play(Create(linea_lin), Write(formula_lin), run_time=3)
        self.wait(2)
        self.play(FadeOut(VGroup(puntos, linea_lin, label_x, label_y, formula_lin, ejes, nums_x, nums_y), run_time=2))

    #======================================
        
        # ESCENA 3: Error Lineal
        
        ejes_err = Axes(
            x_range=[0, 1100, 200],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=4,
            tips=False
        ).to_edge(DOWN)

        nums_x_err = VGroup(*[Text(str(i), font_size=14).next_to(ejes_err.x_axis.n2p(i), DOWN) for i in range(0, 1001, 200)])
        nums_y_err = VGroup(*[Text(str(i), font_size=14).next_to(ejes_err.y_axis.n2p(i), LEFT, buff=0.2) for i in range(0, 101, 20)])
        
        label_x_err = Text("Iteraciones", font_size=22).next_to(ejes_err.x_axis.n2p(1000), DOWN, buff=0.6).shift(RIGHT*0.5)
        label_y_err = Text("Error MSE", font_size=22).next_to(ejes_err.y_axis, LEFT, buff=0.7).rotate(90*DEGREES)

        curva_lin = ejes_err.plot(lambda t: 80 * np.exp(-0.005*t) + 4.15, x_range=[0, 1000], color=RED)
        
        self.play(Create(ejes_err), FadeIn(nums_x_err), FadeIn(nums_y_err), Write(label_x_err), Write(label_y_err), run_time=3)
        self.play(Create(curva_lin, run_time=3))
        
        texto_err_lin = Text("Error final lineal: 4.15", font_size=22, color=RED).next_to(ejes_err, UP)
        self.play(Write(texto_err_lin, run_time=1))
        self.wait(2)
        self.play(FadeOut(VGroup(ejes_err, nums_x_err, nums_y_err, label_x_err, label_y_err, curva_lin, texto_err_lin), run_time=1))
    #======================================
        
        # ESCENA 4: Regresión Polinómica
        
        self.play(Create(ejes), FadeIn(nums_x), FadeIn(nums_y), Write(label_x), Write(label_y), FadeIn(puntos), run_time=3)
        curva_poly = ejes.plot(lambda t: 0.004*(t-10)*(t-15)*(t-20) + 2*t + 1, x_range=[8, 24], color=ORANGE)
        formula_poly = Text("Modelo Polinomico (Grado 3)", font_size=24, color=ORANGE).next_to(ejes, UP, buff=0.2)

        self.play(Create(curva_poly), Write(formula_poly), run_time=4)
        self.wait(2)
        self.play(FadeOut(VGroup(puntos, curva_poly, label_x, label_y, formula_poly, ejes, nums_x, nums_y), run_time=1))
    #======================================
       
        # ESCENA 5: Error Polinómico
       
        self.play(Create(ejes_err), FadeIn(nums_x_err), FadeIn(nums_y_err), Write(label_x_err), Write(label_y_err), run_time=3)
        curva_poly_err = ejes_err.plot(lambda t: 90 * np.exp(-0.007*t) + 3.48, x_range=[0, 1000], color=ORANGE)
        
        self.play(Create(curva_poly_err, run_time=4))
        texto_err_poly = Text("Error final polinomico: 3.48", font_size=22, color=ORANGE).next_to(ejes_err, UP)
        self.play(Write(texto_err_poly, run_time=1))
        self.wait(2)
        self.play(FadeOut(VGroup(ejes_err, nums_x_err, nums_y_err, label_x_err, label_y_err, curva_poly_err, texto_err_poly, titulo), run_time=1))
    #======================================

        # ESCENA 6: Comparación final
   
        titulo_comp = Text("Comparativa Final de Metricas", font_size=36).to_edge(UP)
        self.play(Write(titulo_comp, run_time=2))

        ejes_comp = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 5, 1],
            x_length=9,
            y_length=4,
            tips=False
        ).shift(DOWN*0.5)

        nums_y_comp = VGroup(*[Text(str(i), font_size=15).next_to(ejes_comp.y_axis.n2p(i), LEFT, buff=0.2) for i in range(6)])
        
        nombres = ["MSE Lin", "MSE Poly", "R2 Lin", "R2 Poly"]
        colores = [RED, ORANGE, BLUE, GREEN]
        valores = [4.15, 3.48, 0.88, 0.90]

        barras = VGroup()
        etiquetas_x = VGroup()
        etiquetas_val = VGroup()

        for i, (val, nom, col) in enumerate(zip(valores, nombres, colores)):
            p1 = ejes_comp.coords_to_point(i + 0.2, 0)
            p2 = ejes_comp.coords_to_point(i + 0.8, val)
            rect = Rectangle(color=col, fill_opacity=0.7).replace(Line(p1, p2), stretch=True)
            barras.add(rect)
            etiquetas_x.add(Text(nom, font_size=18).next_to(ejes_comp.x_axis.n2p(i+0.5), DOWN))
            etiquetas_val.add(Text(f"{val:.2f}", font_size=16).next_to(rect, UP, buff=0.1))

        self.play(Create(ejes_comp), FadeIn(nums_y_comp), run_time=2)
        self.play(
            LaggedStart(
                *[Create(b) for b in barras],
                *[FadeIn(e) for e in etiquetas_x],
                *[Write(v) for v in etiquetas_val],
                lag_ratio=0.5
            ),
            run_time=6
        )
        
        info = Text("MSE  | R2 ", font_size=20).to_edge(DOWN, buff=0.5)
        self.play(Write(info, run_time=2))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects), run_time=1))
