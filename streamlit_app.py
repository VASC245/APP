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
    opciones = st.selectbox("Seleccione un opción", ("Empleados", "Carne", "Vegetales", "Colas, Cerveza y Agua", "Servicios Basicos", "Articulos de limpieza", "Otros gastos"))
    if opciones == "Empleados":
        pass

    if opciones == "Servicios Basicos":
        pass

    if opciones == "Vegetales":
        pass

    if opciones == "Carne":
        pass

    if opciones == "Colas, Cerveza y Agua":
        pass

    if opciones == "Otros gastos":
        pass
