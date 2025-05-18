import streamlit as st

st.title("📈 CÁLCULO DE METS - ECO STRESS")

# --- 1. DATOS DEL PACIENTE ---
col1, col2 = st.columns(2)
with col1:
    edad = st.number_input("Edad (años)", min_value=1, max_value=120)
    peso = st.number_input("Peso (kg)", min_value=30.0)
with col2:
    fc_basal = st.number_input("FC basal (lpm)", min_value=40, max_value=120)
    watts = st.number_input("Watts alcanzados", min_value=0)

# --- 2. CÁLCULOS AUTOMÁTICOS ---
fc_max = 220 - edad
fc_alcanzada = fc_max * 0.85
porcentaje_fc = (fc_basal * 1) / fc_max if fc_max > 0 else 0
vo2_max = 7 + ((1.8 * watts) / peso) if peso > 0 else 0
mets = vo2_max / 3.5

# --- 3. RESULTADOS ---
st.subheader("Resultados")
st.metric("METS", f"{mets:.1f}")
st.metric("% FC Alcanzada", f"{porcentaje_fc:.1%}")

# --- 4. INFORME AUTOMÁTICO ---
if st.button("Generar Informe ECO STRESS"):
    informe = f"""
    **PRUEBA DE ESFUERZO GRADUADA:**
    - FC basal: {fc_basal} lpm | FC esfuerzo: {fc_alcanzada:.0f} lpm
    - METS alcanzados: {mets:.1f}
    - VO2 máx: {vo2_max:.1f} ml/kg/min

    **HALLAZGOS:**
    - Prueba detenida por fatiga muscular. No presentó angor ni arritmias.
    - Curva tensional normal. Sin cambios en el segmento ST-T.
    - Motilidad parietal segmentaria normal en reposo y post-esfuerzo.
    - Fracción de eyección: 65% (reposo) → 75% (post-esfuerzo).
    """
    st.code(informe, language="text")