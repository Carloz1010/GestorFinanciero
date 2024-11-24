import matplotlib.pyplot as plt #pip install matplotlib
import seaborn as sns #pip install seaborn

class Presupuesto:
    def __init__(self):
        self.__ingresosFijos = [] #Inicializa la lista de ingresos fijos.
        self.__gastosFijos = [] #Inicializa la lista de gastos fijos.

    #Métodos para agregar ingresos y gastos
    def agregarIngreso(self, descripcion, monto):
        self.agregarElementoFijo("Ingreso", descripcion, monto) #Llama a agregarElementoFijo para agregar un ingreso.

    def agregarGasto(self, descripcion, monto):
        self.agregarElementoFijo("Gasto", descripcion, monto) #Llama a agregarElementoFijo para agregar un gasto.

    #Métodos para eliminar ingresos y gastos.
    def eliminarIngreso(self, descripcion):
        try:
            self.eliminarElementoFijo("Ingreso", descripcion) #Llama a eliminarElementoFijo para eliminar un ingreso.
            return True #Devuelve True si se eliminó con éxito.
        except ValueError:
            return False #Devuelve False si ocurre un error al eliminar.

    def eliminarGasto(self, descripcion):
        try:
            self.eliminarElementoFijo("Gasto", descripcion) #Llama a eliminarElementoFijo para eliminar un gasto.
            return True #Devuelve True si se eliminó con éxito.
        except ValueError:
            return False #Devuelve False si ocurre un error al eliminar.

    #Método para el cálculo del dinero disponible.
    def calcularDineroDisponible(self):
        ingresosTotales = sum(i["monto"] for i in self.__ingresosFijos) #Suma todos los montos de los ingresos.
        gastosTotales = sum(g["monto"] for g in self.__gastosFijos) #Suma todos los montos de los gastos.
        return ingresosTotales - gastosTotales #Devuelve el dinero disponible (ingresos - gastos).

    #Método para la proyección diaria.
    def proyeccionDiaria(self, diasRestantes):
        dineroDisponible = self.calcularDineroDisponible() #Obtiene el dinero disponible.
        if diasRestantes > 0: #Verifica que los días restantes sean positivos.
            return round(dineroDisponible / diasRestantes) #Devuelve el cálculo de la proyección diaria.
        else:
            raise ValueError("Los días restantes deben ser un valor mayor que cero.") #Lanza un error si los días no son válidos.

    #Métodos para fenerar dashboard con gráficos mejorados.
    def generarDashboard(self):
        categoriasGastos = [g["descripcion"] for g in self.__gastosFijos] #Extrae las descripciones de los gastos.
        montosGastos = [g["monto"] for g in self.__gastosFijos] #Extrae los montos de los gastos.
        ingresosTotales = sum(i["monto"] for i in self.__ingresosFijos) #Calcula el total de ingresos.
        gastosTotales = sum(montosGastos) #Calcula el total de gastos.
        dineroDisponible = self.calcularDineroDisponible() #Obtiene el dinero disponible.

        #Configuración de estilo para gráficos.
        sns.set(style="whitegrid") #Establece el estilo del gráfico.
        plt.figure(figsize=(14, 7)) #Configura el tamaño de la figura.

        #Gráfico de pie para la proporción de ingresos y gastos.
        plt.subplot(1, 2, 1) #Configura la primera parte del gráfico (gráfico de pie).
        sizes = [ingresosTotales, gastosTotales] #Define los tamaños para ingresos y gastos.
        labels = ["Ingresos", "Gastos"] #Define las etiquetas para el gráfico de pie.
        colors = ["#4CAF50", "#FF5733"] #Define los colores para cada sección.
        explode = (0.1, 0)  #Explota la parte de "Ingresos" para destacar.

        #Función para mostrar el valor en el gráfico de pie.
        def func(pct, allvals):
            absolute = int(pct / 100. * sum(allvals)) #Calcula el valor absoluto a mostrar.
            return f"${absolute:,}\n({pct:.1f}%)" #Devuelve el texto con el valor y porcentaje.

        #Crear gráfico de pie con colores y etiquetas mejoradas.
        wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct=lambda pct: func(pct, sizes),
                                        colors=colors, startangle=90, explode=explode, 
                                        wedgeprops={"edgecolor": "black", "linewidth": 1})
        plt.title("Proporción de Ingresos y Gastos", fontsize=14, weight="bold") #Título del gráfico.
        plt.axis('equal')  #Hace el gráfico circular perfecto.
        for text in autotexts:
            text.set(size=12, color="white", weight="bold") #Ajusta las etiquetas del gráfico.

        #Gráfico de barras horizontales para la distribución de gastos.
        plt.subplot(1, 2, 2) #Configura la segunda parte del gráfico (gráfico de barras).
        bars = plt.barh(categoriasGastos, montosGastos, color="#FF5733", edgecolor='black', height=0.6) #Crea las barras.
        plt.title("Distribución de Gastos", fontsize=14, weight="bold") #Título del gráfico.
        plt.xlabel("Monto", fontsize=12) #Etiqueta del eje X.
        plt.ylabel("Categorías", fontsize=12) #Etiqueta del eje Y.
        plt.xticks(rotation=0) #Asegura que las etiquetas del eje X estén horizontales.
        
        #Agregar etiquetas con el valor de cada barra, en pesos y porcentaje.
        totalGastos = sum(montosGastos) #Calcula el total de los gastos.
        for bar in bars:
            xval = bar.get_width() #Obtiene el valor de cada barra.
            percentage = (xval / totalGastos) * 100 #Calcula el porcentaje de cada barra.
            plt.text(xval + 10, bar.get_y() + bar.get_height() / 2, 
                    f"${xval:,.2f}\n({percentage:.1f}%)", ha='left', va='center',
                    fontsize=10, color='black', weight='bold') #Agrega el texto a la barra.

        #Mejorar la distribución de los gráficos.
        plt.tight_layout() #Ajusta automáticamente el espaciado de los gráficos.
        plt.show() #Muestra el gráfico.

    #Getter para obtener los ingresos fijos y gastos fijos.
    @property
    def ingresosFijos(self):
        return self.__ingresosFijos

    @ingresosFijos.setter
    def ingresosFijos(self, ingresos):
        self.__ingresosFijos = ingresos

    @property
    def gastosFijos(self):
        return self.__gastosFijos

    @gastosFijos.setter
    def gastosFijos(self, gastos):
        self.__gastosFijos = gastos

    @property
    def dineroDisponible(self):
        return self.calcularDineroDisponible()
    
    #Función modelo para agregar un elemento.
    def agregarElementoFijo(self, tipo, descripcion, monto):
        #Normalizar tipo para evitar problemas de entrada.
        tipo = tipo.capitalize() #Asegura que el tipo de entrada se guarde en mayúscula inicial.
        
        if tipo not in ["Ingreso", "Gasto"]: #Verifica que el tipo sea válido.
            raise ValueError("Tipo no válido. Use 'Ingreso' o 'Gasto'.") #Lanza error si el tipo no es válido.
        
        if monto <= 0: #Verifica que el monto sea positivo.
            raise ValueError(f"El monto del {tipo} debe ser positivo.") #Lanza error si el monto no es válido.
        
        #Normalizar la descripción (hacerla insensible a mayúsculas/minúsculas y con primera letra mayúscula).
        descripcionNormalizada = descripcion.strip().lower() #Elimina espacios y convierte a minúsculas.
        descripcionFormateada = descripcion.strip().capitalize() #Formatea la descripción con la primera letra en mayúscula.

        #Seleccionar la lista correspondiente.
        lista = self.__ingresosFijos if tipo == "Ingreso" else self.__gastosFijos #Selecciona la lista de ingresos o gastos.
        
        #Verificar si la descripción ya existe.
        elemento_existente = next((e for e in lista if e["descripcion"].lower() == descripcionNormalizada), None) #Busca el elemento.
        
        if elemento_existente: #Si el elemento ya existe, actualizar el monto sumando el nuevo valor.
            elemento_existente["monto"] += monto
        else: #Si no existe, agregar el nuevo elemento.
            lista.append({"descripcion": descripcionFormateada, "monto": monto})

    #Función modelo para eliminar un elemento.
    def eliminarElementoFijo(self, tipo, descripcion):
        #Seleccionar la lista adecuada según el tipo.
        if tipo == "Ingreso":
            lista = self.__ingresosFijos #Selecciona la lista de ingresos.
        elif tipo == "Gasto":
            lista = self.__gastosFijos #Selecciona la lista de gastos.
        else:
            raise ValueError("Tipo no válido. Use 'Ingreso' o 'Gasto'.") #Lanza error si el tipo no es válido.

        #Buscar el elemento en la lista y eliminarlo.
        descripcionNormalizada = descripcion.strip().lower() #Normaliza la descripción para búsqueda.
        elemento = next((e for e in lista if e["descripcion"].lower() == descripcionNormalizada), None) #Busca el elemento.

        if elemento: #Si se encuentra el elemento, eliminarlo.
            lista.remove(elemento)
        else:
            raise ValueError(f"{tipo} no encontrado.") #Lanza error si no se encuentra el elemento.
