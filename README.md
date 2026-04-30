# ⚽ Football Players Stats 2024-2025 — Proyecto Final Big Data

> **Especialidad Big Data e IA** · España · Curso 2024-2025  
> Dataset: [Football Players Stats 2024-2025 — Kaggle/FBref](https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025)

---

## 📋 Índice

- [Resumen / Abstract](#-resumen--abstract)
- [Introducción](#-introducción)
- [1. Explicación y detalles de los datos](#1-explicación-y-detalles-de-los-datos)
- [2. Selección e Integración de Datasets](#2-selección-e-integración-de-datasets)
- [3. Metodología CRISP-DM](#3-metodología-crisp-dm)
- [4. Herramientas y Tecnologías](#4-herramientas-y-tecnologías)
- [5. Implementación Práctica](#5-implementación-práctica)
- [6. Resultados y Visualizaciones](#6-resultados-y-visualizaciones)
- [Conclusiones](#-conclusiones)
- [Bibliografía](#-bibliografía)
- [Estructura del repositorio](#-estructura-del-repositorio)

---

## 🧾 Resumen / Abstract

Este proyecto aplica técnicas de Big Data e Inteligencia Artificial al análisis del rendimiento de **2.297 jugadores de fútbol profesional** de las 5 grandes ligas europeas durante la temporada 2024-2025. Utilizando el dataset *Football Players Stats* (FBref / Kaggle), se construye un pipeline completo que abarca desde la exploración y limpieza de datos hasta la aplicación de modelos de machine learning (regresión lineal, Random Forest, K-Means, árbol de decisión) y la visualización interactiva en Power BI.

Los principales hallazgos incluyen: La Liga presenta la mayor producción ofensiva media por jugador, el 55,7% de los jugadores supera sus expected goals (xG), y el modelo Random Forest supera a la regresión lineal en la predicción de G+A. El clustering K-Means identifica **2 perfiles diferenciados**: Delantero Goleador (n=899) y Mediocampista Creativo (n=1.398), resultado coherente con la naturaleza del dataset real de FBref.

---

## 📖 Introducción

El fútbol moderno ha experimentado una revolución analítica impulsada por métricas avanzadas como los *Expected Goals* (xG) y los pases progresivos. Este proyecto nace de la pregunta: **¿hasta qué punto las estadísticas avanzadas predicen el rendimiento real de un jugador?**

Para responderla, se integran herramientas de análisis de datos (Python, SQL), modelos de machine learning y dashboards interactivos (Power BI), siguiendo la metodología estándar CRISP-DM y aplicando los conocimientos adquiridos en las asignaturas de Sistemas en Big Data y Aplicaciones de Big Data.

---

## 1. Explicación y detalles de los datos

El dataset proviene de **FBref.com** (Sports Reference LLC), recopilado automáticamente cada semana mediante un pipeline ETL y publicado en Kaggle por Hubert Sidorowicz:

🔗 https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025

Cubre las **5 grandes ligas europeas** (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) con estadísticas individuales acumuladas de la temporada 2024-2025. No es una muestra: incluye **todos los jugadores** que han disputado al menos un partido oficial (2.854 registros brutos, 2.297 tras limpieza). El uso es legítimo bajo licencia educativa y no comercial (Kaggle Open Dataset).

**Preguntas clave del proyecto:**
- ¿Qué variables tienen mayor correlación con la producción goleadora?
- ¿Existen diferencias significativas de rendimiento entre ligas?
- ¿Se puede predecir G+A a partir de métricas avanzadas (xG, xAG)?
- ¿Qué jugadores rinden por encima de lo esperado (*outperforming xG*)?

---

## 2. Selección e Integración de Datasets

El dataset principal contiene **267 columnas** en su versión original de FBref, de las cuales se seleccionan las más relevantes para el análisis:

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `Pos` | Categórica nominal | Posición (GK, DF, MF, FW) |
| `Comp` | Categórica nominal | Liga |
| `Gls`, `Ast`, `G+A` | Numérica discreta | Producción ofensiva |
| `xG`, `xAG` | Numérica continua | Expected Goals / Assisted Goals |
| `PrgC`, `PrgP`, `PrgR` | Numérica discreta | Acciones progresivas |
| `Gls/90`, `Ast/90` | Numérica continua | Rendimiento por 90 min (calculado) |
| `market_value_eur_M` | Numérica continua | Valor de mercado estimado (M€) |

> **Nota:** La columna `market_value_eur_M` no existe en el dataset original de FBref. Se calcula en el pipeline Python mediante una fórmula basada en el rendimiento del jugador (Gls, Ast, xG), ya que un join real con Transfermarkt requeriría un segundo dataset externo.

**Análisis estadístico aplicado:**
- Estadística descriptiva (media, mediana, IQR, outliers)
- Correlación de Pearson (xG vs Gls, xAG vs Ast)
- ANOVA visual (Gls/90 por liga)
- Regresión lineal múltiple
- Clustering K-Means
- Árbol de decisión (clasificación)

---

## 3. Metodología CRISP-DM

Se aplica el modelo **CRISP-DM** por su naturaleza iterativa, adecuada para un dominio con alto ruido estadístico como el fútbol.

```
Comprensión     →  Comprensión   →  Preparación  →  Modelado
del negocio        de los datos      de datos
     ↑                                                   ↓
  Despliegue   ←  Evaluación  ←────────────────────────────
```

**Decisiones de limpieza aplicadas (Fase 3):**
- Separación de porteros (GK): análisis exclusivamente ofensivo
- Filtro mínimo de 90 minutos jugados para evitar sesgos en métricas /90
- Limpieza de posiciones compuestas (`MF,FW` → `MF`)
- Cálculo de columnas `/90` desde la columna `90s` del dataset FBref
- Imputación de nulos con mediana en variables numéricas clave

**Criterios de éxito:** Silhouette Score > 0,25 en clustering · Accuracy > 70% en clasificación.

---

## 4. Herramientas y Tecnologías

### 🐍 Python (Pandas · Matplotlib · Seaborn · Scikit-learn)

**¿Qué es?** Python es el lenguaje de referencia en Data Science. Las librerías utilizadas cubren el ciclo completo de análisis:

- **Pandas**: manipulación y limpieza de datos en DataFrames.
- **Matplotlib / Seaborn**: generación de gráficas estadísticas (boxplots, scatterplots, heatmaps).
- **Scikit-learn**: implementación de modelos de machine learning con API unificada (`fit` / `predict` / `score`).

**Uso en el proyecto:** EDA completo, limpieza de datos, regresión lineal múltiple, Random Forest, K-Means, árbol de decisión y validación cruzada k-fold (k=5).

📄 Código: [`notebooks/01_eda_and_modeling.py`](notebooks/01_eda_and_modeling.py)

---

### 🗄️ SQL (DuckDB)

**¿Qué es?** SQL es el estándar para consultar bases de datos relacionales. **DuckDB** es un motor SQL embebido y analítico que procesa directamente archivos CSV sin necesidad de servidor, con la misma sintaxis que BigQuery o PostgreSQL.

**Uso en el proyecto:** Consultas de exploración, ranking de jugadores, KPIs por liga, análisis de outliers y segmentación por valor de mercado.

📄 Código: [`sql/football_analysis.sql`](sql/football_analysis.sql)

---

### 📊 Power BI

**¿Qué es?** Herramienta de Business Intelligence de Microsoft para la creación de dashboards interactivos con filtros cruzados, KPIs y visualizaciones dinámicas.

**Uso en el proyecto:** Dashboard de 4 páginas sobre el CSV enriquecido exportado por Python.

📄 Archivo: [`powerbi/football_dashboard.pbix`](powerbi/football_dashboard.pbix)

---

## 5. Implementación Práctica

### 5.1 Flujo del pipeline

```
[Kaggle CSV — 2.854 registros, 267 columnas]
                    ↓
      01_eda_and_modeling.py
      ├── Limpieza → 2.297 jugadores de campo
      ├── EDA: 11 visualizaciones
      ├── Regresión Lineal + Random Forest
      ├── K-Means Clustering (k=2)
      ├── Árbol de Decisión
      └── football_stats_enriched.csv
                    ↓
         SQL (DuckDB) — 8 consultas analíticas
         Power BI — Dashboard 4 páginas
```

### 5.2 Resultados de los modelos

#### Regresión Lineal Múltiple (predecir G+A)

| Métrica | Valor |
|---------|-------|
| R² CV (5-fold) | 0,345 ± 0,064 |
| RMSE CV | 4,52 ± 0,19 |
| MAE | 3,56 |

Variables más influyentes: `xG` (coef. +0,28), `xAG` (coef. +0,15), `PrgC` (coef. +0,05).

#### Random Forest (comparativa)

| Métrica | Valor |
|---------|-------|
| R² CV (5-fold) | **0,452 ± 0,088** |

El Random Forest mejora la regresión lineal al capturar relaciones no lineales entre xG, minutos jugados y producción real.

#### K-Means Clustering (k=2)

| Cluster | Perfil | n jugadores | Gls medio | Ast medio |
|---------|--------|-------------|-----------|-----------|
| 0 | Delantero Goleador | 899 | 3,92 | 2,85 |
| 1 | Mediocampista Creativo | 1.398 | 0,91 | 0,60 |

> Con el dataset real de FBref el Silhouette Score convergió en **k=2** como número óptimo de clusters. Este resultado es coherente: la variable más discriminante es la producción goleadora directa, que separa claramente perfiles ofensivos de perfiles creativos/defensivos.

#### Árbol de Decisión (¿supera el jugador su xG?)

| Métrica | Valor |
|---------|-------|
| Accuracy CV (5-fold) | **74,5%** |
| F1-Score (clase positiva) | 0,80 |

La variable más discriminante es `xG ≤ 3,42`: jugadores con baja expectativa goleadora son más propensos a superarla estadísticamente.

### 5.3 Hallazgos principales

- **Mohamed Salah** lidera la producción ofensiva con 47 G+A en la temporada, muy por encima de su xG (outperformer destacado).
- El **55,7% de los jugadores de campo** supera sus expected goals, lo que indica que el xG es un predictor conservador en la práctica.
- **La Liga** presenta la mayor producción ofensiva media entre las 5 ligas analizadas.
- El **valor de mercado estimado** se correlaciona más con la producción acumulada que con el rendimiento por 90 minutos.
- El clustering identifica dos perfiles estadísticamente coherentes con el conocimiento del dominio futbolístico.

---

## 6. Resultados y Visualizaciones

> Las figuras generadas por Python se encuentran en [`docs/figures/`](docs/figures/)

| Figura | Descripción |
|--------|-------------|
| `01_distribucion_goles_posicion.png` | Boxplot G/A/G+A por posición |
| `02_goles90_por_liga.png` | Gls/90 por liga (base ANOVA) |
| `03_heatmap_correlaciones.png` | Matriz de correlación |
| `04_scatter_xg_vs_goles.png` | xG vs Goles reales por posición |
| `05_valor_mercado_vs_ga.png` | Valor estimado de mercado vs G+A |
| `06_top15_jugadores_ga.png` | Top 15 jugadores por G+A |
| `07_regresion_residuos.png` | Residuos y Real vs Predicho |
| `08_feature_importance_rf.png` | Importancia de variables (RF) |
| `09_kmeans_elbow_silhouette.png` | Elbow + Silhouette (K-Means) |
| `10_kmeans_clusters_scatter.png` | Clusters de jugadores (scatter) |
| `11_confusion_matrix_dt.png` | Matriz de confusión árbol de decisión |

**Dashboard Power BI — 4 páginas:**
- **Vista General**: KPIs por liga, media G+A, filtro por posición
- **Top Jugadores**: tabla completa ordenada por G+A con filtros interactivos
- **Análisis xG**: scatter Goles reales vs xG coloreado por posición
- **Perfiles Clustering**: segmentación K-Means con scatter y tabla de métricas medias

---

## 📌 Conclusiones

1. Las métricas avanzadas (xG, xAG) tienen poder predictivo real pero limitado: el Random Forest con R²=0,45 muestra que el rendimiento ofensivo depende también de factores no capturados estadísticamente (sistema táctico, compañeros, forma física).
2. El clustering K-Means con datos reales identificó **k=2** como número óptimo, diferenciando perfiles ofensivos de creativos/defensivos de forma estadísticamente sólida (Silhouette > 0,25).
3. El 55,7% de los jugadores supera su xG, confirmando que el modelo de expected goals tiende a ser conservador en la práctica real.
4. Para futuros trabajos se recomienda incorporar datos de partidos individuales (no solo acumulados de temporada) y métricas defensivas para construir un índice de rendimiento global más completo.

---

## 📚 Bibliografía

- FBref.com — Sports Reference LLC. *Football Statistics and History*. https://fbref.com
- Sidorowicz, H. (2024). *Football Players Stats 2024-2025*. Kaggle. https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2024-2025
- Chapman, P. et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Pedregosa, F. et al. (2011). *Scikit-learn: Machine Learning in Python*. JMLR 12, 2825-2830.
- McKinney, W. (2010). *Data Structures for Statistical Computing in Python*. Proceedings of the 9th Python in Science Conference.
- Microsoft. (2024). *Power BI Documentation*. https://docs.microsoft.com/power-bi
- DuckDB Team. (2024). *DuckDB Documentation*. https://duckdb.org/docs
- Anthropic Claude AI — apoyo en redacción, estructuración y desarrollo del proyecto.

---

## 📁 Estructura del repositorio

```
football-bigdata-project/
│
├── README.md                          # Este archivo
│
├── data/
│   ├── generate_sample_data.py        # Generador de datos de muestra
│   ├── football_stats_2024_25.csv     # Dataset principal (Kaggle/FBref)
│   ├── football_stats_enriched.csv    # Dataset enriquecido con predicciones y clusters
│   └── summary_by_league.csv         # KPIs agregados por liga
│
├── notebooks/
│   └── 01_eda_and_modeling.py         # Pipeline completo: EDA + 4 modelos ML
│
├── sql/
│   └── football_analysis.sql          # 8 consultas SQL analíticas (DuckDB)
│
├── powerbi/
│   └── football_dashboard.pbix        # Dashboard interactivo — 4 páginas
│
└── docs/
    └── figures/                       # 11 gráficas PNG generadas por Python
        ├── 01_distribucion_goles_posicion.png
        ├── 02_goles90_por_liga.png
        ├── 03_heatmap_correlaciones.png
        ├── 04_scatter_xg_vs_goles.png
        ├── 05_valor_mercado_vs_ga.png
        ├── 06_top15_jugadores_ga.png
        ├── 07_regresion_residuos.png
        ├── 08_feature_importance_rf.png
        ├── 09_kmeans_elbow_silhouette.png
        ├── 10_kmeans_clusters_scatter.png
        └── 11_confusion_matrix_dt.png
```

---

*Proyecto académico — Especialidad Big Data e IA · España · 2024-2025*