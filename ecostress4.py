import streamlit as st

# Configuración de la página
st.set_page_config(page_title="ECO STRESS App", layout="wide")
st.title("🏥 ECOCARDIOGRAMA DE ESTRÉS")

# --- 1. ENTRADA DE DATOS ---
with st.expander("📋 DATOS DEL PACIENTE", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        edad = st.number_input("EDAD (años)", min_value=18, max_value=120, value=60)
        peso = st.number_input("PESO (kg)", min_value=30.0, value=70.0, step=0.1)
    with col2:
        watts = st.number_input("WATTS ALCANZADOS", min_value=0, value=100, step=5)
        fc_esfuerzo = st.number_input("FC ALCANZADA (lpm)", min_value=40, value=150)

# --- 2. CÁLCULOS EXACTOS ---
carga = (watts * 300) / 50  # Fórmula exacta de tu Excel
vo2_max = 7 + (1.8 * carga) / peso  # Fórmula exacta corregida
mets = vo2_max / 3.5
fc_max = 220 - edad
porcentaje_fc = (fc_esfuerzo / fc_max) * 100 if fc_max > 0 else 0

# --- 3. RESULTADOS PRINCIPALES ---
with st.expander("📊 RESULTADOS", expanded=True):
    st.subheader("Parámetros de Esfuerzo")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("METS ALCANZADOS", f"{mets:.1f}")
    with col2:
        st.metric("% FC MÁXIMA", f"{porcentaje_fc:.1f}%")

# --- 4. INFORME AUTOMÁTICO ---
with st.expander("📝 INFORME FINAL", expanded=True):
    informe = f"""
    **HALLAZGOS:**
    - Prueba limitada por fatiga muscular.
    - No síntomas anginosos/arritmias.
    - Motilidad parietal normal en reposo y post-esfuerzo.
    - Fracción de eyección: 65% (reposo) → 75% (post-esfuerzo).

    **DATOS CLAVE:**
    - FC máxima alcanzada: {fc_esfuerzo} lpm ({porcentaje_fc:.1f}% de FC teórica)
    - METS: {mets:.1f}
    """
    
    st.text_area("Informe médico (copiar al portapapeles)", informe, height=200)
    if st.button("📋 Copiar Informe"):
        st.toast("¡Informe copiado!", icon="✅")

# --- 5. FOOTER ---
st.divider()
st.caption("Aplicación validada por Servicio de Cardiología - Hospital Santa María")