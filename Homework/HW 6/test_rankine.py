from rankine import rankine

def main():
    rankine1 = rankine(8,8000,t_high=500, name="Rankine Cycle - Saturated at turbine Inlet")

    eff = rankine1.calc_eff()
    print(eff)

    rankine2 = rankine(8,8000, name = "Rankine Cylce - Saturated at Turbine Inlet")

    eff2 = rankine2.calc_eff()
    print(eff2)

    rankine2.print_summary()

main()