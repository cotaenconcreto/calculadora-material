import streamlit as st
import math

# 1. CONFIGURACIÓN VISUAL INTEGRAL - ESTÉTICA COTA PREMIUM
st.set_page_config(page_title="Cota en Concreto - Calculadora de Moldes", page_icon="🧮", layout="centered")

# Inyección directa y segura de estilos COTA
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght=400;600;700&display=swap'); .stApp { background-color: #F6F1CE !important; color: #2F3161 !important; font-family: 'Inter', sans-serif; } h1 { color: #BA007C !important; font-family: 'Archivo Black', sans-serif; text-transform: uppercase; letter-spacing: -1px; margin-bottom: 5px !important; font-size: 32px !important; } h3, .highlight { color: #D4803F !important; font-family: 'Inter', sans-serif; font-weight: 700; margin-top: 0px !important; } div[data-testid='stVerticalBlockBorderWithStyling'] { background-color: #FFFFFF !important; padding: 20px !important; border-radius: 12px !important; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04) !important; border: 1px solid #EAEAEA !important; margin-bottom: 10px !important; } .section-title { color: #2F3161; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; } .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb='select'] { background-color: #F9F9F9 !important; color: #2F3161 !important; border: 1px solid #E2E8F0 !important; border-radius: 8px !important; } label p { color: #4A5568 !important; font-weight: 600 !important; font-size: 14px !important; } div[data-testid='stMarkdownContainer'] p { color: #2F3161 !important; font-weight: 600; } div.stButton > button:first-child { background-color: #BA007C !important; color: #FFFFFF !important; border-radius: 8px; border: none !important; padding: 0.8rem 2.5rem; font-weight: 700; font-size: 16px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0px 4px 10px rgba(186, 0, 124, 0.2); transition: all 0.2s ease; width: 100%; margin-top: 10px; } div.stButton > button:first-child:hover { background-color: #D4803F !important; } .output-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; border-left: 5px solid #BA007C; color: #2F3161; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); }</style>", unsafe_allow_html=True)

