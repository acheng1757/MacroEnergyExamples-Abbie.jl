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

MacroEnergy.write_balance_duals("results/", system, 1.0)

