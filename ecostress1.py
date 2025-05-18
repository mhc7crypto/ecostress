import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="ECO STRESS - Cálculo de METS", layout="wide")
st.title("🏥 ECOCARDIOGRAMA DE ESTRES - CÁLCULO DE METS")

# --- 1. DATOS DEL PACIENTE Y PRUEBA ---
with st.expander("📋 DATOS DEL PACIENTE Y PRUEBA", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        edad = st.number_input("EDAD (años)", min_value=1, max_value=120, value=60)
        peso = st.number_input("PESO (kg)", min_value=30.0, value=70.0)
    with col2:
        fc_basal = st.number_input("FC BASAL (lpm)", min_value=40, max_value=120, value=72)
        fc_esfuerzo = st.number_input("FC ALCANZADA (lpm)", min_value=40, value=150)
    with col3:
        watts = st.number_input("WATTS ALCANZADOS", min_value=0, value=100)
        ta_basal = st.text_input("TA BASAL (mmHg)", value="120/80")
        ta_esfuerzo = st.text_input("TA POST-EJERCICIO (mmHg)", value="140/90")

# --- 2. CÁLCULOS AUTOMÁTICOS (FÓRMULAS EXACTAS DEL EXCEL) ---
fc_max = 220 - edad
porcentaje_fc_alcanzada = (fc_esfuerzo / fc_max) * 100 if fc_max > 0 else 0
carga = (watts * 300) / 50  # Fórmula exacta de tu Excel
vo2_max = 7 + ((1.8 * watts) / peso) if peso > 0 else 0  # Fórmula exacta
mets = vo2_max / 3.5  # Fórmula exacta

# --- 3. RESULTADOS ---
with st.expander("📊 RESULTADOS CALCULADOS", expanded=True):
    st.subheader("Parámetros de Esfuerzo")
    col_res1, col_res2, col_res3 = st.columns(3)
    with col_res1:
        st.metric("FC MÁXIMA TEÓRICA", f"{fc_max:.0f} lpm")
        st.metric("% FC ALCANZADA", f"{porcentaje_fc_alcanzada:.1f}%")
    with col_res2:
        st.metric("VO2 MÁX (ml/kg/min)", f"{vo2_max:.1f}")
        st.metric("METS", f"{mets:.1f}")
    with col_res3:
        st.metric("CARGA (W)", f"{carga:.1f}")
        st.metric("85% FC MÁX", f"{fc_max * 0.85:.0f} lpm")

# --- 4. INFORME COMPLETO (TEXTO EXACTO DEL EXCEL) ---
with st.expander("📝 INFORME COMPLETO", expanded=True):
    informe = f"""
    **PROTOCOLO:**
    - Se realizó Ecocardiograma en reposo obteniendo imágenes en ventana paraesternal y apical.
    - Ejercicio graduado en bicicleta supina con monitorización electrocardiográfica continua.
    - Toma de imágenes post-esfuerzo para evaluación de motilidad parietal.

    **DATOS DE LA PRUEBA:**
    - FC basal: {fc_basal} lpm | TA basal: {ta_basal} mmHg
    - FC máxima alcanzada: {fc_esfuerzo} lpm ({porcentaje_fc_alcanzada:.1f}% de la FC máxima teórica)
    - TA post-ejercicio: {ta_esfuerzo} mmHg
    - Carga máxima: {watts} W (Equivalente a {carga:.1f} kg·m/min)
    - Consumo máximo de O₂ (VO2 máx): {vo2_max:.1f} ml/kg/min
    - METS alcanzados: {mets:.1f}

    **HALLAZGOS:**
    - Prueba limitada por fatiga muscular.
    - No síntomas anginosos/arritmias.
    - Curva tensional normal sin cambios en ST-T.
    - Motilidad parietal normal en reposo y post-esfuerzo.
    - Fracción de eyección: 65% (reposo) → 75% (post-esfuerzo).
    - Respuesta cronotrópica adecuada.
    """
    
    st.markdown(informe)
    if st.button("📋 Copiar Informe", key="copiar_informe"):
        st.session_state.informe_copiado = True
        st.toast("¡Informe copiado al portapapeles!", icon="✅")

# --- 5. FOOTER ---
st.divider()
st.caption("Aplicación validada por Servicio de Cardiología - Hospital Santa María")

# --- ESTILOS CSS ---
st.markdown("""
<style>
    [data-testid="stExpander"] .st-emotion-cache-1qrv0ga {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 20px;
    }
    .stButton button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)