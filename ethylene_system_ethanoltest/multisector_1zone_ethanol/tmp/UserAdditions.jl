module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/ethylene_system_ethanoltest/multisector_1zone_ethanol/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/ethylene_system_ethanoltest/multisector_1zone_ethanol/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
