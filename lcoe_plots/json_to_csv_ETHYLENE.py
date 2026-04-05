import json
import csv
import io

def json_to_csv_transforms(json_data, output_path=None):
    """
    Parse ThermalSteamCracker JSON and extract transform + cost fields per instance.
    
    Args:
        json_data: dict (already parsed JSON) or str (path to JSON file)
        output_path: optional path to write CSV. If None, prints to stdout.
    """
    
    FIELDS = [
        "id",
        "h2_consumption", "h2_production", "elec_consumption",
        "ethylene_production", "natgas_consumption", "natgas_production",
        "capture_rate", "emission_rate",
        "investment_cost", "fixed_om_cost", "variable_om_cost"
    ]

    # Accept either a file path or already-parsed dict
    if isinstance(json_data, str):
        with open(json_data) as f:
            json_data = json.load(f)

    rows = []

    # Iterate over top-level asset types (e.g. "ThermalSteamCracker")
    for asset_type, asset_list in json_data.items():
        for asset in asset_list:
            instances = asset.get("instance_data", [])
            for instance in instances:
                row = {"id": instance.get("id")}

                # Pull from transforms
                transforms = instance.get("transforms", {})
                for field in FIELDS[1:9]:  # h2_consumption through emission_rate
                    row[field] = transforms.get(field)

                # Pull from edges > ethane_consumption_edge
                ethane_edge = instance.get("edges", {}).get("ethane_consumption_edge", {})
                row["investment_cost"] = ethane_edge.get("investment_cost")
                row["fixed_om_cost"] = ethane_edge.get("fixed_om_cost")
                row["variable_om_cost"] = ethane_edge.get("variable_om_cost")

                rows.append(row)

    # Write CSV
    if output_path:
        with open(output_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Written to {output_path}")
    else:
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
        print(output.getvalue())

    return rows

# Load the JSON file
with open("/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/assets/thermalsteamcracker_retrofit_option.json") as f:
    data = json.load(f)

# Write to a CSV file
rows = json_to_csv_transforms(data, output_path="/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/assets/thermalsteamcracker_retrofit_option.csv")

# Load the JSON file
with open("/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/assets/thermalsteamcracker.json") as f:
    data = json.load(f)

# Write to a CSV file
rows = json_to_csv_transforms(data, output_path="/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/assets/thermalsteamcracker.csv")