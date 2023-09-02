import matplotlib.pyplot as plt
import seaborn as sns
#Funciones creadas para aplicaar a la prueba:

#Fucnion para graficar histogramas
def histograma(dataframe):
    '''
    Función de histograma entregando Dataframe.
    
        Parameters: Dataframe.
        
        Returns: Histograma con información del dataframe y sus columnas.              
                       
    '''
    for col in dataframe.columns:
        plt.figure(figsize=(15,5))
        sns.histplot(dataframe[col])
        plt.title(f'Histograma de {col}')
        plt.xticks(rotation=55)
        plt.show()


#Función que convierte dtype desde objet a integrer
def convierte_objeto_en_int (dataframe, nombre_columna):
    '''
    Convierte los type de la columna desde objeto a integrer.
    
        Parameters: Dataframe : Nombre del dataframe
                    nombre_columna: Nombre de columna a convertir.
        
        Returns: type en integrer (int)
    
    '''
    
    type_df= dataframe[nombre_columna].dtypes
    
    if type_df == 'object':
        dataframe[nombre_columna] = dataframe[nombre_columna].astype(int)
        

