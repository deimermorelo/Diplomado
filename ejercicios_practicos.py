# Solucion al Taller sobre Regresiones 1
# Diplomado Python Aplicado a la Ingenieria UPB
# Autor: Deimer David Morelo Ospino
# ID: 502217
# Email: deimer.morelo@upb.edu.co

# Importamos las librerias que utilizaremos
import pandas as pd
from sklearn import linear_model as lm
import numpy as np

# Leemos el archivo csv con pandas y creamos el dataframe
cars_𝑑𝑓 = 𝑝d.𝑟𝑒𝑎𝑑_𝑐𝑠𝑣("cars.csv")

# Hacemos una lista de las variables independientes
𝑋 = cars_𝑑𝑓[['Volume', 'Weight', 'CO2']]

# Creamos la variable "conditions" con las diferentes marcas de autos contenidas en el dataframe  
conditions = [
    (cars_df["Car"] == "Audi"),
    (cars_df["Car"] == "BMW"),
    (cars_df["Car"] == "Fiat"),
    (cars_df["Car"] == "Ford"),
    (cars_df["Car"] == "Honda"),
    (cars_df["Car"] == "Hundai"),
    (cars_df["Car"] == "Mazda"),
    (cars_df["Car"] == "Mercedes"),
    (cars_df["Car"] == "Mini"),
    (cars_df["Car"] == "Mitsubishi"),
    (cars_df["Car"] == "Opel"),
    (cars_df["Car"] == "Skoda"),
    (cars_df["Car"] == "Suzuki"),
    (cars_df["Car"] == "Toyoty"),
    (cars_df["Car"] == "VW"),
    (cars_df["Car"] == "Volvo"),
    (cars_df["Car"] == "Hyundai")]

# Creamos una variable denominada "selections" que contendra un array de numeros enteros desde el 1 hasta el 17
selections = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Normalizamos y relacionamos la informacion de cada una de las marcas de autos con un numero del array "selections" 
cars_df['brand_car_normalized'] = np.select(conditions, selections, default="not_specified")
new_cars_df = pd.DataFrame()
new_cars_df["brand"] = cars_df["Car"].drop_duplicates()
new_cars_df["brand_car_normalized"] = selections


# Ahora si, seleccionamos la variable dependiente
y = cars_df["brand_car_normalized"]

# Llevamos a cabo la regresion
reg_model=lm.LinearRegression()
reg_model.fit(X,y)

# Realizamos la prediccion
predict_marca=reg_model.predict([[1400, 1300, 90]])
car_brand=int(np.round(predict_marca, decimals = 0))
name = new_cars_df[new_cars_df["brand_car_normalized"].isin([car_brand])]



# Mostramos la prediccion por consola
print("La prediccion nos arroja que la marca del auto es:", name["brand"].values[0])

# Mostramos el valor de r de relacion para evidenciar el funcionamiento optimo del modelo
print("\n"+"r="+str(reg_model.coef_))

