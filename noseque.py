import streamlit as st
from datetime import date

# Configuración de la página
st.set_page_config(page_title="IA en la Educación", layout="wide")

# --- ESTILOS CSS (DISEÑO MAXIMALISTA Y PERSONALIZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Fondo general con degradado maximalista */
    .stApp {
        background: linear-gradient(135deg, #001f3f 0%, #0074D9 50%, #7FDBFF 100%);
    }

    /* Contenedor principal con bordes redondeados */
    .article-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 30px;
        border: 5px solid #01FF70; /* Toque de color maximalista */
        box-shadow: 10px 10px 0px #FF4136;
        color: #001f3f;
        margin-bottom: 30px;
    }

    /* Título con iconos */
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        color: #FFFFFF;
        text-shadow: 3px 3px #FF851B;
        margin-bottom: 0px;
    }

    /* Frase de Kant */
    .quote-kant {
        text-align: right;
        font-style: italic;
        font-weight: bold;
        color: #FFDC00;
        font-size: 1.2rem;
        margin-top: 10px;
    }

    /* Subtítulos con iconos */
    .subtitle {
        color: #0074D9;
        font-size: 1.8rem;
        font-weight: 700;
        border-bottom: 2px solid #0074D9;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Fecha alineada a la izquierda */
    .date-text {
        text-align: left;
        color: #F012BE;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    /* Texto del artículo */
    .article-body {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
col_date, col_empty = st.columns([1, 1])
with col_date:
    st.markdown(f"<p class='date-text'>📅 Fecha: {date.today().strftime('%d / %m / %Y')}</p>", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🤖 Inteligencia Artificial en las escuelas: ¿motivación o desmotivación? 🎓</h1>", unsafe_allow_html=True)

st.markdown("<p class='quote-kant'>“¡Ten el valor de servirte de tu propia razón!\" – Immanuel Kant</p>", unsafe_allow_html=True)

# --- CUERPO DEL ARTÍCULO ---
st.markdown("""
<div class="article-container">
    <h2 style='text-align: center; color: #001f3f;'>El Motor Invisible: Cómo la Inteligencia Artificial está Redefiniendo las Ganas de Aprender</h2>
    <p class="article-body">
    Durante décadas, el aula de clases ha sido un escenario de batalla silenciosa contra la apatía. El modelo tradicional, diseñado bajo una lógica de "talla única", a menudo dejaba a los estudiantes sintiéndose como piezas de un engranaje, movidos más por la presión de las calificaciones o el miedo al fracaso que por un interés genuino. Hasta hace poco, la psicología educativa sugería que la motivación era un rasgo casi fijo: o el alumno tenía curiosidad, o no la tenía. Sin embargo, una nueva frontera científica está emergiendo, donde la Inteligencia Artificial (IA) no solo actúa como una herramienta de consulta, sino como un sofisticado soporte emocional y psicológico que podría encender la chispa del aprendizaje autónomo.
    </p>

    <div class="subtitle">🏗️ El Trípode de la Motivación Humana</div>
    <p class="article-body">
    Para entender este cambio, debemos mirar hacia la Teoría de la Autodeterminación (SDT). Esta brújula psicológica nos dice que los seres humanos florecemos cuando se satisfacen tres necesidades básicas: la <b>autonomía</b> (sentir que somos dueños de nuestras decisiones), la <b>competencia</b> (sentir que somos capaces de superar retos) y la <b>relación</b> (sentirnos conectados con otros).
    <br><br>
    Tradicionalmente, la tecnología en el aula era pasiva. Pero investigadores como Galindo-Domínguez y su equipo (2025) han descubierto que la IA está cambiando las reglas del juego. Al ser personalizable y responder en tiempo real, la IA se comporta menos como un libro de texto y más como un "andamiaje" dinámico. Imagine a un tutor que nunca se cansa, que no juzga y que ajusta la dificultad de un problema justo al nivel donde el estudiante se siente desafiado pero no abrumado. Este es el núcleo de la competencia: el éxito constante y ajustado.
    </p>

    <div class="subtitle">🪞 La IA como Espejo de Nuestras Habilidades</div>
    <p class="article-body">
    Lo que hace fascinante a la IA educativa —definida por expertos como Castro y su equipo como sistemas que simulan procesos humanos para ofrecer apoyo personalizado— es su capacidad para fomentar la autorregulación. En lugar de esperar a que un profesor corrija un examen días después, un asistente virtual o chatbot ofrece retroalimentación instantánea. Esta inmediatez permite al alumno percibir el control sobre su propio progreso, transformando la motivación externa (estudiar por obligación) en una regulación más profunda y duradera.
    <br><br>
    Sin embargo, no todo es color de rosa en el laboratorio. Estudios recientes, como el análisis de redes de Li y colaboradores (2025), han revelado una verdad incómoda: muchos estudiantes hoy estudian sobre IA no por placer, sino por una "regulación introyectada". En términos sencillos, lo hacen por culpa, presión social o para no quedarse atrás en un mercado laboral competitivo.
    </p>

    <div class="subtitle">🚀 Un Futuro de Personalización Extrema</div>
    <p class="article-body">
    La relevancia de estos hallazgos es monumental. En contextos tan diversos como las escuelas de Polonia o los bachilleratos fiscales de Ecuador, la IA está demostrando que puede reducir la carga de tareas repetitivas y prevenir problemas como el plagio, permitiendo que tanto alumnos como maestros se concentren en lo que realmente importa: el pensamiento crítico y la creatividad.
    <br><br>
    Al final del día, la ciencia nos recuerda que la tecnología más avanzada es aquella que nos ayuda a reconectar con nuestro deseo más básico y humano: el de descubrir el mundo por nosotros mismos, a nuestro propio ritmo y con la confianza de que podemos lograrlo.
    </p>
</div>
""", unsafe_allow_html=True)

# --- REFERENCIAS BIBLIOGRÁFICAS ---
st.markdown("### 📚 Referencias Bibliográficas")

referencias = {
    "Annamalai et al. (2025) - ChatGPT en Malasia": """
    **RESUMEN:** Investiga los factores que determinan la motivación de estudiantes universitarios para el uso continuo de ChatGPT en el aprendizaje del idioma inglés en Malasia. 
    * **Teorías:** Teoría de la Autodeterminación (SDT) modificada y Teoría Cognitiva Social. 
    * **Metodología:** Enfoque cuantitativo (324 estudiantes), técnica PLS-SEM. 
    * **Gaps:** Falta de análisis de efectos moderadores (género, edad) y enfoque longitudinal.
    """,
    "Caratiquit & Caratiquit (2023) - ChatGPT como soporte": """
    **RESUMEN:** Investiga los factores que determinan la motivación de estudiantes universitarios para el uso continuo de ChatGPT en el aprendizaje del idioma inglés en Malasia. 
    * **Teorías:** Teoría de la Autodeterminación (SDT) modificada y Teoría Cognitiva Social.
    """,
    "Castro et al. (2025) - Bachillerato en Ecuador": """
    **RESUMEN:** Analiza el impacto de la IA en la personalización del aprendizaje, motivación y rendimiento en bachillerato fiscal en Ecuador. 
    * **Teorías:** Aprendizaje adaptativo y analítica del aprendizaje. 
    * **Metodología:** Enfoque cuantitativo y descriptivo-explicativo. 
    * **Gaps:** Desafíos en equidad digital y falta de formación docente.
    """,
    "Galindo-Domínguez et al. (2025) - Adolescentes Españoles": """
    **RESUMEN:** Estudio longitudinal sobre el impacto de una asignatura de IA en las necesidades psicológicas básicas y la motivación intrínseca. 
    * **Teorías:** Teoría de la Autodeterminación (SDT). 
    * **Metodología:** Intervención de 7 meses con 50 estudiantes. 
    * **Gaps:** Muestra pequeña y ausencia de grupo control.
    """,
    "García-Allén et al. (2025) - GenAI en Canadá": """
    **RESUMEN:** Explora el impacto de la IA Generativa en la motivación y competencia comunicativa en un curso de español en Canadá. 
    * **Teorías:** Comunidad de Indagación. 
    * **Metodología:** Métodos mixtos (41 estudiantes). 
    * **Gaps:** Duración corta de la sesión (60 min).
    """,
    "Imran et al. (2025) - Universitarios Paquistaníes": """
    **RESUMEN:** Evalúa el impacto del aprendizaje personalizado mediante sistemas adaptativos de IA en la motivación y el rendimiento académico. 
    * **Teorías:** SDT y Teoría de la Carga Cognitiva. 
    * **Metodología:** Diseño cuasiexperimental (n=200). 
    * **Gaps:** Carencia de datos longitudinales.
    """,
    "Li et al. (2025) - Análisis de Redes": """
    **RESUMEN:** Analiza la estructura de red de la motivación de los estudiantes para aprender IA desde la perspectiva de la SDT.
    """,
    "Mohamed et al. (2025) - Facultades de Educación": """
    **RESUMEN:** Examina el potencial de la IA para motivar y mejorar el aprendizaje de estudiantes de Educación en Arabia Saudita, Egipto, España y Polonia. 
    * **Teorías:** Teoría de la Autodeterminación. 
    * **Metodología:** Diseño no experimental (n=455). 
    * **Gaps:** Variaciones por diferencias culturales no controladas.
    """
}

# Selector desplegable (Selectbox)
seleccion = st.selectbox("Selecciona una referencia para ver su resumen:", list(referencias.keys()))

# Mostrar contenido seleccionado
if seleccion:
    st.info(referencias[seleccion])
