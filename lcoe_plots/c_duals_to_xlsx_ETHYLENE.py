import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# ── Paths ──────────────────────────────────────────────────────────────────────
DUALS_CSV     = "/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/results_017/results/balance_duals.csv"
CO2_DUALS_CSV = "/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/results_017/results/co2_cap_duals.csv"
XLSX_PATH     = "/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/lcoe_plots/LCOE_Ethylene_Macro.xlsx"

# ── Mapping: xlsx dual column header → CSV column prefix ──────────────────────
# The script will look for  <csv_prefix>_<ZONE>  in the CSV and take the average.
# e.g. xlsx header "elec_demand" + zone "CA"  →  CSV column "elec_CA"
DUAL_COLUMN_MAP = {
    "elec_demand":     "elec",
    "h2_balance":      "h2",
    "h2_demand":       "h2_demand",        # adjust if there's a separate h2_demand column
    "ng_balance":      "natgas",
    "ng_demand":       "natgas_demand",
    "ethane_supply":   "ethane",
    "ethanol_balance": "ethanol",
    "ethanol_demand":  "ethanol_demand",
    "ethylene_balance": "ethylene",
    "ethylene_demand":  "ethylene_demand",
    "gasoline_balance":"gasoline",
    "gasoline_demand": "gasoline_demand",
    "diesel_balance":  "diesel",
    "diesel_demand":   "diesel_demand",
    "jetfuel_balance": "jetfuel",
    "jetfuel_demand":  "jetfuel_demand",
    "bioherb_supply":  "bioherb",
    "biowood_supply":  "biowood",
    "bioagri_supply":  "bioagri",
}

# ── co2_sink comes from a separate CSV ────────────────────────────────────────
# co2_cap_duals.csv has columns: Node, CO2_Shadow_Price
# The co2_sink row gives a single system-wide value applied to every asset row.
co2_df = pd.read_csv(CO2_DUALS_CSV)
co2_sink_value = co2_df.loc[co2_df["Node"] == "co2_sink", "CO2_Shadow_Price"].values
CO2_SINK_VALUE = round(float(co2_sink_value[0]), 6) if len(co2_sink_value) > 0 else None

HEADER_ROW     = 3
DATA_START_ROW = 4
light_blue = PatternFill(start_color="ADD8E6", end_color="ADD8E6", fill_type="solid")

# ── Load data ──────────────────────────────────────────────────────────────────
duals_df = pd.read_csv(DUALS_CSV)
wb = load_workbook(XLSX_PATH)
ws = wb.active

# ── Build column index map from xlsx header row ────────────────────────────────
col_name_to_idx = {}
for cell in ws[HEADER_ROW]:
    if cell.value:
        col_name_to_idx[cell.value] = cell.column

# ── Helper: extract zone from asset id ────────────────────────────────────────
def extract_zone(asset_id: str) -> str:
    """
    Extract the zone suffix from an asset id.
    Examples:
        'CA_TSC'         -> 'CA'
        'CA_TSC+CC90'    -> 'CA'
        'TX_TSC:H2'      -> 'TX'
        'NCEN_TSC+H2in'  -> 'NCEN'
    Strategy: the zone is everything before the first '_'.
    """
    return asset_id.split("_")[0]

# ── Clear any existing dual values before writing ─────────────────────────────
all_dual_cols = set(DUAL_COLUMN_MAP.keys()) | {"co2_sink"}
dual_col_indices = {
    col_name_to_idx[col]
    for col in all_dual_cols
    if col in col_name_to_idx
}

row = DATA_START_ROW
while True:
    asset_id = ws.cell(row=row, column=col_name_to_idx.get("id", 2)).value
    if asset_id is None:
        break
    for col_idx in dual_col_indices:
        ws.cell(row=row, column=col_idx).value = None
    row += 1

# ── Iterate over data rows ─────────────────────────────────────────────────────
row = DATA_START_ROW
while True:
    asset_id = ws.cell(row=row, column=col_name_to_idx.get("id", 2)).value
    if asset_id is None:
        break

    zone = extract_zone(str(asset_id))

    # Zone-specific duals from balance_duals.csv
    for xlsx_col, csv_prefix in DUAL_COLUMN_MAP.items():
        if xlsx_col not in col_name_to_idx:
            continue

        csv_col = f"{csv_prefix}_{zone}"

        if csv_col not in duals_df.columns:
            continue

        avg_val = duals_df[csv_col].mean()
        col_idx = col_name_to_idx[xlsx_col]
        cell = ws.cell(row=row, column=col_idx, value=round(avg_val, 6))
        cell.fill = light_blue

    # co2_sink: same value for every row, from co2_cap_duals.csv
    if "co2_sink" in col_name_to_idx and CO2_SINK_VALUE is not None:
        col_idx = col_name_to_idx["co2_sink"]
        cell = ws.cell(row=row, column=col_idx, value=CO2_SINK_VALUE)
        cell.fill = light_blue

    row += 1

# ── Save ───────────────────────────────────────────────────────────────────────
wb.save(XLSX_PATH)
print(f"Done! Populated duals for {row - DATA_START_ROW} rows.")
print(f"  co2_sink value used: {CO2_SINK_VALUE}")