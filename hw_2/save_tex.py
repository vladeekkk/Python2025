from generate_tex import convert_to_tex
import os

table = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"]
]

table_tex = convert_to_tex(table)

os.makedirs("artifacts", exist_ok=True)

with open("artifacts/output.tex", "w", encoding="utf-8") as file:
    file.write(table_tex)
