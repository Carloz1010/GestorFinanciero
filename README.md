# Sistema de Gestión Financiera Personal

Este proyecto es una aplicación de **Gestión Financiera Personal** desarrollada en **Python** utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)** y la biblioteca **CustomTkinter** para crear una interfaz gráfica de usuario interactiva. El objetivo principal del sistema es permitir a los usuarios gestionar sus ingresos, gastos y planificación financiera de manera sencilla y efectiva.

## Descripción del Proyecto

El sistema permite a los usuarios:

- Gestionar **ingresos y gastos**, asignándoles categorías y visualizando el balance.
- Realizar **proyecciones financieras**, calculando el dinero disponible diariamente.
- **Planificar gastos futuros**, ajustando el monto disponible y confirmando los gastos a largo plazo.
- **Generar reportes visuales** con gráficos interactivos y exportarlos en formato **PDF**.

## Estructura del Proyecto

### 1. **Modelo**
   - **Clase `Presupuesto`**: Maneja los ingresos, gastos y categorías de gastos. Permite agregar ingresos, agregar gastos y calcular la proyección diaria de dinero disponible.

### 2. **Vista**
   - **Clase `App`**: Interfaz gráfica desarrollada con **CustomTkinter** que permite al usuario interactuar con el sistema de manera sencilla. Los usuarios pueden agregar o eliminar ingresos y gastos, ver resúmenes financieros y generar reportes visuales.

### 3. **Controlador**
   - **Archivo `controller.py`**: Actúa como el punto de entrada al sistema, inicializando la aplicación y coordinando la interacción entre la vista y el modelo.

## Características

- **Gestión de Ingresos y Gastos**: 
  - Agregar, eliminar y categorizar ingresos y gastos.
  - Visualizar un resumen del estado financiero actual.
  
- **Proyección Financiera**: 
  - Calcular la proyección diaria del dinero disponible en función de los días restantes en el mes.

- **Generación de Reportes Visuales**: 
  - Generar gráficos de barras y pie charts con el desglose de los ingresos, gastos y los gastos futuros proyectados.
  - Exportar los reportes visuales en formato PDF.

- **Interfaz Intuitiva**: 
  - La interfaz está diseñada para ser fácil de usar, permitiendo a los usuarios gestionar su dinero de manera eficiente.

## Instalación

Para ejecutar este proyecto, necesitas tener **Python 3.x** instalado en tu máquina. Además, deberás instalar las siguientes bibliotecas:

1. **CustomTkinter**: Para la creación de la interfaz gráfica.
2. **Matplotlib**: Para la generación de gráficos visuales.

Puedes instalar estas dependencias usando `pip`:

```bash
pip install customtkinter matplotlib
```
## Uso

Clona este repositorio en tu máquina:

```bash
git clone https://github.com/Carloz1010/GestorFinanciero.git
```

Ejecuta el archivo `controller.py` para iniciar la aplicación:

```bash
  python controller.py
```


## Authors

- [@Carloz1010](https://github.com/Carloz1010)

