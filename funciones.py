import matplotlib.pyplot as plt



def get_borough(location_id):

    """
    Cuando se llama a la función get_borough y se le proporciona un location_id específico, la función busca 
    en el diccionario zones para encontrar en qué lista de identificadores se encuentra ese número.
    Si encuentra una coincidencia, significa que ha encontrado el distrito al que pertenece ese 
    location_id y devuelve el nombre del distrito.
    Si no encuentra ninguna coincidencia, devuelve "Unknown" (Desconocido), 
    indicando que no pudo determinar el distrito para ese identificador.
    """
    
    # Agrupamos los PULocationID y DOLocationID de acuerdo a su Borough correspondiente
    zones = {
        'Manhattan' : [4, 12, 13, 24, 41, 42, 43, 45, 48, 50, 68, 74, 75, 79, 87, 88, 90, 100, 103, 103, 103, 107, 113, 114, 116, 120, 125,
                      127, 128, 137, 140, 141, 142, 143, 144, 148, 151, 152, 153, 158, 161, 162, 163, 164, 166, 170, 186, 194, 202, 209, 211,
                      224, 229, 230, 231, 232, 233, 234, 236, 237, 238, 239, 243, 244, 246, 249, 261, 262, 263],
        'Brooklyn' : [11, 14, 17, 21, 22, 25, 26, 29, 33, 34, 35, 36, 37, 39, 40, 49, 52, 54, 55, 61, 62, 63, 65, 66, 67, 71, 72, 76, 77, 80,
                     85, 89, 91, 97, 106, 108, 111, 112, 123, 133, 149, 150, 154, 155, 165, 177, 178, 181, 188, 189, 190, 195, 210, 217, 222,
                     225, 227, 228, 255, 256, 257],
        'Queens' : [2, 7, 8, 9, 10, 15, 16, 19, 27, 28, 30, 38, 53, 56, 56, 64, 70, 73, 82, 83, 86, 92, 93, 95, 96, 98, 101, 102, 117, 121,
                   122, 124, 129, 130, 131, 132, 134, 135, 138, 139, 145, 146, 157, 160, 171, 173, 175, 179, 180, 191, 192, 193, 196, 197,
                   198, 201, 203, 205, 207, 215, 216, 218, 219, 223, 226, 252, 253, 258, 260],
        'Bronx' : [3, 18, 20, 31, 32, 46, 47, 51, 58, 59, 60, 69, 78, 81, 94, 119, 126, 136, 147, 159, 167, 168, 169, 174, 182, 183, 184,
                   185, 199, 200, 208, 212, 213, 220, 235, 240, 241, 242, 247, 248, 250, 254, 259],
        'Staten Island' : [5, 6, 23, 44, 84, 99, 109, 110, 115, 118, 156, 172, 176, 187, 204, 206, 214, 221, 245, 251],
        'EWR' : [1]}
    
    for borough, ids in zones.items():
        if location_id in ids:
            return borough
    return 'Unknown'

def time_series(df,variable,temporalidades):
    #columnas_tiempo = ['year','quarter','month','day_month','weekday','hour']
    plt.figure(figsize=(18, 14))
    y = 3
    x = 2
    z = 1
    for col in temporalidades:
        plt.subplot(x,y,z,facecolor = 'skyblue')
        z += 1
        df.groupby(col)[variable].sum().plot(kind='bar',color='blue')
        plt.title(f'{variable} vs {col}')
        plt.xlabel(col)
        plt.ylabel("kW")
        
        
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_val = df[feature_name].max()
        min_val = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_val) / (max_val - min_val)

    return result