module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/dolphyn_system/power_OneZone_MIDAT/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/dolphyn_system/power_OneZone_MIDAT/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