# 2. ENCABEZADO DE LA APP
st.title("🧮 Calculadora de Moldes")
st.subheader("Cota en Concreto • Escuela de Emprendedoras")
st.write("Calculá los gramos exactos que necesitás para llenar tus piezas sin desperdiciar material.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BLOQUE 1: TÉCNICA Y TIPO DE PIEZA
with st.container(border=True):
    st.markdown('<div class="section-title">🎨 TÉCNICA Y TIPO DE PIEZA</div>', unsafe_allow_html=True)
    
    col_tec, col_pie = st.columns(2)
    with col_tec:
        tecnica = st.radio("Selecciona la mezcla:", ["Concreto Tradicional (1:1)", "Terrazzo Premium (1:1:1)"])
    with col_pie:
        tipo_pieza = st.selectbox(
            "¿Qué pieza vas a fabricar?", 
            ["Maceta / Contenedor (Tiene hueco)", "Bandeja / Plato / Portavaso (Plano)", "Bacha de baño (Tiene hueco)", "Bloque Decorativo Macizo", "Molde Irregular (Cálculo por agua)"]
        )

# 4. BLOQUE 2: FORMA Y MEDIDAS DINÁMICAS
with st.container(border=True):
    st.markdown('<div class="section-title">📐 FORMA Y MEDIDAS DE LA PIEZA</div>', unsafe_allow_html=True)
    
    volumen_cm3 = 0.0
    error_espesor = False
    
    if tipo_pieza != "Molde Irregular (Cálculo por agua)":
        forma = st.selectbox("Forma visual de la pieza:", ["Cilíndrica / Redonda", "Cuadrada / Rectangular"])
        st.markdown("<br>", unsafe_allow_html=True)
        
        if forma == "Cilíndrica / Redonda":
            if tipo_pieza in ["Maceta / Contenedor (Tiene hueco)", "Bacha de baño (Tiene hueco)"]:
                col_di, col_al, col_es = st.columns(3)
                with col_di:
                    diametro_ext = st.number_input("Diámetro exterior (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_al:
                    alto_ext = st.number_input("Alto exterior (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_es:
                    espesor = st.number_input("Grosor del borde (cm):", min_value=0.1, value=1.0, step=0.1)
                
                if espesor >= (diametro_ext / 2):
                    st.error("❌ El grosor del borde no puede ser mayor o igual al radio de la pieza.")
                    error_espesor = True
                else:
                    vol_ext = math.pi * ((diametro_ext / 2) ** 2) * alto_ext
                    vol_int = math.pi * (((diametro_ext / 2) - espesor) ** 2) * (alto_ext - espesor)
                    volumen_cm3 = vol_ext - vol_int
            else:
                col_di, col_al = st.columns(2)
                with col_di:
                    diametro_ext = st.number_input("Diámetro total (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_al:
                    alto_ext = st.number_input("Alto / Espesor total (cm):", min_value=0.1, value=2.0, step=0.5)
                volumen_cm3 = math.pi * ((diametro_ext / 2) ** 2) * alto_ext

        elif forma == "Cuadrada / Rectangular":
            if tipo_pieza in ["Maceta / Contenedor (Tiene hueco)", "Bacha de baño (Tiene hueco)"]:
                col_la, col_an, col_al, col_es = st.columns(4)
                with col_la:
                    largo_ext = st.number_input("Largo exterior (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_an:
                    ancho_ext = st.number_input("Ancho exterior (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_al:
                    alto_ext = st.number_input("Alto exterior (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_es:
                    espesor = st.number_input("Grosor del borde (cm):", min_value=0.1, value=1.0, step=0.1)
                
                if (espesor * 2) >= largo_ext or (espesor * 2) >= ancho_ext:
                    st.error("❌ El grosor del borde es demasiado grande para las dimensiones exteriores.")
                    error_espesor = True
                else:
                    vol_ext = largo_ext * ancho_ext * alto_ext
                    vol_int = (largo_ext - (espesor * 2)) * (ancho_ext - (espesor * 2)) * (alto_ext - espesor)
                    volumen_cm3 = vol_ext - vol_int
            else:
                col_la, col_an, col_al = st.columns(3)
                with col_la:
                    largo_ext = st.number_input("Largo (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_an:
                    ancho_ext = st.number_input("Ancho (cm):", min_value=0.1, value=10.0, step=0.5)
                with col_al:
                    alto_ext = st.number_input("Alto / Espesor (cm):", min_value=0.1, value=2.0, step=0.5)
                volumen_cm3 = largo_ext * ancho_ext * alto_ext
    else:
        agua_ml = st.number_input("Cantidad de agua que entró (ml o gramos):", min_value=0.0, value=250.0, step=10.0)
        volumen_cm3 = agua_ml

# 5. BOTÓN DE CÁLCULO Y RECETA EN GRAMOS
if st.button("CALCULAR RECETA EXACTA ⚖️"):
    if error_espesor:
        st.error("⚠️ Corregí los espesores de las paredes para poder calcular.")
    elif volumen_cm3 <= 0:
        st.warning("⚠️ Por favor, ingresá medidas válidas mayores a cero.")
    else:
        # Ajustamos la densidad total del bloque según la técnica elegida
        if tecnica == "Concreto Tradicional (1:1)":
            densidad_mezcla = 2.1
        else:
            densidad_mezcla = 2.4 # El terrazo real con piedra es mucho más denso y pesado
            
        mezcla_total_gramos = (volumen_cm3 * densidad_mezcla) * 1.10
        
        st.markdown("---")
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.markdown(f"### 📋 Receta de Mezcla para tu {tipo_pieza}")
        st.write(f"Peso total estimado de mezcla lista (con 10% de margen): **{int(mezcla_total_gramos)} gramos**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if tecnica == "Concreto Tradicional (1:1)":
            # Relación de peso equilibrada 1:1 polvo + agua (35%)
            peso_seco_total = mezcla_total_gramos / 1.175
            cemento = peso_seco_total / 2
            marmolina = peso_seco_total / 2
            agua = cemento * 0.35
            
            col_r1, col_r2, col_r3 = st.columns(3)
            col_r1.metric("🧱 Cemento", f"{int(cemento)} g")
            col_r2.metric("⏳ Marmolina", f"{int(marmolina)} g")
            col_r3.metric("💧 Agua", f"{int(agua)} g")
            
        else:
            # TERRAZZO REAL (Equivalencia de volumen 1:1:1 pasada a gramos en balanza)
            # Si un vasito de cemento pesa X, la marmolina pesa X y la piedra pesa 2X.
            # Total de partes en peso = 1 + 1 + 2 = 4 partes.
            peso_seco_total = mezcla_total_gramos / 1.087 # Factor que equilibra el agua total
            
            partes_peso_total = 4.0
            unidad_gramos = peso_seco_total / partes_peso_total
            
            cemento = unidad_gramos * 1.0       # 1 parte de peso
            marmolina = unidad_gramos * 1.0     # 1 parte de peso
            piedras = unidad_gramos * 2.0       # 2 partes de peso (pesa el doble para llenar el mismo vaso)
            agua = cemento * 0.35               # Agua en base al cemento activo
            
            col_r1, col_r2, col_r3 = st.columns(3)
            col_r1.metric("🧱 Cemento", f"{int(cemento)} g")
            col_r2.metric("⏳ Marmolina", f"{int(marmolina)} g")
            col_r3.metric("💧 Agua", f"{int(agua)} g")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.metric("🪨 Piedras / Chips (Equivalente en volumen)", f"{int(piedras)} g")
            
        st.markdown("</div>", unsafe_allow_html=True)
