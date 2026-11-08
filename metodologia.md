# Metodología y definiciones

## Fuente
Datos **ficticios** generados con NumPy en 20 días hábiles simulados, del 5 al 30 de octubre de 2026. No proceden de una empresa real.

## Variables
- `cantidad_programada`: unidades planificadas por registro diario.
- `cantidad_producida`: unidades fabricadas según simulación.
- `prendas_defectuosas`: unidades de la producción que requieren corrección.
- `operarias`: cinco personas asignadas por registro.
- `tiempo_horas`: ocho horas por registro diario.
- `tipo_prenda`: una categoría seleccionada aleatoriamente por registro.

## Fórmulas
- Cumplimiento = 100 × Σproducidas / Σprogramadas.
- Tasa de defectos = 100 × Σdefectuosas / Σproducidas.
- Prendas conformes = Σproducidas − Σdefectuosas.
- Productividad = Σproducidas / Σ(tiempo_horas × operarias).

La tasa de cumplimiento global se calcula a partir de totales, no promediando porcentajes diarios. Para la primera semana, la variación porcentual de productividad queda sin valor porque no existe una semana anterior.

## Alcance de las recomendaciones
Los mensajes del CSV semanal provienen de reglas simples (umbral didáctico de cumplimiento de 95%). Indican qué revisar, pero no prueban causas de defectos o retrasos.

## Verificación
Ejecutar `python scripts/verificar_datos.py` para reconciliar las cuatro tablas y el resumen de indicadores.
