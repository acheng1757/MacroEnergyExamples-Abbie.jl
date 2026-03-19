module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/dolphyn_system/EASTERN_US_MACRO_Ethylene_POWER+H2+CSC+NG+LF+BESC_globaldemand/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/dolphyn_system/EASTERN_US_MACRO_Ethylene_POWER+H2+CSC+NG+LF+BESC_globaldemand/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
