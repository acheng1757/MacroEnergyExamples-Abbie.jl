module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/ETHYLENESYSTEM_ethanol+ethylene/liquid_fuels_only/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/ETHYLENESYSTEM_ethanol+ethylene/liquid_fuels_only/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
