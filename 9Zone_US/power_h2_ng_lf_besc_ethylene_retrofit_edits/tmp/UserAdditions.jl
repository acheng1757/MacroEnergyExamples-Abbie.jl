module UserAdditions
using MacroEnergy

commodities_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/power_h2_ng_lf_besc_ethylene_retrofit_edits/tmp/usersubcommodities.jl"
if isfile(commodities_path)
    include(commodities_path)
end

assets_path = raw"/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/power_h2_ng_lf_besc_ethylene_retrofit_edits/tmp/userassets.jl"
if isfile(assets_path)
    include(assets_path)
end

end
