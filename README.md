# Taxis New York

<img src="images/logo_taxi.jpg" width="300" height="300">

## Contexto
En la ciudad de Nueva York, los servicios de taxis y de viajes compartidos como Uber han transformado la movilidad urbana, proporcionando una opción conveniente y accesible tanto para turistas como para locales. Estos servicios generan una gran cantidad de datos, incluyendo detalles sobre la ubicación de los vehículos, la duración de los viajes, las tarifas y la cantidad de pasajeros. Esta información es invaluable para empresas que desean comprender mejor los patrones de demanda, los costos operativos y las oportunidades de expansión en el mercado del transporte de pasajeros.

Un cliente que maneja una empresa de transporte que actualmente opera en el sector de micros de media y larga distancia ubicada en Manhattan está evaluando la posibilidad de expandirse hacia el transporte de pasajeros en automóviles y necesita evaluar los costes de transportar los pasajeros en autos electricos o a combustion interna. Con el objetivo de maximizar sus ingresos y controlar los costos operativos, están interesados en realizar ademas un análisis preliminar sobre el uso, los costos de combustible de los vehículos que operan en Nueva York y la emision de CO2 generada. Quieren entender cómo se relacionan variables como el tipo de vehículo, el consumo de combustible y los costos por kilómetro recorrido, con el fin de tomar decisiones estratégicas sobre su inversión en este sector.

El area de finanzas de la empresa de nuestro cliente, consideraron primero estimar cuantos viajes pudieran llegar a realizarse durante el proximo dia, en que horarios e intentando diferenciar si esos viajes van a ser dentro del distrito local(Manhattan) o fuera del distrito y segundo como parte de la iniciativa de reducir el impacto al medio ambiente consideraron realizar una comparacion entre la emision de co2 de vehiculos que utilizan combustion interna contra la emision que generan vehiculos hibridos.


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
- Duracion de viajes (Continua)
- Viajes inter e intra boroughs(categorica)

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