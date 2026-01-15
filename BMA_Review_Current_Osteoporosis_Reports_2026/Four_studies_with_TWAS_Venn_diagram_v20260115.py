import pandas as pd
import matplotlib.pyplot as plt
from venny4py.venny4py import venny4py

# --------------------------------------------------
# 1. Load difference matrix
# --------------------------------------------------
df = pd.read_csv("Four_studies_with_TWAS_difference_matrix.csv")

gene_col = df.columns[0]
study_cols = df.columns[1:5]

# Clean TRUE/FALSE safely
for c in study_cols:
    df[c] = (
        df[c]
        .astype(str)
        .str.strip()
        .str.upper()
        .map({"TRUE": True, "FALSE": False})
    )

# --------------------------------------------------
# 2. Convert to gene sets
# --------------------------------------------------
gene_sets = {
    study: set(df.loc[df[study], gene_col])
    for study in study_cols
}

# --------------------------------------------------
# 3. Draw Venn diagram (NO extra arguments)
# --------------------------------------------------
venny4py(gene_sets)

# --------------------------------------------------
# 4. Export SVG
# --------------------------------------------------
plt.tight_layout()
plt.savefig(
    "Venn_Diagram_4_sets_Fig1A_right_with_TWAS.svg",
    format="svg"
)
plt.show()
