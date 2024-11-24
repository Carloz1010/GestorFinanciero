import customtkinter as ctk #pip install customtkinter
from tkinter import messagebox
from model import Presupuesto

#Definición de la clase principal de la aplicación
class App(ctk.CTk):
    def __init__(self):
        #Inicialización de la ventana principal
        super().__init__()
        self.title("Gestión de Finanzas")
        self.geometry("800x700")
        
        #Creación de la instancia de la clase Presupuesto
        self.presupuesto = Presupuesto()
        #Configuración del diseño en columnas con peso igual
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Título principal de la aplicación
        self.titulo = ctk.CTkLabel(self, text="Gestión de Finanzas")
        self.titulo.grid(row=0, column=1, padx=20, pady=5, sticky="nsew")

        #Salto de línea como espaciador
        self.saltoLinea = ctk.CTkLabel(self, text="")
        self.saltoLinea.grid(row=1, column=0, padx=0, pady=5, sticky="nsew")

        #Sección para agregar ingresos
        self.tituloIngresos = ctk.CTkLabel(self, text="Agrega tus ingresos")
        self.tituloIngresos.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")
        
        self.ingresoDescripcionEntry = ctk.CTkEntry(self, placeholder_text="Descripción Ingreso")
        self.ingresoDescripcionEntry.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        
        self.ingresoMontoEntry = ctk.CTkEntry(self, placeholder_text="Monto Ingreso")
        self.ingresoMontoEntry.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
        
        self.agregarIngresoButton = ctk.CTkButton(self, text="Agregar Ingreso", command=self.agregarIngreso)
        self.agregarIngresoButton.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
        
        #Sección para agregar gastos
        self.tituloGastos = ctk.CTkLabel(self, text="Agrega tus gastos")
        self.tituloGastos.grid(row=4, column=1, padx=20, pady=5, sticky="nsew")

        self.gastoDescripcionEntry = ctk.CTkEntry(self, placeholder_text="Descripción Gasto")
        self.gastoDescripcionEntry.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        
        self.gastoMontoEntry = ctk.CTkEntry(self, placeholder_text="Monto Gasto")
        self.gastoMontoEntry.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")
        
        self.agregarGastoButton = ctk.CTkButton(self, text="Agregar Gasto", command=self.agregarGasto)
        self.agregarGastoButton.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
        
        #Sección para eliminar ingresos y gastos
        self.tituloEliminar = ctk.CTkLabel(self, text="Elimina tus ingresos o gastos")
        self.tituloEliminar.grid(row=6, column=1, padx=20, pady=5, sticky="nsew")

        self.eliminarIngresoDescripcionEntry = ctk.CTkEntry(self, placeholder_text="Descripción Ingreso a Eliminar")
        self.eliminarIngresoDescripcionEntry.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")
        
        self.eliminarIngresoButton = ctk.CTkButton(self, text="Eliminar Ingreso", command=self.eliminarIngreso)
        self.eliminarIngresoButton.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")
        
        self.eliminarGastoDescripcionEntry = ctk.CTkEntry(self, placeholder_text="Descripción Gasto a Eliminar")
        self.eliminarGastoDescripcionEntry.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")
        
        self.eliminarGastoButton = ctk.CTkButton(self, text="Eliminar Gasto", command=self.eliminarGasto)
        self.eliminarGastoButton.grid(row=8, column=2, padx=10, pady=5, sticky="nsew")

        #Sección para mostrar ingresos y gastos
        self.labelIngresos = ctk.CTkLabel(self, text="Ingresos:")
        self.labelIngresos.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
        
        self.ingresosText = ctk.CTkTextbox(self, height=100, width=20)
        self.ingresosText.grid(row=10, column=0, padx=10, pady=5, sticky="nsew")
        
        self.labelGastos = ctk.CTkLabel(self, text="Gastos:")
        self.labelGastos.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")
        
        self.gastosText = ctk.CTkTextbox(self, height=100, width=20)
        self.gastosText.grid(row=10, column=1, padx=10, pady=5, sticky="nsew")

        #Etiqueta para mostrar el dinero disponible
        self.labelDineroDisponible = ctk.CTkLabel(self, text="Dinero Disponible: 0")
        self.labelDineroDisponible.grid(row=10, column=2, padx=10, pady=5, sticky="nsew")

        #Botón para generar reporte financiero
        self.reporteButton = ctk.CTkButton(self, text="Generar Reporte", command=self.generarReporte)
        self.reporteButton.grid(row=11, column=1, padx=10, pady=20, sticky="nsew")
        
        #Sección para mostrar proyección diaria
        self.diasRestantesEntry = ctk.CTkEntry(self, placeholder_text="Días Restantes")
        self.diasRestantesEntry.grid(row=12, column=0, padx=10, pady=5, sticky="nsew")
        
        self.proyeccionDiariaButton = ctk.CTkButton(self, text="Proyección Diaria", command=self.proyeccionDiaria)
        self.proyeccionDiariaButton.grid(row=12, column=1, padx=10, pady=5, sticky="nsew")
        
        #Actualización inicial de la vista
        self.actualizarVista()

    #Método que actualiza las vistas de ingresos, gastos y dinero disponible en la interfaz gráfica.    
    def actualizarVista(self):
        #Actualizar los campos de ingresos y gastos
        self.ingresosText.delete(1.0, "end") #Elimina todo el contenido del campo de texto de ingresos.
        for ingreso in self.presupuesto.ingresosFijos: #Itera sobre la lista de ingresos fijos almacenados en el presupuesto.
            self.ingresosText.insert("end", f"{ingreso['descripcion']}: {ingreso['monto']}\n") #Agrega cada ingreso al campo de texto con su descripción y monto.
        
        self.gastosText.delete(1.0, "end")#Elimina todo el contenido del campo de texto de gastos.
        for gasto in self.presupuesto.gastosFijos:#Itera sobre la lista de gastos fijos almacenados en el presupuesto.
            self.gastosText.insert("end", f"{gasto['descripcion']}: {gasto['monto']}\n")#Agrega cada gasto al campo de texto con su descripción y monto.
        
        self.labelDineroDisponible.configure(text=f"Dinero Disponible: {self.presupuesto.dineroDisponible}")#Actualiza la etiqueta de dinero disponible con el valor actual.

    def agregarIngreso(self):#Método que permite agregar un nuevo ingreso al presupuesto.
        descripcion = self.ingresoDescripcionEntry.get()#Obtiene el texto ingresado en la entrada de descripción del ingreso.
        monto = self.ingresoMontoEntry.get()#Obtiene el texto ingresado en la entrada del monto del ingreso.
        
        if not descripcion or not monto:#Verifica si alguno de los campos está vacío.
            messagebox.showerror("Error", "La descripción y el monto no pueden estar vacíos.")#Muestra un mensaje de error si los campos están vacíos.
            return#Termina la ejecución del método.
        
        try:
            monto = int(monto)#Intenta convertir el monto ingresado a un entero.
            self.presupuesto.agregarIngreso(descripcion, monto)#Agrega el ingreso al objeto de presupuesto.
            self.ingresoDescripcionEntry.delete(0, "end")#Limpia el campo de entrada de descripción del ingreso.
            self.ingresoMontoEntry.delete(0, "end")#Limpia el campo de entrada del monto del ingreso.
            self.actualizarVista()#Actualiza la vista de la interfaz gráfica.
        except ValueError as e:#Captura errores si la conversión del monto falla.
            messagebox.showerror("Error", str(e))#Muestra el error en un cuadro de mensaje.

    def agregarGasto(self):#Método que permite agregar un nuevo gasto al presupuesto.
        descripcion = self.gastoDescripcionEntry.get()#Obtiene el texto ingresado en la entrada de descripción del gasto.
        monto = self.gastoMontoEntry.get()#Obtiene el texto ingresado en la entrada del monto del gasto.
        
        if not descripcion or not monto:#Verifica si alguno de los campos está vacío.
            messagebox.showerror("Error", "La descripción y el monto no pueden estar vacíos.")#Muestra un mensaje de error si los campos están vacíos.
            return#Termina la ejecución del método.
        
        try:
            monto = int(monto)#Intenta convertir el monto ingresado a un entero.
            self.presupuesto.agregarGasto(descripcion, monto)#Agrega el gasto al objeto de presupuesto.
            self.gastoDescripcionEntry.delete(0, "end")#Limpia el campo de entrada de descripción del gasto.
            self.gastoMontoEntry.delete(0, "end")#Limpia el campo de entrada del monto del gasto.
            self.actualizarVista()#Actualiza la vista de la interfaz gráfica.
        except ValueError as e:#Captura errores si la conversión del monto falla.
            messagebox.showerror("Error", str(e))#Muestra el error en un cuadro de mensaje.

    def eliminarIngreso(self):#Método que permite eliminar un ingreso del presupuesto.
        descripcion = self.eliminarIngresoDescripcionEntry.get()#Obtiene el texto ingresado en la entrada de descripción del ingreso a eliminar.
        
        if not descripcion:#Verifica si el campo de descripción está vacío.
            messagebox.showerror("Error", "Debe ingresar una descripción válida para eliminar el ingreso.")#Muestra un mensaje de error si el campo está vacío.
            return#Termina la ejecución del método.
        
        if self.presupuesto.eliminarIngreso(descripcion):#Intenta eliminar el ingreso del presupuesto.
            self.eliminarIngresoDescripcionEntry.delete(0, "end")#Limpia el campo de entrada de descripción del ingreso a eliminar.
            self.actualizarVista()#Actualiza la vista de la interfaz gráfica.
        else:#Si no se encuentra un ingreso con la descripción proporcionada.
            messagebox.showerror("Error", "No se encontró un ingreso con esa descripción.")#Muestra un mensaje de error.

    def eliminarGasto(self):#Método que permite eliminar un gasto del presupuesto.
        descripcion = self.eliminarGastoDescripcionEntry.get()#Obtiene el texto ingresado en la entrada de descripción del gasto a eliminar.
        
        if not descripcion:#Verifica si el campo de descripción está vacío.
            messagebox.showerror("Error", "Debe ingresar una descripción válida para eliminar el gasto.")#Muestra un mensaje de error si el campo está vacío.
            return#Termina la ejecución del método.
        
        if self.presupuesto.eliminarGasto(descripcion):#Intenta eliminar el gasto del presupuesto.
            self.eliminarGastoDescripcionEntry.delete(0, "end")#Limpia el campo de entrada de descripción del gasto a eliminar.
            self.actualizarVista()#Actualiza la vista de la interfaz gráfica.
        else:#Si no se encuentra un gasto con la descripción proporcionada.
            messagebox.showerror("Error", "No se encontró un gasto con esa descripción.")#Muestra un mensaje de error.

    def generarReporte(self):#Método que genera un reporte financiero basado en el presupuesto.
        reporte = self.presupuesto.dineroDisponible#Obtiene el dinero disponible del presupuesto.

        if not reporte:#Verifica si no hay datos en el reporte.
            messagebox.showerror("Error", "Ingresa valores antes de exportar el reporte.")#Muestra un mensaje de error si no hay datos.
            return#Termina la ejecución del método.
        self.presupuesto.generarDashboard()#Genera el dashboard visual del reporte.

    def proyeccionDiaria(self):#Método que calcula la proyección diaria de dinero disponible.
        diasRestantes = self.diasRestantesEntry.get()#Obtiene el texto ingresado en la entrada de días restantes.
        
        if not diasRestantes:#Verifica si el campo de días restantes está vacío.
            messagebox.showerror("Error", "Debe ingresar el número de días.")#Muestra un mensaje de error si el campo está vacío.
            return#Termina la ejecución del método.
        
        try:
            diasRestantes = int(diasRestantes)#Intenta convertir los días restantes ingresados a un entero.
            if diasRestantes <= 0:#Verifica si el número de días es menor o igual a cero.
                raise ValueError("El número de días debe ser mayor a cero.")#Lanza un error si el número de días no es válido.
            proyeccion = self.presupuesto.proyeccionDiaria(diasRestantes)#Calcula la proyección diaria usando el presupuesto.
            messagebox.showinfo("Proyección Diaria", f"Se puede gastar {proyeccion} por día.")#Muestra la proyección diaria en un cuadro de mensaje.
        except ValueError as e:#Captura errores si la conversión de los días falla o el valor es inválido.
            messagebox.showerror("Error", str(e))#Muestra el error en un cuadro de mensaje.