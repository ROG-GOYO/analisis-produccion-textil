from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1] / "data"
original = pd.read_csv(base / "produccion_textil.csv")
limpio = pd.read_csv(base / "produccion_textil_limpia.csv")
semanal = pd.read_csv(base / "diagnostico_produccion_semanal.csv")
prendas = pd.read_csv(base / "diagnostico_por_prenda.csv")

assert len(original) == len(limpio) == 20
assert original["fecha"].equals(limpio["fecha"])
assert not original.isna().any().any()
for origen, destino in [
    ("cantidad_programada", "programadas"),
    ("cantidad_producida", "producidas"),
    ("prendas_defectuosas", "defectuosas"),
]:
    assert original[origen].sum() == semanal[destino].sum()

assert original["cantidad_producida"].sum() == prendas["producidas"].sum()
assert original["prendas_defectuosas"].sum() == prendas["defectuosas"].sum()
assert (limpio["prendas_conformes"] == limpio["cantidad_producida"] - limpio["prendas_defectuosas"]).all()

programadas = original["cantidad_programada"].sum()
producidas = original["cantidad_producida"].sum()
defectuosas = original["prendas_defectuosas"].sum()
horas = (original["operarias"] * original["tiempo_horas"]).sum()

print("Validaciones correctas: CSV originales, procesados y diagnósticos conciliados")
print(f"Programadas: {programadas:,}; Producidas: {producidas:,}; Defectuosas: {defectuosas:,}")
print(f"Cumplimiento: {100*producidas/programadas:.2f}%")
print(f"Defectos: {100*defectuosas/producidas:.2f}%")
print(f"Productividad: {producidas/horas:.2f} prendas/hora-persona")
