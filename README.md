# Customer Segmentation

El presente proyecto busca averiguar los distintos segmentos de clientes de un negocio retail.
Advirtiéndose que el set de datos con el cuál se parte se encuentra recopilado a nivel 'Boleta' debiendo ser necesario agregarlo a nivel 'cliente' para cumplir lo cometido.

Para lo cuál se trabajo de manera modular, aplicando diversas funciones para tratar los aspectos de calidad de datos y análisis exploratorio de los mismos (EDA).
Una vez obtenida la data preprocesada, tras haber pasado por etapas de limpieza y unificación de formatos y comprendido la misma, tras la identificación de patrones, tendencias y correlaciones que pudiesen existir entre las distintas variables, se prosiguió a cambiar su granularidad. Como se mencionó con anterioridad, se partió de un dataset el cuál se encontraba a un nivel de detalle de 'Boleta' para arrivar a otro a un nivel de detalle de 'Cliente', siendo necesario generar nuevas features al último nivel de detalle mencionado y realizar un posterior EDA sobre el dataset resultante.

La última etapa del notebook aborda el proceso de segmentación en sí. Explorando tres diferentes opciones de modelos de clustering y barriendo sobre diferentes combinaciones posibles de hiperparámetros que éstos pudiesen tomar. 
Concretamente, se implementaron los siguientes modelos:
 - KMeans
 - Hierarchical Agglomerative
 - DBSCAN
 
 para finalizar con una etapa de validación de clusters que permitió identificar cuál de ellos era el que presentaba mejor performance, para así arrivar a los segmentos de clientes buscados.

  
 Diccionario de datos:
- InvoiceNo: Nro identificador de cada boleta
- InvoiceDate: Fecha de la boleta
- CustomerId: Nro identificador de cada cliente
- Quantity: Cantidad de unidades totales compradas
- price_total: Precio total de la boleta
- StockCode: Cantidad de unidades diferentes compradas


 Dependencias:
- numpy
- pandas
- matplotlib.pyplot 
- seaborn
- functions
- sklearn.preprocessing.StandardScaler
- sklearn.decomposition.PCA
- sklearn.cluster.KMeans
- sklearn.cluster.AgglomerativeClustering
- sklearn.cluster.DBSCAN
- sklearn.metrics.davies_bouldin_score
- sklearn.metrics.silhouette_score
- scipy.spatial.distance.pdist
- scipy.cluster.hierarchy.dendrogram
- scipy.cluster.hierarchy.linkage
