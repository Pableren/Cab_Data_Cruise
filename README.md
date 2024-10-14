# Taxis New York

<img src="images/logo_taxi.jpg" width="300" height="300">

## Contexto
En la ciudad de Nueva York, los servicios de taxis y viajes compartidos como Uber han transformado la movilidad urbana, ofreciendo una opción conveniente y accesible tanto para turistas como para locales. Estos servicios generan una gran cantidad de datos, que incluyen detalles sobre la ubicación de los vehículos, duración de los viajes, tarifas y cantidad de pasajeros. Esta información resulta invaluable para empresas que desean comprender mejor los patrones de demanda, los costos operativos y las oportunidades de expansión en el mercado del transporte de pasajeros.

Una empresa de transporte de media y larga distancia, con una sólida presencia en Manhattan, está evaluando la posibilidad de expandirse hacia el mercado de taxis y viajes compartidos. Para tomar una decisión informada, desean realizar un análisis exhaustivo que les permita abordar los siguientes aspectos:

- Optimización de la flota: Determinar el tamaño óptimo de la flota y la proporción adecuada entre vehículos eléctricos y de combustión interna para satisfacer la demanda prevista, tanto dentro como fuera de Manhattan.

- Minimización de costos operativos: Evaluar los costos de operación asociados con cada tipo de vehículo. Esto incluye el consumo de combustible, costos de mantenimiento, y el costo de la carga eléctrica para los vehículos eléctricos, con el objetivo de maximizar la eficiencia de la flota.

- Reducción del impacto ambiental: Comparar las emisiones de CO2 entre vehículos de combustión interna y eléctricos, cuantificando el impacto ambiental y explorando el potencial de reducción de emisiones mediante la adopción de vehículos híbridos o eléctricos, como parte de una iniciativa verde para reducir la huella de carbono.

- Maximización de ingresos: Predecir la demanda de viajes en función de las zonas geográficas (tanto dentro como fuera de Manhattan), horarios y tipo de vehículo. La empresa busca ajustar tarifas y optimizar la asignación de vehículos para responder de manera eficiente a los picos de demanda, aumentando así los ingresos.

El área de finanzas de la empresa también ha considerado una primera estimación sobre cuántos viajes podrían realizarse en un día típico, diferenciando entre los realizados dentro del distrito local de Manhattan y aquellos fuera de él. Además, este análisis preliminar incluiría una evaluación de los costos por kilómetro recorrido según el tipo de vehículo, ya sea eléctrico o de combustión interna, permitiendo una comparación directa de costos y emisiones.

Este enfoque permitirá a la empresa no solo optimizar su operación y controlar los costos, sino también mejorar su competitividad en un mercado dinámico como el transporte de pasajeros en Nueva York.


## Rol a desarrollar
El equipo deberá utilizar los datos disponibles sobre el consumo de combustible y otros aspectos de los vehículos para calcular costos por kilómetro recorrido. Estos cálculos ayudarán a la empresa a prever los gastos operativos, que son fundamentales para elaborar presupuestos precisos para su flota. Además, el equipo deberá entrenar modelos predictivos para estimar el Monto total del viaje, así como la Cantidad de pasajeros que podrían utilizar estos servicios en diferentes escenarios, lo cual permitirá a la empresa optimizar su operación y maximizar sus ingresos.


## Objetivos

Los **objetivos** que requiere la empresa son realizar un **presupuesto** de la proxima semana, obteniendo predicciones sobre cuantos viajes se realizaran y cuanto puede llegar a ser la distancia de cada viaje.

Ademas, la empresa requiere proyectar su flota sobre los datos de TLC, considerando que su flota se compone por:
50% de las unidades(taxis) son de combustion interna, 30% de unidades son electricas y 20% son hibridos(plug-in).

## Variables sinteticas

- Desgaste_CI: Expresa el costo en dolares que tendria el uso del vehiculo de combustion interna. (CI=Combustion Interna)
- Desgaste_E: Expresa el costo en dolares que tendria el uso del vehiculo electrico.
- Desgaste_H: Expresa el costo en dolares que tendria el uso del vehiculo hibrido.
- Trip_Duration: Duracion de viajes (Continua)
- Service: Viajes inter e intra boroughs(categorica)


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