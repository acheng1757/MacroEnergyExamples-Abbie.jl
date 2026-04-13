using MacroEnergy
using Gurobi
using JSON3

MacroEnergy.retrofitted_capacity(::MacroEnergy.Storage) = 0.0

(systems, model) = run_case(
    @__DIR__;
    optimizer=Gurobi.Optimizer,
    optimizer_attributes=("Method" => 2, "Crossover" => 0, "BarConvTol" => 1e-3),
);

system = systems[1]

MacroEnergy.write_duals("/Users/abbie/MacroEnergy-Abbie.jl/MacroEnergyExamples/9Zone_US/allethylene_168hr/results_003/results", system, 1.0)

