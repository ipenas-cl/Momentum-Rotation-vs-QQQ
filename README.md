# Momentum Rotation vs QQQ

Este repositorio contiene un sistema de rotación de carteras que selecciona las mejores acciones del Nasdaq basadas en su momentum y las compara con el ETF QQQ. Si las acciones seleccionadas no superan el rendimiento del QQQ, todo el capital se transfiere al ETF para optimizar el rendimiento de la cartera.

## CaracterísticasCaracterísticas

Selección de activos: Selecciona hasta 5 empresas del Nasdaq utilizando un criterio de momentum (rendimiento reciente).
Frecuencia de rotación: La rotación de las empresas se realiza cada 3 meses.
Comparación con QQQ: Si las acciones seleccionadas no superan el rendimiento del ETF QQQ, el capital se transfiere completamente a QQQ.
Ponderación igual: Las empresas seleccionadas se ponderan de manera equitativa en la cartera (20% cada una si se seleccionan 5).
## Instalación

### Clona el repositorio a tu máquina local:

    git clone https://github.com/tu_usuario/momentum-rotation-vs-qqq.git
    cd momentum-rotation-vs-qqq
	
### Instala las dependencias necesarias utilizando pip:

    pip install -r requirements.txt
### Ejecución

Para ejecutar el sistema, simplemente corre el archivo principal **main.py**. Este descargará los datos históricos de las acciones seleccionadas y calculará los retornos tanto de la cartera rotada como del **ETF QQQ**.

    python main.py
### Estructura del Proyecto

    main.py: Contiene el código principal que implementa la lógica de la rotación de carteras y la comparación con el rendimiento del QQQ.
    requirements.txt: Archivo con las dependencias del proyecto, como yfinance, pandas y matplotlib.
    README.md: Este archivo de documentación.
## Requisitos
El proyecto está diseñado para ejecutarse con:

    Python 3.x
### Las siguientes librerías de Python:
    yfinance: Para obtener datos financieros históricos.
    pandas: Para el manejo de datos y cálculos.
    matplotlib: Para la visualización de gráficos.
### Parámetros Ajustables

En el código, puedes modificar los siguientes parámetros según tus necesidades:

    momentum_period: Establece el período para el cálculo del momentum (por defecto, 60 días).
    top_n: Define cuántas empresas serán seleccionadas (máximo 5).
    threshold: Determina cuándo rotar al ETF QQQ si las acciones seleccionadas no lo superan.
## Visualización de Resultados

El sistema genera un gráfico que compara el rendimiento acumulado de la cartera rotada frente al ETF QQQ. Aquí un ejemplo de cómo se vería:


## Contribuciones

Si tienes sugerencias o mejoras para el sistema, eres bienvenido a contribuir. Puedes hacerlo abriendo un pull request o iniciando una discusión en las issues del repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Revisa el archivo LICENSE para más detalles.

