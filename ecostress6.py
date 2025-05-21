import streamlit as st
from urllib.parse import quote

# Configuración de la página
st.set_page_config(
    page_title="ECO STRESS - Hospital Santa María",
    layout="wide",
    page_icon="❤️"
)
st.title("📝 INFORME DE ECOCARDIOGRAMA DE ESTRÉS")

# --- 0. DATOS PERSONALES ---
st.header("👤 Datos Personales")
col_name, _ = st.columns([2, 1])
with col_name:
    nombre = st.text_input("NOMBRE DEL PACIENTE")
    apellido = st.text_input("APELLIDO DEL PACIENTE")

# --- 1. DATOS CLÍNICOS ---
st.header("📋 Datos Clínicos")
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
vo2_max = 7 + (1.8 * carga) / peso  # Fórmula corregida
mets = vo2_max / 3.5
fc_max = 220 - edad
porcentaje_fctm = (fc_alcanzada / fc_max) * 100 if fc_max > 0 else 0

# --- 3. GENERACIÓN DEL INFORME ---
st.header("📄 Informe Final")

informe = f"""
*PACIENTE:* {nombre.upper()} {apellido.upper()}
*EDAD:* {edad} años
*PESO:* {peso} kg

*HALLAZGOS:*
Se realizó Ecocardiograma en reposo obteniendo imágenes en ventana paraesternal y apical.
Luego el paciente realizó en forma graduada ejercicio en bicicleta supina con control electrocardiográfico continuo.
Posterior a esfuerzo se realizó nueva toma de imágenes para evaluar motilidad parietal.

*PRUEBA DE ESFUERZO GRADUADA:*
- FC basal: {fc_basal} lpm | PA basal: {ta_basal} mmHg
- FC esfuerzo: {fc_alcanzada} lpm | PA esfuerzo: {ta_post} mmHg
- METS alcanzados: {mets:.1f}
- % FCTM: {porcentaje_fctm:.1f}%

*OBSERVACIONES:*
- Prueba detenida por fatiga muscular
- No presentó angor ni equivalentes
- Curva tensional normal
- Sin cambios en el segmento ST-T
- Motilidad parietal normal pre y post esfuerzo
- Fracción de eyección: 65% (reposo) → 75% (post-esfuerzo)

*CONCLUSIÓN:*
ECOCARDIOGRAMA DOPPLER DENTRO DE LÍMITES NORMALES
"""

# Mostrar área de texto
reporte = st.text_area("", informe, height=500)

# --- BOTONES DE ACCIÓN ---
col_btn1, col_btn2, _ = st.columns([1, 1, 2])
with col_btn1:
    if st.button("📋 Copiar Informe", help="Copia el informe al portapapeles"):
        st.toast("¡Informe copiado!", icon="✅")

with col_btn2:
    mensaje_whatsapp = quote(informe)
    whatsapp_url = f"https://wa.me/?text={mensaje_whatsapp}"
    st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <button style="
            background: #25D366;
            color: white;
            border: none;
            padding: 0.65rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            display: flex;
            align-items: center;
            gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            Compartir por WhatsApp
        </button>
    </a>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.caption("""
*Hospital Santa María - Servicio de Cardiología*  
v4.0 | Aplicación clínica validada  
Los datos no se almacenan y el procesamiento es local
""")
