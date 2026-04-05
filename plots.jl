using CSV
using DataFrames
using JuMP
using MacroEnergy

import MacroEnergy: write_balance_duals;
system = systems[1]

write_balance_duals("results/", system)

# === WRITE TO SPECIFIC FOLDER ===
#folder_path = "MacroEnergyExamples.jl/examples/retrofit_tests/ethanol_retrofit_drymillccsproxy_only_z1/results_002/results"  # <-- change to your desired path

    # assets with transmission or hydrogen pipelines
#file_name = "asset_types_nolink.csv"
#file_path = joinpath(folder_path, file_name)
#CSV.write(file_path, asset_types_nolink_df)
#println("CSV written to: ", file_path)