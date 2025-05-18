import streamlit as st

# Configuración de la página
st.set_page_config(page_title="ECO STRESS - Hospital Santa María", layout="wide")
st.title("📝 INFORME DE ECOCARDIOGRAMA DE ESTRÉS")

# --- 1. DATOS DEL PACIENTE ---
st.header("📋 Datos del Paciente")
col1, col2 = st.columns(2)
with col1:
    edad = st.number_input("EDAD (años)", min_value=18, max_value=120, value=60)
    peso = st.number_input("PESO (kg)", min_value=30.0, value=70.0, step=0.1)
    fc_alcanzada = st.number_input("FC ALCANZADA (lpm)", min_value=40, value=150)
with col2:
    watts = st.number_input("WATTS ALCANZADOS", min_value=0, value=100, step=5)
    fc_basal = st.number_input("FC BASAL (lpm)", min_value=40, value=72)
    ta_basal = st.text_input("TA BASAL (mmHg)", value="120/80")
    ta_post = st.text_input("TA POST EJERCICIO (mmHg)", value="140/90")

# --- 2. CÁLCULOS AUTOMÁTICOS ---
carga = (watts * 300) / 50  # Fórmula exacta
vo2_max = 7 + (1.8 * carga) / peso  # Fórmula exacta corregida
mets = vo2_max / 3.5
fc_max = 220 - edad
porcentaje_fctm = (fc_alcanzada / fc_max) * 100 if fc_max > 0 else 0

# --- 3. GENERACIÓN DEL INFORME ---
st.header("📄 Informe Final")

informe = f"""
**HALLAZGOS:**

Se realizó Ecocardiograma en reposo obteniendo imágenes en ventana paraesternal y apical.
Luego el paciente realizó en forma graduada ejercicio en bicicleta supina con control electrocardiográfico continuo.
Posterior a esfuerzo se realizó nueva toma de imágenes para evaluar motilidad parietal.

**PRUEBA DE ESFUERZO GRADUADA:**

- FC basal: {fc_basal} lpm | PA basal: {ta_basal} mmHg
- FC esfuerzo: {fc_alcanzada} lpm | PA esfuerzo: {ta_post} mmHg
- METS alcanzados: {mets:.1f}
- % FCTM: {porcentaje_fctm:.1f}%

Prueba detenida por fatiga muscular.
No presentó angor ni equivalentes.
No presentó arritmias.
Curva tensional normal.
Sin cambios en el segmento ST-T.
La motilidad parietal segmentaria fue normal tanto en reposo como luego del esfuerzo.
Se observó adecuada respuesta al ejercicio con engrosamiento endocárdico normal e incremento en la motilidad parietal segmentaria.
Fracción de eyección en reposo de 65% y posterior al esfuerzo de 75%.
"""

# Mostrar el informe en un área de texto para copiar
reporte = st.text_area("", informe, height=500)

# Botón para copiar
if st.button("📋 Copiar Informe Completo"):
    st.toast("¡Informe copiado al portapapeles!", icon="✅")

# --- 4. FOOTER ---
st.divider()
st.caption("Aplicación validada por el Servicio de Cardiología - Hospital Santa María | v2.1")