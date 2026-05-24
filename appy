import streamlit as st
import math

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA PREMIUM
st.set_page_config(page_title="Cota en Concreto - Calculadora de Moldes", page_icon="🧮", layout="centered")

# Inyección directa y segura de estilos COTA
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700&display=swap'); .stApp { background-color: #F6F1CE !important; color: #2F3161 !important; font-family: 'Inter', sans-serif; } h1 { color: #BA007C !important; font-family: 'Archivo Black', sans-serif; text-transform: uppercase; letter-spacing: -1px; margin-bottom: 5px !important; font-size: 32px !important; } h3, .highlight { color: #D4803F !important; font-family: 'Inter', sans-serif; font-weight: 700; margin-top: 0px !important; } div[data-testid='stVerticalBlockBorderWithStyling'] { background-color: #FFFFFF !important; padding: 20px !important; border-radius: 12px !important; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04) !important; border: 1px solid #EAEAEA !important; margin-bottom: 10px !important; } .section-title { color: #2F3161; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; } .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb='select'] { background-color: #F9F9F9 !important; color: #2F3161 !important; border: 1px solid #E2E8F0 !important; border-radius: 8px !important; } label p { color: #4A5568 !important; font-weight: 600 !important; font-size: 14px !important; } /* Estilo específico para los radio buttons inline */ div[data-testid='stMarkdownContainer'] p { color: #2F3161 !important; font-weight: 600; } div.stButton > button:first-child { background-color: #BA007C !important; color: #FFFFFF !important; border-radius: 8px; border: none !important; padding: 0.8rem 2.5rem; font-weight: 700; font-size: 16px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0px 4px 10px rgba(186, 0, 124, 0.2); transition: all 0.2s ease; width: 100%; margin-top: 10px; } div.stButton > button:first-child:hover { background-color: #D4803F !important; } .output-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; border-left: 5px solid #BA007C; color: #2F3161; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); }</style>", unsafe_allow_html=True)

# 2. ENCABEZADO DE LA APP
st.title("🧮 Calculadora de Moldes")
st.subheader("Cota en Concreto • Escuela de Emprendedoras")
st.write("Calculá los gramos exactos que necesitás para llenar tus piezas sin desperdiciar material.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BLOQUE 1: TÉCNICA Y TIPO DE MOLDE
with st.container(border=True):
    st.markdown('<div class="section-title">🎨 TÉCNICA Y TIPO DE MOLDE</div>', unsafe_allow_html=True)
    
    col_tec, col_mol = st.columns(2)
    with col_tec:
        tecnica = st.radio("Selecciona la mezcla:", ["Concreto Tradicional (1:1)", "Terrazzo Premium (1:1:1)"])
    with col_mol:
        tipo_molde = st.selectbox("Forma de tu molde:", ["Rectangular / Cuadrado", "Cilíndrico / Redondo", "Irregular (Cálculo por agua)"])

# 4. BLOQUE 2: MEDIDAS EN CENTÍMETROS
with st.container(border=True):
    st.markdown('<div class="section-title">📐 MEDIDAS DEL MOLDE</div>', unsafe_allow_html=True)
    
    volumen_cm3 = 0.0
    
    if tipo_molde == "Rectangular / Cuadrado":
        col_l, col_an, col_al = st.columns(3)
        with col_l:
            largo = st.number_input("Largo (cm):", min_value=0.0, value=10.0, step=0.5)
        with col_an:
            ancho = st.number_input("Ancho (cm):", min_value=0.0, value=10.0, step=0.5)
        with col_al:
            alto = st.number_input("Alto (cm):", min_value=0.0, value=5.0, step=0.5)
        volumen_cm3 = largo * ancho * alto
        
    elif tipo_molde == "Cilíndrico / Redondo":
        col_di, col_al_c = st.columns(2)
        with col_di:
            diametro = st.number_input("Diámetro total (cm):", min_value=0.0, value=10.0, step=0.5)
        with col_al_c:
            alto_c = st.number_input("Alto interno (cm):", min_value=0.0, value=5.0, step=0.5)
        radio = diametro / 2
        volumen_cm3 = math.pi * (radio ** 2) * alto_c
        
    elif tipo_molde == "Irregular (Cálculo por agua)":
        st.info("💡 Tip de Cota: Llená el molde con agua, volcá esa agua en tu balanza digital e ingresá abajo los gramos o mililitros (ml) que pesó.")
        agua_ml = st.number_input("Cantidad de agua que entró (ml o gramos):", min_value=0.0, value=250.0, step=10.0)
        volumen_cm3 = agua_ml

# 5. BOTÓN DE CÁLCULO Y RECETA EN GRAMOS
if st.button("CALCULAR RECETA EXACTA ⚖️"):
    if volumen_cm3 <= 0:
        st.warning("⚠️ Por favor, ingresá medidas mayores a cero.")
    else:
        # Densidad del material fraguado (2.2) + 10% de margen de desperdicio técnico
        mezcla_total_gramos = (volumen_cm3 * 2.2) * 1.10
        
        st.markdown("---")
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.markdown(f"### 📋 Receta para un volumen de {volumen_cm3:.1f} cm³")
        st.write(f"Peso total estimado de mezcla lista (con 10% de margen): **{int(mezcla_total_gramos)} gramos**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if tecnica == "Concreto Tradicional (1:1)":
            # Factor 1.175 equilibra el 35% de agua sobre el cemento
            peso_seco_total = mezcla_total_gramos / 1.175
            cemento = peso_seco_total / 2
            marmolina = peso_seco_total / 2
            agua = cemento * 0.35
            
            col_r1, col_r2, col_r3 = st.columns(3)
            col_r1.metric("🧱 Cemento", f"{int(cemento)} g")
            col_r2.metric("⏳ Marmolina", f"{int(marmolina)} g")
            col_r3.metric("💧 Agua", f"{int(agua)} g")
            
        else:
            # Terrazzo Premium (1:1:1)
            # Factor 1.116 equilibra el agua y la densidad mineral de la piedra
            peso_seco_total = mezcla_total_gramos / 1.116
            cemento = peso_seco_total / 3
            marmolina = peso_seco_total / 3
            piedras = peso_seco_total / 3
            agua = cemento * 0.35
            
            col_r1, col_r2, col_r3 = st.columns(3)
            col_r1.metric("🧱 Cemento", f"{int(cemento)} g")
            col_r2.metric("⏳ Marmolina", f"{int(marmolina)} g")
            col_r3.metric("💧 Agua", f"{int(agua)} g")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.metric("🪨 Piedras / Semillas", f"{int(piedras)} g")
            
        st.markdown("</div>", unsafe_allow_html=True)
