import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def data_quality_analysis(df):
    # Se crea un nuevo dataframe para almacenar los resultados
    result_df = pd.DataFrame(columns=['Columna', 'Tipo de dato', 'Valores únicos', 'Valores faltantes'])

    # Se obtiene información general del dataframe
    columns = df.columns
    data_types = df.dtypes.to_list()
    unique_values = [df[column].nunique() for column in columns]
    missing_values = [df[column].isnull().mean() for column in columns]

    # Se llena el nuevo dataframe con los resultados
    result_df['Columna'] = columns
    result_df['Tipo de dato'] = data_types
    result_df['Valores únicos'] = unique_values
    result_df['Valores faltantes'] = missing_values

    return result_df.set_index('Columna')




def plot_distributions(data, analysis_result, columns_review=None):
    plt.rcParams.update({'font.size': 8})

    if columns_review:
        columns_distributions = columns_review
    else:
        columns_distributions = data.columns
    plt.figure(figsize=(10, 8))
    number_rows = len(columns_distributions)//2 + len(columns_distributions)%2
    for n, i in enumerate(columns_distributions):
        plt.subplot(number_rows, 2, n + 1)
        if analysis_result.loc[i, 'Tipo de dato']=='object':
            col = data[i].astype(str)
            sns.countplot(y= col, order=col.value_counts().iloc[:7].index)
            plt.title('Frecuencias para {}'.format(i))
        else:
            sns.distplot(data[i])
            plt.title('Distribución para {}'.format(i))
        plt.tight_layout()




def plot_box_and_whiskers(data, columns):
    for i in columns:
        plt.rcParams.update({'font.size': 8})
        sns.boxplot(data[i])
        quant_95 = data[i].quantile([0.95]).values[0]
        plt.axhline(quant_95, label=f'Percentil 95% ({quant_95})')
        plt.title(i)
        plt.legend()
        plt.xlabel('')
        plt.show()