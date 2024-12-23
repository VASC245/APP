import streamlit as st

menu = st.sidebar.radio(
    "Seleccione una opción: ",
    ("Registrar Ingresos", "Registrar Gastos", "Reportes")
)

if menu == "Registrar Ingresos":
    options = st.selectbox("Seleccione una opción: ",("Efectivo, Tarjeta, Transferencia", "Chicha, Jamaicas", "Bazar", "Galletas, Pellet"))
    if options == "Efectivo, Tarjeta, Transferencia":
        with st.form(key= "money", clear_on_submit= True):
            fecha = st.date_input("Ingrese la fecha del dia: ")
            efectivo = st.number_input("Ingrese lo recaudado en efectivo: ")
            tarjeta = st.number_input("Ingrese lo recaudado en tarjeta: ")
            transferecnia = st.number_input("Ingrese lo recaudado en transferencia: ")
            suma = efectivo + tarjeta + transferecnia
            resultado_suma = st.write(f"Se registro: {suma} en ventas en la fecha: {fecha} .")
            st.form_submit_button("Guardar")
    
    if options == "Chicha, Jamaicas":
        with st.form(key="jugos", clear_on_submit= True):
            fecha2 = st.date_input("Ingrese la fecha del dia: ")
            #Jamaicas
            st.subheader("Jamaica")
            vaso_jamaica = st.number_input("Ingrese el número de Vasos de Jamaicas vendidos: ")
            media_jarra_jamaica = st.number_input("Ingrese le número de Media Jarra de Jamaica vendidos: ")
            jarra_jamaica = st.number_input("Ingrese le número de Jarras de Jamaica vendidos: ")
             
            #Calculo de jamaicas
            total_jamaica_vasos = vaso_jamaica * 1.50
            total_jamaica_med_jarra = media_jarra_jamaica * 3.00
            total_jamaica_jarra = jarra_jamaica * 5.00
            #st.write(f"Vasos de Jamaica ingresados: {vaso_jamaica}, en dinero es igual a: {total_jamaica_vasos}")
            #st.write(f"Medias Jarras de Jamaica ingresadas: {media_jarra_jamaica}, en dinero es igual a: {total_jamaica_med_jarra}")
            #st.write(f"Jarras de Jamaica ingresadas: {jarra_jamaica}, en dinero es igual a: {total_jamaica_jarra}")

            #Chichas
            st.subheader("Chicha")
            vaso_chicha= st.number_input("Ingrese el número de Vasos de Chicha vendidos: ")
            media_jarra_chicha = st.number_input("Ingrese le número de Media Jarra de Chicha vendidos: ")
            jarra_chicha = st.number_input("Ingrese le número de Jarras de Chicha vendidos: ")

            #Calculo de chichas
            total_chicha_vasos = vaso_chicha * 1.50
            total_chicha_med_jarra = media_jarra_chicha * 3.00
            total_chicha_jarra = jarra_chicha * 6.00
            #st.write(f"Vasos de Chicha ingresados: {vaso_chicha}, en dinero es igual a: {total_chicha_vasos}")
            #st.write(f"Medias Jarras de Chicha ingresadas: {media_jarra_chicha}, en dinero es igual a: {total_chicha_med_jarra}")
            #st.write(f"Jarras de Chicha ingresadas: {jarra_chicha}, en dinero es igual a: {total_chicha_jarra}")


            st.form_submit_button("Guardar")

if menu == "Registrar Gastos":
    opciones = st.selectbox("Seleccione un opción", ("Empleados", "Carne","Cuero","Granos","Lacteos", "Vegetales", "Bebidas", "Servicios Basicos", "Articulos de limpieza", "Otros gastos"))
   
    if opciones == "Empleados":
        with st.form(key="empleados", clear_on_submit=True):
            fecha3 = st.date_input("Ingresa la fecha actual: ")
            pago_empleado1 = st.number_input("Registre lo pagado a Emerzon: ")
            pago_empleado2 = st.number_input("Registre lo pagado a Amelia: ")
            pago_empleado3 = st.number_input("Registre lo pagado a Balto: ")
            st.form_submit_button("Guardar")
    if opciones == "Carne":
        col1 , col2 , col3 = st.columns(3)
        with col1:
            st.header("Proalimec")
            gasto_proalimec = st.number_input("Registre lo pagado:")
            uploaded_files = st.file_uploader( "Choose a CSV file", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("Nombre de archivo:", uploaded_file.name)
        with col2:
            st.header("Pronaca")
            gasto_pronaca = st.number_input("Registre lo pagado: ")

        with col3:
            st.header("Sr. Espinoza")
            gasto_espinoza = st.number_input("Registre lo pagado")
    


    if opciones == "Cuero":
        with st.form(key="cuero", clear_on_submit= True):
            cuero = st.number_input("Registre lo pagado de cuero: ")
            chicharron = st.number_input("Registre lo pagado de chicharron: ")
            st.form_submit_button("Guardar")

    if opciones == "Granos":
        with st.form(key="cereales", clear_on_submit= True):
            mote = st.number_input("Ingrese lo pagado de mote: ")
            tostado = st.number_input("Ingrese lo pagado de tostado: ")
            canguil = st.number_input("Ingrese lo pagado de canguil: ")
            sal = st.number_input("Ingrese lo pagado de sal: ")
            azucar = st.number_input("Ingrese lo pagado de azucar: ")
            royal = st.number_input("Ingrese lo pagado de royal: ")
            harina = st.number_input("Ingrese lo pagado de harina: ")
            huevos = st.number_input("Ingrese lo pagado de huevos: ")
            st.form_submit_button("Guardar")

    if opciones == "Articulos de limpieza":
        pass

    if opciones == "Vegetales":
        with st.form(key="vegetales", clear_on_submit= True):
            aji = st.number_input("Ingrese lo pagado de ají: ")
            cebolla = st.number_input("Ingrese lo pagado de cebolla: ")
            papa = st.number_input("Inrese lo pagado de papa: ")
            platano = st.number_input("Ingrese lo pagado de plátano: ")
            tomate_arbol = st.number_input("Ingrese lo pagado de tomate de arbol: ")
            cebolla_blanca = st.number_input("Ingrese lo pagado de cebolla blanca: ")
            st.form_submit_button("Guardar")
