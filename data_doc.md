
### Yellow Taxis
1. **VendorID**: Un código que representa al proveedor de tecnología (TPEP) que proporcionó el registro del viaje.
   - `1`: Creative Mobile Technologies, LLC
   - `2`: VeriFone Inc.

2. **tpep_pickup_datetime**: Fecha y hora en que se inició el viaje (se activó el taxímetro).

3. **tpep_dropoff_datetime**: Fecha y hora en que finalizó el viaje (se desactivó el taxímetro).

4. **Passenger_count**: Cantidad de pasajeros reportados para el viaje. Este dato es ingresado manualmente por el conductor.

5. **Trip_distance**: Distancia recorrida durante el viaje, reportada en millas.

6. **PULocationID**: ID de la zona de taxi TLC donde comenzó el viaje.

7. **DOLocationID**: ID de la zona de taxi TLC donde terminó el viaje.

8. **RateCodeID**: Código de la tarifa aplicada para el viaje.
   - `1`: Tarifa estándar
   - `2`: JFK
   - `3`: Newark
   - `4`: Nassau o Westchester
   - `5`: Tarifa negociada
   - `6`: Viaje en grupo

9. **Store_and_fwd_flag**: Indica si el registro del viaje fue almacenado temporalmente en la memoria del vehículo debido a problemas de conectividad.
   - `Y`: Sí, almacenado y enviado más tarde
   - `N`: No, enviado en tiempo real

10. **Payment_type**: Método de pago utilizado.
    - `1`: Tarjeta de crédito
    - `2`: Efectivo
    - `3`: Sin cargo
    - `4`: Disputa
    - `5`: Desconocido
    - `6`: Viaje anulado

11. **Fare_amount**: Monto de la tarifa calculada en base al tiempo y distancia por el taxímetro.

12. **Extra**: Cargos adicionales (como cargos por hora pico o nocturnos).

13. **MTA_tax**: Un impuesto de $0.50 para la Autoridad Metropolitana de Transporte (MTA).

14. **Improvement_surcharge**: Un recargo de $0.30 que se aplica desde 2015.

15. **Tip_amount**: Propinas recibidas, automáticamente registradas para pagos con tarjeta de crédito (las propinas en efectivo no se incluyen).

16. **Tolls_amount**: Total de peajes pagados durante el viaje.

17. **Total_amount**: El total del viaje, excluyendo las propinas en efectivo.

18. **Congestion_Surcharge**: Recargo por congestión recolectado para el programa de tarifas de congestión del Estado de Nueva York.

19. **Airport_fee**: Un recargo de $1.25 para recogidas en los aeropuertos LaGuardia y JFK.

### Ideas y métricas para generar:
- **Análisis del volumen de viajes**: Analizar el número total de viajes por día, semana o mes utilizando `tpep_pickup_datetime`.
- **Distribución del número de pasajeros**: Examinar cuántos pasajeros suelen viajar en cada viaje usando `Passenger_count`.
- **Distribución de la distancia de los viajes**: Analizar la distribución de las distancias de los viajes con `Trip_distance` y detectar tendencias para viajes cortos y largos.
- **Análisis de tarifas**: Explorar el promedio de tarifas por viaje utilizando `Fare_amount`, con desgloses por tipo de tarifa (`RateCodeID`) y método de pago (`Payment_type`).
- **Tendencias de zonas de recogida y destino**: Identificar las zonas de mayor tráfico para recogidas y destinos usando `PULocationID` y `DOLocationID`.
- **Preferencias de métodos de pago**: Comprender las preferencias de pago de los pasajeros a lo largo del tiempo con `Payment_type`.
- **Impacto de los recargos por congestión y peajes**: Calcular cómo afectan los recargos por congestión y los peajes al costo total de los viajes utilizando `Congestion_Surcharge` y `Tolls_amount`.
- **Tendencias en los aeropuertos**: Analizar los viajes hacia y desde aeropuertos utilizando `Airport_fee` y las zonas asociadas a estos.

Estas ideas pueden ayudarte a comprender mejor los patrones de uso de taxis en Nueva York, los desgloses de tarifas y las tendencias de pago.

Para elegir una variable a predecir en tu dataset de taxis amarillos de Nueva York, depende mucho del objetivo que quieras alcanzar, pero aquí hay algunas variables que podrían tener un gran valor y utilidad:

#### Luego de un exhaustivo analisis el area de Data Science requiere tener los datos listos y limpios para realizar predicciones sobre 2 variables:

1. **Total_amount (Monto total del viaje)**: Predecir el monto total del viaje es una de las opciones más prácticas y relevantes. Esta variable es un resumen de los diferentes factores que afectan el costo, como la distancia, el tiempo, los peajes, y otros cargos. Un modelo que prediga el costo total de un viaje podría ser útil para calcular tarifas antes de que el viaje ocurra, optimizar rutas, o incluso prever la demanda en ciertas áreas o momentos del día.

