# DASI-2023-2024
# Predicción de la Producción de Energías Renovables utilizando Aprendizaje Automático

## Introducción

Desde el inicio a partir de los años cincuenta de la informática como campo de estudio, los científicos y matemáticos empezaron a plantearse de forma realista si era posible crear una máquina que pudiese imitar, o incluso superar, la inteligencia humana. A lo largo de las décadas siguientes se producen desarrollos tecnológicos notables, tales como la invención del transistor de unión, que permiten que la ciencia de la computación avance de forma exponencial, lo que posibilita los medios técnicos, y no solo teóricos, que respondan a dicho planteamiento, el cual dio origen al campo de la inteligencia artificial. Término acuñado en 1956 por John McCarthy durante una conferencia en Dartmouth.

El campo de la inteligencia artificial (IA) utiliza múltiples técnicas para tratar de imitar el pensamiento humano. En el presente trabajo se hará uso del aprendizaje automático, o machine learning. El objetivo principal de dicha rama es el de desarrollar técnicas que permitan a los computadores “aprender”. Es decir, se busca que las máquinas sean capaces de realizar tareas para las cuales no han sido diseñadas previamente de forma explicita, y que puedan extraer relaciones y conclusiones relevantes a partir de una serie de datos. Esta rama tiene que ver con la estadística, ya que se basa en el análisis de diversos datos. Sin embargo, desde el punto de vista de la ciencia de la computación, se introduce la preocupación por la complejidad computacional de los problemas. En otras palabras, la medida asintótica del tiempo que se puede tardar resolviendo un problema concreto. Existen diversos tipos de algoritmos, tales como el aprendizaje supervisado, no supervisado, por refuerzo, etc. En el presente trabajo se utilizará el enfoque del aprendizaje supervisado, el cual permite predecir el valor de una variable continua, en este caso, el IBEX 35, a partir de una serie de datos.

Las energías renovables surgen como una forma de energía sostenible y amigable con el medio ambiente, a la par que como una solución prometedora para satisfacer la inmensa demanda energética global. Sin embargo, la naturaleza intermitente y variable de estas fuentes, como la energía solar y la eólica, presentan desafíos significativos para la planificación y la gestión eficiente de la producción energética. En el año 2022, las energías renovables aportaron al PIB español diecinueve mil millones de euros, una cifra muy significativa y que va en aumento los últimos años. Las renovables representan ya en España casi el 50% del mix energético consumido diariamente. En este contexto, la informática y sus distintas herramientas pueden servir para proporcionar una solución confiable y estable a esta problemática. En concreto, las distintas técnicas de Inteligencia Artificial y de Aprendizaje automático pueden servir para proporcionar una forma adecuada de utilización de estos recursos.

El presente trabajo tiene por objetivo, por tanto, tratar de predecir la producción neta de energías renovables a partir de distintos datos meteorológicos, el PIB, o las producciones netas de electricidad.

## Caso de Negocio

Utilizar herramientas informáticas para la predicción de la producción neta de energías renovables. En concreto, se tratará de proporcionar a las empresas energéticas y a los planificadores de infraestructuras una herramienta precisa y confiable para gestionar y optimizar la producción de energía renovable.

Se desarrollará un sistema basado en aprendizaje automático que utilizará distintos datos, tales como:

- Las producciones netas de electricidad mediantes el uso de energías como la nuclear, la eólica o el gas natural, dadas por mes.
- El PIB en ese preciso momento.
- Las horas de sol, viento y capacidad hidráulica.

Deseamos predecir cuál debería ser la producción, en gigavatios, de energías renovables, en este caso la solar, la eólica y la hidráulica. Para ello, se entrenará un modelo con los datos mencionados anteriormente.

## Objetivos

En el presente trabajo, se trabajará con datos climatológicos y de producción energética de España, así como con datos del Producto Interno Bruto (PIB) del país. La finalidad es analizar y entender cómo las condiciones climatológicas y el nivel económico afectan la producción de energía en sus diferentes formas: nuclear, eólica, hidroeléctrica, solar, entre otras.

Para el desarrollo de esta práctica, se cuenta con un conjunto de datos climatológicos detallados de España. Estos datos incluyen parámetros como la temperatura, precipitación, horas de sol, velocidad del viento, entre otros factores climáticos, recopilados de manera mensual desde el año 2010 hasta el 2023. Estos datos son esenciales para analizar cómo las variaciones climáticas impactan en la producción de energía, particularmente en aquellas formas de energía que dependen directamente de las condiciones meteorológicas, como la energía solar y eólica.

Además, disponemos de información sobre la producción neta de energía de diferentes tipos (nuclear, eólica, hidroeléctrica, solar, etc.) también a lo largo de los meses desde el 2010 hasta el 2023. Estos datos nos permitirán observar las tendencias y fluctuaciones en la producción de cada tipo de energía y correlacionarlas con las condiciones climatológicas correspondientes.

Asimismo, se cuenta con datos del Producto Interno Bruto (PIB) de España, registrados de forma cuatrimestral durante el mismo periodo. El PIB es un indicador clave del estado económico del país y puede influir en la capacidad y la demanda de producción de energía. La relación entre el PIB y la producción de energía es un aspecto crucial de esta práctica, ya que un PIB más alto puede reflejar una mayor capacidad de inversión en infraestructuras energéticas y un mayor consumo de energía debido al crecimiento económico.

El objetivo final de esta práctica es multifacético y se desglosa en los siguientes puntos:

1. **Analizar la Relación entre Clima y Producción de Energía**: Determinar cómo las distintas condiciones climatológicas (temperatura, precipitación, horas de sol, velocidad del viento, etc.) afectan la producción de los diferentes tipos de energía (solar, eólica, hidroeléctrica, nuclear, etc.).
2. **Evaluar el Impacto Económico en la Producción Energética**: Investigar si existe una correlación entre el PIB de España y la producción de energía, considerando que un PIB más alto podría ser un indicador de una mayor capacidad y demanda de producción energética.
3. **Desarrollar Modelos Predictivos**: Utilizar los datos recopilados para desarrollar modelos que puedan predecir la cantidad de energía producida de cada tipo en función de las condiciones climatológicas y del PIB. Estos modelos pueden ser útiles para planificar la producción energética y para tomar decisiones informadas sobre inversiones en infraestructuras energéticas.

