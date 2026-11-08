# Análisis de producción textil con Python y Plotly

![Resumen visual de los indicadores basado en los CSV](images/dashboard.png)

**Autor:** Roger Armando Rodríguez Barrero  
**Tipo:** Proyecto académico de portafolio, con **datos simulados** (no son datos de ninguna empresa real).  
**Periodo simulado:** 5 al 30 de octubre de 2026 · 20 días laborales, cuatro semanas.  
**Tecnologías:** Python, pandas, NumPy, Matplotlib, Plotly, Google Colab, HTML y CSS.

## Objetivo

Analizar indicadores descriptivos de producción de prendas para practicar la preparación de datos, comparación semanal, análisis de calidad y comunicación de resultados mediante un dashboard interactivo.

## Dashboard

**[Abrir archivo HTML del dashboard](dashboard/Dashboard_Produccion_Textil.html)** — descarga el archivo y ábrelo en un navegador. Contiene gráficos Plotly interactivos (consulta de valores y zoom), pero **el selector semanal de Google Colab no se exportó**; el HTML presenta el periodo completo. GitHub puede mostrar el código del HTML en vez de ejecutarlo: ábrelo localmente.

## Resultados de la simulación

| Indicador | Resultado |
|---|---:|
| Registros diarios | 20 |
| Semanas | 4 |
| Prendas programadas | 2,717 |
| Prendas producidas | 2,572 |
| Pendientes frente al plan | 145 |
| Cumplimiento (producidas / programadas) | 94.66% |
| Prendas con defectos simulados | 58 |
| Tasa de defectos (defectuosas / producidas) | 2.26% |
| Prendas conformes (producidas − defectuosas) | 2,514 |
| Productividad estimada (prendas / horas-persona) | 3.21 |

**Hallazgos descriptivos:** la semana 3 registró el menor cumplimiento (94.48%). La semana 4 presentó la tasa de defectos más alta (2.73%). En las cuatro semanas los cumplimientos estuvieron por debajo del umbral didáctico de 95%; esto no demuestra una causa ni equivale a una evaluación real de desempeño.

### Comparación semanal

| Semana | Programadas | Producidas | Cumplimiento | Defectos | Tasa de defectos | Productividad |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 664 | 628 | 94.58% | 16 | 2.55% | 3.14 |
| 2 | 670 | 634 | 94.63% | 10 | 1.58% | 3.17 |
| 3 | 688 | 650 | 94.48% | 14 | 2.15% | 3.25 |
| 4 | 695 | 660 | 94.96% | 18 | 2.73% | 3.30 |

## Metodología

1. **Generación:** 20 registros diarios simulados mediante Python y NumPy, con una semilla fija para reproducibilidad.
2. **Preparación:** revisión de estructura, fechas, valores faltantes, duplicados y coherencia de cantidades.
3. **Indicadores:** cumplimiento, tasa de defectos, prendas conformes y productividad por hora-persona.
4. **Agrupación:** reportes por semana y tipo de prenda con pandas.
5. **Comunicación:** visualizaciones y dashboard en Google Colab; exportación de una versión HTML con Plotly.

## Organización del repositorio

```text
analisis-produccion-textil/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── produccion_textil.csv
│   ├── produccion_textil_limpia.csv
│   ├── diagnostico_produccion_semanal.csv
│   └── diagnostico_por_prenda.csv
├── dashboard/
│   └── Dashboard_Produccion_Textil.html
├── images/
│   └── dashboard.png
├── scripts/
│   └── verificar_datos.py
├── docs/
│   ├── metodologia.md
│   └── texto_hoja_de_vida.md
└── notebooks/
    └── analisis_produccion_textil.ipynb
```

## Cómo revisar y reproducir

1. Descarga o clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta `python scripts/verificar_datos.py` para validar totales entre las cuatro tablas.
4. Descarga y abre `dashboard/Dashboard_Produccion_Textil.html` en Chrome, Edge o Firefox.
5. Abre [`notebooks/analisis_produccion_textil.ipynb`](notebooks/analisis_produccion_textil.ipynb) en Google Colab para revisar el flujo original. El cuaderno contiene instrucciones propias de Colab (`files.upload()`, `files.download()` y `%pip`): para ejecutarlo de principio a fin, mantén los CSV disponibles en el directorio de sesión. Cuando aparezca el selector de archivos, elige el CSV correspondiente y verifica los nombres antes de continuar.

## Estado del cuaderno

Se incorporó el cuaderno original descargado desde Google Colab, conservando sus cuatro celdas de código. Se verificó su estructura JSON y se validaron los archivos CSV mediante `scripts/verificar_datos.py`. **No se ha certificado una ejecución integral sin intervención** porque incluye pasos de subida y descarga de archivos propios de Colab, así como un dashboard interactivo.

## Limitaciones y próximos pasos

- **Todos los datos son simulados.** No deben presentarse como mediciones de una operación real ni como mejoras efectivamente logradas.
- Solo se creó un registro de un tipo de prenda principal por día; el modelo no representa todos los pedidos ni la variedad intradía.
- `prendas_conformes = producidas − defectuosas` supone que las defectuosas requieren corrección y están incluidas en las producidas.
- Las horas-persona son horas asignadas según el modelo, no tiempos reales medidos de actividades.
- El umbral del 95% se empleó como regla didáctica, no como objetivo empresarial verificado.
- Aunque el título menciona inventarios, **este primer conjunto de datos no incluye entradas, salidas ni existencias de inventario**. Una extensión futura incorporará esa información.
- Futuras mejoras: fechas y múltiples referencias por pedido, causas de defectos, tiempos por etapa, movimientos de materia prima y filtros cruzados en una aplicación de Dash/Streamlit.

## Uso responsable

Material elaborado para aprendizaje y demostración técnica. No contiene registros internos ni información confidencial de Orion Sport Line.
