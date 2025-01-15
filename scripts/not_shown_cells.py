import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def plot_regression_error(exploratory_data:pd.DataFrame):
    # Muestra de los datos para el gráfico
    data = exploratory_data.sample(25, random_state=7)
    x = data["father"]
    y = data["childHeight"]
    y_pred_father = data["childHeight_father"]

    # Configuración de los subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), sharey=True)
    fig.suptitle("Regresión lineal simple vs. regresión lineal múltiple", fontsize=16)
    # Primer grafico
    axes[0].scatter(x, y, color="blue", label="Datos originales")

    # Línea de regresión basada solo en el padre
    axes[0].plot(x, y_pred_father, color="red", label="Regresión (padre)")

    # Añadir líneas que representen las distancias para el primer modelo
    for xi, yi, ypi in zip(x, y, y_pred_father):
        axes[0].plot([xi, xi], [yi, ypi], color="green", linestyle="--")

    axes[0].set_title("Regresión basada en el padre")
    axes[0].set_xlabel("Altura del padre")
    axes[0].set_ylabel("Altura del hijo")
    axes[0].legend()
    axes[0].grid()

    x_male = data[data["gender"] == "male"]["father"]
    x_female = data[data["gender"] == "female"]["father"]
    y_male = data[data.index.isin(x_male.index)]["childHeight"]
    y_female = data[data.index.isin(x_female.index)]["childHeight"]

    male_pred = data[data.index.isin(x_male.index)]["childHeight_father_gender"]
    female_pred = data[data.index.isin(x_female.index)]["childHeight_father_gender"]

    # Segundo gráfico 
    axes[1].scatter(x, y, color="blue", label="Datos originales")

    # Línea de regresión basada en el padre y el género
    axes[1].plot(x_male, male_pred, color="#57b3de", label="Regresión (padre + male)")
    axes[1].plot(x_female, female_pred, color="#de57b9", label="Regresión (padre + female)")


    # Añadir líneas que representen las distancias para el segundo modelo
    for xi, yi, ypi in zip(x_male, y_male, male_pred):
        axes[1].plot([xi, xi], [yi, ypi], color="#57b3de", linestyle="--")

    for xi, yi, ypi in zip(x_female, y_female, female_pred):
        axes[1].plot([xi, xi], [yi, ypi], color="#de57b9", linestyle="--")

    axes[1].set_title("Regresión basada en el padre + género")
    axes[1].set_xlabel("Altura del padre")
    axes[1].set_ylabel("Altura del hijo")
    axes[1].legend()
    axes[1].grid()

    # Ajuste del espacio entre gráficos
    plt.tight_layout()
    plt.show()

def get_outlier_df(data: pd.DataFrame):
    ex_df = data[["father", "childHeight"]].sample(20, random_state=42)
    ex_1 = ex_df.copy()
    ex_1["has_outlier"] = 0
    ex_2 = ex_df.copy()
    ex_2["has_outlier"] = 1
    df = pd.concat([ex_1, ex_2], axis=0)
    return df