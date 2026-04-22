module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/JunWen_4_18_edited/NineZones_High_Biomass_High_CO2_26/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/JunWen_4_18_edited/NineZones_High_Biomass_High_CO2_26/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
