# Taxis New York

<img src="images/logo_taxi.jpg" width="300" height="300">

## Contexto
En la ciudad de Nueva York, los servicios de taxis y viajes compartidos como Uber han transformado la movilidad urbana, ofreciendo una opción conveniente y accesible tanto para turistas como para locales. Estos servicios generan una gran cantidad de datos, que incluyen detalles sobre la ubicación de los vehículos, duración de los viajes, tarifas y cantidad de pasajeros. Esta información resulta invaluable para empresas que desean comprender mejor los patrones de demanda, los costos operativos y las oportunidades de expansión en el mercado del transporte de pasajeros.

Una empresa de transporte de media y larga distancia, con una sólida presencia en Manhattan, está evaluando la posibilidad de expandirse hacia el mercado de taxis y viajes compartidos. Para tomar una decisión informada, desean realizar un análisis exhaustivo que les permita abordar los siguientes aspectos:

- Optimización de la flota: Determinar la composición ideal de la flota, es decir, la proporción óptima de unidades eléctricas, de combustión interna e híbridas para satisfacer la demanda a lo largo del día.

- Minimización de costos operativos: Realizar un análisis detallado de los costos asociados a cada unidad, considerando el consumo de combustible o energía eléctrica, mantenimiento y seguros. El objetivo es identificar la unidad más eficiente en términos de costo por kilómetro recorrido.

- Reducción del impacto ambiental: Comparar las emisiones de CO2 entre vehículos de combustión interna y eléctricos, cuantificando el impacto ambiental y explorando el potencial de reducción de emisiones mediante la adopción de vehículos híbridos o eléctricos, como parte de una iniciativa verde para reducir la huella de carbono.

- Maximización de ingresos: El área de finanzas de la empresa considero predecir la demanda de viajes en función del horario y tipo de vehículo. La empresa busca ajustar tarifas y optimizar la asignación de vehículos para responder de manera eficiente a los picos de demanda, aumentando así los ingresos.

- Evaluacion de kpis: El primer kpi solicitado fue de la cantidad de CO2 emitido y el segundo fue de la cantidad de ganancia neta obtenida por la totalidad de los viajes.

Este enfoque permitirá a la empresa no solo optimizar su operación y controlar los costos, sino también mejorar su competitividad en un mercado dinámico como el transporte de pasajeros en Nueva York.

## Rol a desarrollar
El equipo deberá utilizar los datos disponibles sobre el consumo de combustible y otros aspectos de los vehículos para calcular costos por kilómetro recorrido. Estos cálculos ayudarán a la empresa a prever los gastos operativos, que son fundamentales para elaborar presupuestos precisos para su flota. Además, el equipo deberá entrenar modelos predictivos para estimar la cantidad de viajes que podrian llegar a tener cada unidad, lo cual permitirá a la empresa optimizar su operación y maximizar sus ingresos.


## Objetivos

Los **objetivos** que requiere la empresa son:

- Optimizar la flota
- Minimizar costos operativos
- Evaluar el impacto ambiental de los tipos de vehiculos
- Predecir la demanda de viajes
- Evaluar los kpis


Ademas uno de los gerentes pidio realizar un **tablero** interactivo para expandir el analisis ademas de poder visualizar los kpis propuestos por la empresa.

La empresa tambien requiere proyectar su flota sobre los datos de TLC, considerando que su flota se compone por:
50% de las unidades(taxis) son de combustion interna, 30% de unidades son electricas y 20% son hibridos(plug-in).

## Recopilacion de datos

Los datos seran extraidos de la pagina oficial de TLC. 
Encontramos los datos en formato parquet, lo cual es conveniente para el desarrollo del proyecto debido a lo comprimido que estan estos datos ademas de que se encuentran en el formato necesario a utilizar es decir de tipo tabla.

Se implementa un proceso ETL el cual se desarrollara luego.

## Herramientas utilizadas:

### AWS

- Amazon Elastic Compute Cloud(EC2)
- S3
- SageMaker
- Amazon QuickSight

### Python

- Pandas, Numpy, pyarrow
- Matplotlib, Seaborn
- Sklearn, Autoregresive Models


## Variables sinteticas

- Desgaste = Indica el desgaste vehicular expresado en dolares dependiendo de la distancia del viaje.
- fuel_type = Indica el tipo de energia que consume el vehiculo.
- Trip_Duration: Duracion de viajes (Continua)
- Service: Viajes inter e intra boroughs(categorica)
- Labor: Servicio del empleado


## Indicadores

- Días, días de la semana y semanas con mas viajes
- % payments types
- Borough con mayor/menor cantidad de viajes
- price_per_km: Expresa el costo en dolares por km realizado por la unidad(varia en funcion del tipo de vehiculo).

## Metricas y predicciones

- Monto total del viaje.
- Cantidad de viajes diarios
- Distancia del viaje.




Este análisis permitirá a la empresa tomar decisiones bien fundamentadas sobre la viabilidad de su expansión al sector del transporte de pasajeros en automóviles, mejorando su rentabilidad y eficiencia operativa.



links

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

https://github.com/capitanfeeder/Proyecto-Taxis-NYC

https://github.com/soyHenry/PF_DS/blob/FULL-TIME/Proyectos/nyc_taxis%2Bco2.md