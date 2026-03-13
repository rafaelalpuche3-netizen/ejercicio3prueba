import streamlit as st
from datetime import date

# 1. Configuración de página (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(page_title="IA y Motivación Escolar", layout="wide")

# 2. Definición de estilos CSS Mejorados
# He ajustado el z-index y los márgenes para asegurar visibilidad
st.markdown("""
    <style>
    /* Estilo para el fondo de la aplicación */
    .stApp {
        background: linear-gradient(135deg, #001f3f 0%, #0074D9 50%, #7FDBFF 100%);
        color: #FFFFFF;
    }

    /* Contenedor del Artículo con bordes redondeados */
    .main-card {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 2rem;
        border-radius: 25px;
        border: 4px solid #01FF70;
        box-shadow: 12px 12px 0px #FF4136;
        color: #001f3f;
        margin-top: 20px;
    }

    /* Títulos e Iconos */
    .header-title {
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 3.2rem;
        color: white;
        text-shadow: 4px 4px #F012BE
        line-height: 1.1;
    }

    .kant-quote {
        text-align: right;
        font-style: italic;
        font-size: 1.3rem;
        color: #FFDC00;
        font-weight: bold;
        margin: 15px 0;
    }

    .section-icon {
        color: #0074D9;
        font-weight: 800;
        font-size: 1.6rem;
        margin-top: 20px;
        display: block;
        border-bottom: 2px dashed #0074D9;
    }

/* Ajuste de la fecha */
.date-left {
text-align: left;
font-weight: bold;
color: #01FF70;
font-size: 1.2rem;
}
</style>
    """, unsafe_allow_html=True)

# 3. Encabezado y Fecha
st.markdown(f"<div class='date-left'>📅 {date.today().strftime('%d / %m / %Y')}</div>", unsafe_allow_html=True)

st.markdown("<h1 class='header-title'>🤖 Inteligencia artificial en las escuelas: ¿motivación o desmotivación? 🎓</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="main-card">

<span class="section-icon">🔍 El Motor Invisible: Cómo la Inteligencia Artificial está Redefiniendo las Ganas de Aprender</span>

Durante décadas, el aula de clases ha sido un escenario de batalla silenciosa contra la apatía. 
El modelo tradicional, diseñado bajo una lógica de "talla única", a menudo dejaba a los estudiantes 
sintiéndose como piezas de un engranaje.

<span class="section-icon">🧠 El Trípode de la Motivación Humana</span>

Para entender este cambio debemos mirar hacia la Teoría de la Autodeterminación (SDT). 
Esta teoría plantea tres necesidades psicológicas básicas:

• Autonomía  
• Competencia  
• Relación  

<span class="section-icon">🤖 La IA como Espejo de Nuestras Habilidades</span>

La IA educativa puede ofrecer retroalimentación instantánea. 
Esto permite que los estudiantes desarrollen mayor autorregulación 
y perciban control sobre su aprendizaje.

<span class="section-icon">🚀 Un Futuro de Personalización Extrema</span>

La inteligencia artificial puede reducir tareas repetitivas y permitir 
que estudiantes y docentes se concentren en habilidades más complejas 
como el pensamiento crítico y la creatividad.

</div>
""", unsafe_allow_html=True)
