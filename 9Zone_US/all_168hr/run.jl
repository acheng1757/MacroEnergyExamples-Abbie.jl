using MacroEnergy
using Gurobi
using JSON3

MacroEnergy.retrofitted_capacity(::MacroEnergy.Storage) = 0.0

(system, model) = run_case(
    @__DIR__;
    optimizer=Gurobi.Optimizer,
    optimizer_attributes=("Method" => 2, "Crossover" => 0, "BarConvTol" => 1e-3),
);

file_path = "/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/all_168hr/assets/thermalsteamcracker.json"

# 1. Read the raw JSON
# We use JSON3.read(..., Any) first to get the raw structure
raw_json = JSON3.read(read(file_path, String))

# 2. Access your tech-specific list (ThermalSteamCracker)
# JSON3 objects can be accessed with strings
raw_list = raw_json["ThermalSteamCracker"]

# 3. CONVERSION STEP: This is where we fix the String vs Symbol issue
# We loop through each item and ensure keys are Symbols
formatted_data = [Dict{Symbol, Any}(Symbol(k) => v for (k, v) in item) for item in raw_list]

# 4. Call the function
csv_rows = MacroEnergy.json_to_csv(formatted_data)