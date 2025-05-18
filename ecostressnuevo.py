import streamlit as st

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

# --- 2. CÁLCULOS AUTOMÁTICOS ---
fc_max = 220 - edad
porcentaje_fc_alcanzada = (fc_esfuerzo / fc_max) * 100 if fc_max > 0 else 0
vo2_max = 7 + ((1.8 * watts) / peso) if peso > 0 else 0
mets = vo2_max / 3.5

# --- 3. RESULTADOS ---
with st.expander("📊 RESULTADOS CALCULADOS", expanded=True):
    st.subheader("Parámetros de Esfuerzo")
    col_res1, col_res2, col_res3 = st.columns(3)
    with col_res1:
        st.metric("FC MÁXIMA TEÓRICA", f"{fc_max:.0f} lpm")
        st.metric("% FC ALCANZADA", f"{porcentaje_fc_alcanzada:.1f}%")
    with col_res2:
        st.metric("VO2 MÁX", f"{vo2_max:.1f} ml/kg/min")
        st.metric("METS", f"{mets:.1f}")
    with col_res3:
        st.metric("CARGA (WATTS)", f"{watts} W")

# --- 4. INFORME COMPLETO (TEXTO EXACTO DEL EXCEL) ---
with st.expander("📝 INFORME COMPLETO", expanded=True):
    informe = f"""
    **HALLAZGOS:**
    - Se realizó Ecocardiograma en reposo obteniendo imágenes en ventana paraesternal y apical.
    - Luego el paciente realizó en forma graduada ejercicio en bicicleta supina con control electrocardiográfico continuo.
    - Posterior a esfuerzo se realizó nueva toma de imágenes para evaluar motilidad parietal.

    **PRUEBA DE ESFUERZO GRADUADA:**
    - FC basal: {fc_basal} lpm | PA basal: {ta_basal} mmHg
    - FC esfuerzo: {fc_esfuerzo} lpm | PA esfuerzo: {ta_esfuerzo} mmHg
    - METS alcanzados: {mets:.1f}
    - % FCTM: {porcentaje_fc_alcanzada:.1f}%

    **CONCLUSIONES:**
    - Prueba detenida por fatiga muscular.
    - No presentó angor ni equivalentes.
    - No presentó arritmias.
    - Curva tensional normal.
    - Sin cambios en el segmento ST-T.
    - La motilidad parietal segmentaria fue normal tanto en reposo como luego del esfuerzo.
    - Se observó adecuada respuesta al ejercicio con engrosamiento endocárdico normal e incremento en la motilidad parietal segmentaria.
    - Fracción de eyección en reposo de 65% y posterior al esfuerzo de 75%.
    """
    st.markdown(informe)
    
    # Botón para copiar
    st.button("📋 Copiar Informe al Portapapeles")

# --- 5. FOOTER ---
st.divider()
st.caption("Aplicación desarrollada para Cálculo de METS en ECO STRESS - Hospital Santa María")

# --- ESTILOS CSS PARA MEJORAR VISUALIZACIÓN ---
st.markdown("""
<style>
    [data-testid="stExpander"] .st-emotion-cache-1qrv0ga {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)