"""
# Proyecto: Regresión Lineal y Polinomial 

## 👥 Integrantes del proyecto

Nombre             | Rol / Participación
------------------ | ---------------------
Dylan Cabezas      | Desarrollo del código
Mauricio Gonzales  | Desarrollo del informe
Fabrizio Rojas     | Desarrollo del video

---

## 📖 Introducción al caso
En este proyecto simulamos la relación entre el tamaño de una casa y su precio
para ilustrar cómo distintos modelos de regresión se ajustan a los mismos datos.
Generamos un conjunto de datos sintético siguiendo una relación lineal y añadimos
ruido aleatorio para reflejar la variabilidad real del mercado.  

Con este ejemplo buscamos mostrar cómo un modelo lineal ofrece una primera
aproximación sencilla, mientras que un modelo polinomial añade mayor flexibilidad
para capturar patrones más complejos. Finalmente, evaluamos ambos enfoques mediante
métricas como el **Error Cuadrático Medio (MSE)** y el **R² ajustado**, comparando
su capacidad explicativa y el riesgo de sobreajuste.

---

## 🛠️ Requisitos de software
- Python 3.8 o superior  
- Bibliotecas necesarias:
  - numpy
  - matplotlib
  - scikit-learn
  - manim

---

## 🖥️ Creación del video
El video se realizó con **Manim Community Edition**, mostrando paso a paso:  
1. Visualización de los datos simulados.  
2. Ajuste de regresión lineal y visualización de su función.  
3. Evolución del error MSE del modelo lineal vs iteraciones.  
4. Ajuste de regresión polinomial y visualización de su función.  
5. Evolución del error MSE del modelo polinomial vs iteraciones.  
6. Comparación final de métricas entre ambos modelos usando gráfico de barras
   y tabla de valores.  

**Nota:** Los datos de entrenamiento y las métricas fueron previamente calculados
en un código externo ejecutado en **Google Colab**. En el código del video se 
utilizaron directamente esos datos ya obtenidos para evitar sobrecarga de cálculos,
bloqueos o saturaciones de memoria al renderizar con Manim.

Se utilizaron colores consistentes para diferenciar los modelos:  
- Rojo → Regresión lineal  
- Naranja → Regresión polinomial  
- Otros colores → para métricas adicionales en la comparación final  

---

## 3. Renderizado y exportación
- El video se generó en **formato MP4** usando el comando:  
  manim -pqh test.py RegresionLinealPolinomial
- Posteriormente, si se necesitaba un formato MPEG (.mpg), se convirtió usando FFmpeg:  
  ffmpeg -i "C:\Ruta\Al\Proyecto\media\videos\test\1080p60\RegresionLinealPolinomial.mp4" \
  -c:v mpeg2video -qscale:v 2 \
  "C:\Ruta\Al\Proyecto\media\videos\test\1080p60\RegresionLinealPolinomial.mpg"

---

## 4. Métricas finales de los modelos

Modelo                | MSE    | R²     | R² ajustado
--------------------- | ------ | ------ | ------------
Lineal                | 4.1528 | 0.8848 | 0.8836
Polinomial (Grado 3)  | 3.4820 | 0.9034 | 0.9004

Estas métricas se muestran también visualmente en el video usando gráfico de barras y
una tabla resumen para facilitar la comparación.
"""


