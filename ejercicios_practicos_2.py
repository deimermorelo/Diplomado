# Solucion al Taller sobre Regresiones 2
# Diplomado Python Aplicado a la Ingenieria UPB
# Autor: Deimer David Morelo Ospino
# ID: 502217
# Email: deimer.morelo@upb.edu.co

# Importamos las librerias que utilizaremos
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from scipy import stats
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------
# Parte 1 - Regresion Lineal

# Leemos el archivo .xlsx con pandas y creamos el dataframe
dataframe = pd.read_excel('AirQualityUCI.xlsx')

# Definimos los valores de la variable independiente
x = dataframe["RH"]

#Definimos los valores de la variable ependiente
y = dataframe["T"]

#Variables estadisticas retornadas del metodo linregress
slope,intercept,r,p,std_err = stats.linregress(x,y)

# Definimos la funcion para crear el mod_reg de regresion
def reg(x):
    return slope*x + intercept

# Modelo de regresion
mod_reg = list(map(reg, x))

# Diagrama de dispersion de los datos
plt.scatter(x,y)

# Labels de plot y titulo
plt.plot(x,mod_reg)
plt.xlabel("RH")
plt.ylabel("T")
plt.title("Diagrama de dispersion RH vs T (Regresion Lineal)")
plt.show()

# Mostramos la prediccion y el r de relacion por consola
predict_reg = reg(12)
print("""La prediccion arrojada por la regresion lineal es {} y el r de relacion es {}""".format(str(predict_reg), str(r)))
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Parte 2 - Regresion Polinomial

#Modelo polinomial
pol_mod = np.poly1d(np.polyfit(x,y, 3))

#Definimos el espaciamiento para la linea
pol_line = np.linspace(1,22,100)

#Nuevos valores de y
pol_new_y = pol_mod(pol_line)

#Diagrama de dispersion
plt.scatter(x,y)

# Labels de plot y titulo
plt.plot(pol_line, pol_new_y)
plt.xlabel("RH")
plt.ylabel("T")
plt.title("Diagrama de dispersion RH vs T (Regresion Polinomial)")
plt.show()

# Mostramos la prediccion y el r de relacion por consola
predict_reg_pol = pol_mod(7)
r2_poli = r2_score(y,pol_mod(x))
print("\n"+"""La prediccion arrojada por la regresion polinomial es {} y el r de relacion es {}""".format(str(predict_reg_pol), str(r2_poli)))
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Parte 3 - Regresion Multiple

#Valores de la variable independiente
var = dataframe[["NO2(GT)"]]

#Realizamos la regresion
reg_mod_mul = linear_model.LinearRegression()
reg_mod_mul.fit(var,y)

#Realizamos la prediccion
pred_mult = reg_mod_mul.predict([[9]])
r_mult = reg_mod_mul.coef_

# Mostramos la prediccion y el r de relacion por consola
print("\n"+"""La prediccion arrojada por la regresion multiple es {} y el r de relacion es {}""".format(str(pred_mult), str(r_mult)))
#---------------------------------------------------------------------------------