2. **Passenger_count (Cantidad de pasajeros)**: Aunque es una variable que depende de la entrada manual del conductor, podrías intentar predecir cuántos pasajeros probablemente utilizarán un taxi en función de la hora, la ubicación y otros factores. Esto podría ser útil para entender mejor el comportamiento de los clientes y optimizar el servicio.

3. **RateCodeID (Tipo de tarifa)**: Podrías también predecir el tipo de tarifa. Esto te permitiría anticipar si el viaje es estándar, a un aeropuerto (JFK, Newark), o negociado, lo cual podría ayudar a hacer predicciones de ingresos y optimizar las asignaciones de taxis para estos viajes.

4. **Pasaje intra o extra distrito**: predecir si el viaje sera dentro o fuera del mismo distrito.

# Dataset Fuel Rating
Tus datos parecen estar divididos en tres tipos de vehículos: vehículos convencionales (gasolina/diesel), híbridos enchufables, y vehículos eléctricos de batería. Cada fila de tus tablas representa un vehículo específico (identificado por el **año del modelo**, **marca**, **modelo** y otras características técnicas) y proporciona datos relacionados con su consumo de combustible o electricidad, así como sus emisiones de CO2. Te explico cómo podrías identificar si es un vehículo eléctrico o no, y cómo podrías utilizar los datos para estimar los costos de combustible o electricidad.

### Identificación del tipo de vehículo
1. **Vehículos convencionales (gasolina/diesel):**  
   - Aparecen en la primera tabla.
   - Variables como el **Fuel type** (tipo de combustible) te indicarán si el vehículo usa gasolina o diesel.
   - Otras variables clave: 
     - **City (L/100 km)**: Consumo en ciudad (litros por 100 km).
     - **Highway (L/100 km)**: Consumo en carretera.
     - **Combined (L/100 km)**: Consumo combinado.
     - **CO2 emissions (g/km)**: Emisiones de dióxido de carbono.

2. **Vehículos híbridos enchufables (plug-in hybrids):**  
   - Aparecen en la segunda tabla.
   - Se identifican por la variable **Type de carburant 1** (Tipo de combustible 1) y **Type de carburant 2** (Tipo de combustible 2). Estos vehículos combinan combustible tradicional (gasolina/diesel) con energía eléctrica.
   - Variables clave adicionales:
     - **Combinee Le/100 km**: Consumo combinado equivalente en litros por 100 km para electricidad.
     - **Autonomie 1 (km)**: Autonomía en modo eléctrico.
     - **Temps de recharge (h)**: Tiempo de recarga de la batería.

3. **Vehículos eléctricos de batería (battery-electric vehicles):**  
   - Aparecen en la tercera tabla.
   - Estos vehículos no usan combustible convencional, por lo que su consumo se mide en **kWh/100 km** (kilovatios-hora por cada 100 km).
   - Variables clave adicionales:
     - **City (kWh/100 km)** y **Highway (kWh/100 km)**: Consumo eléctrico en ciudad y carretera.
     - **Combined (kWh/100 km)**: Consumo combinado en kWh.
     - **Range (km)**: Autonomía total en modo eléctrico.
     - **Recharge time (h)**: Tiempo de recarga.

### Diferenciar los vehículos
- **Vehículos convencionales**: Si en la tabla se especifica un valor en las columnas de consumo en litros por 100 km (`City (L/100 km)`), puedes estar seguro de que no es un vehículo eléctrico.
- **Vehículos híbridos enchufables**: Si hay dos tipos de combustible mencionados (`Type de carburant 1` y `Type de carburant 2`), o si se menciona la autonomía en modo eléctrico o el tiempo de recarga, estás tratando con un híbrido enchufable.
- **Vehículos eléctricos**: Si el consumo se mide en **kWh/100 km**, es un vehículo eléctrico puro.

### Estimación del gasto en combustible o electricidad
1. **Vehículos convencionales:**  
   Para estimar el gasto de combustible, puedes usar el valor de consumo combinado en litros por cada 100 km (`Combined (L/100 km)`), multiplicado por el costo del combustible por litro y la distancia del viaje en kilómetros. Fórmula básica:
   ``` 
   Gasto_combustible = (Distancia_recorrida / 100) * Consumo_combustible * Precio_combustible_por_litro
   ```

2. **Vehículos híbridos enchufables:**  
   El cálculo es un poco más complejo, porque depende de cuánta distancia se recorre en modo eléctrico y cuánta en modo de combustible. Para el tramo eléctrico, usarías el consumo eléctrico equivalente en litros por 100 km (`Combinee Le/100 km`), y para el tramo de combustible, el consumo normal de combustible (`Ville (L/100 km)` o `Route (L/100 km)`).
   ``` 
   Gasto_total = (Distancia_en_modo_electrico / 100) * Consumo_electrico * Precio_electricidad + 
                (Distancia_en_modo_combustible / 100) * Consumo_combustible * Precio_combustible
   ```

3. **Vehículos eléctricos:**  
   El cálculo se basa en el consumo en **kWh/100 km** y el costo de la electricidad por kWh:
   ``` 
   Gasto_electricidad = (Distancia_recorrida / 100) * Consumo_electrico * Precio_kWh
   ```