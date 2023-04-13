PROBABILISTIC_TOURNAMENT_VALUE = 0.75

def selection_method(population, target, selection_algorithm):
        match selection_algorithm: 
            case "roulette":
                roulette_selection(population, target)
            case "elite":
                elite_selection(population, target)
            case "rank":
                rank_selection(population, target)
            case "probabilistic_tournament":
                probabilistic_tournament_selection(population, target)