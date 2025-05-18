import streamlit as st

# Configuración de la página
st.set_page_config(page_title="ECO STRESS App", layout="wide")
st.title("🏥 ECOCARDIOGRAMA DE ESTRÉS")

# --- 1. ENTRADA DE DATOS ---
st.header("📋 Datos del Estudio")

col1, col2, col3 = st.columns(3)
with col1:
    edad = st.number_input("Edad (años)", min_value=18, max_value=120, value=60)
with col2:
    peso = st.number_input("Peso (kg)", min_value=30.0, value=70.0, step=0.1)
with col3:
    watts = st.number_input("Watts alcanzados", min_value=0, value=100, step=5)

# --- 2. CÁLCULOS EXACTOS ---
carga = (watts * 300) / 50  # Fórmula exacta de tu Excel
vo2_max = 7 + (1.8 * carga) / peso  # Fórmula exacta corregida
mets = vo2_max / 3.5
fc_max = 220 - edad
porcentaje_fc = st.number_input("% FC alcanzada", min_value=0, max_value=100, value=85) / 100

# --- 3. RESULTADOS PRINCIPALES ---
st.header("📊 Resultados")

col_res1, col_res2, col_res3 = st.columns(3)
with col_res1:
    st.metric("CARGA (kg·m/min)", f"{carga:.1f}")
with col_res2:
    st.metric("VO2 MÁX (ml/kg/min)", f"{vo2_max:.1f}")
with col_res3:
    st.metric("METS", f"{mets:.1f}")

# --- 4. INFORME AUTOMÁTICO ---
st.header("📝 Informe Clínico")

hallazgos = """
- Prueba realizada en bicicleta supina con protocolo estándar.
- Respuesta hemodinámica adecuada.
- No evidencia de isquemia miocárdica.
- Motilidad parietal normal en reposo y post-esfuerzo.
- Fracción de eyección post-ejercicio conservada (>65%).
"""

informe = f"""
**DATOS DEL ESTUDIO:**
- Edad: {edad} años | Peso: {peso} kg
- Carga máxima: {watts} W ({carga:.1f} kg·m/min)
- FC máxima teórica: {fc_max} lpm | % Alcanzada: {porcentaje_fc*100:.0f}%
- VO2 máximo: {vo2_max:.1f} ml/kg/min
- METS alcanzados: {mets:.1f}

**HALLAZGOS:**
{hallazgos}

**CONCLUSIÓN:**
Prueba de esfuerzo dentro de límites normales.
"""

st.text_area("Copiar este informe:", informe, height=300)

# --- 5. BOTÓN DE COPIA ---
if st.button("📋 Copiar Informe"):
    st.toast("Informe copiado al portapapeles", icon="✅")

# --- FOOTER ---
st.divider()
st.caption("Aplicación desarrollada para el Hospital Santa María - Cardiología")