from analysis import prepare_dataframe, get_safest_cells, get_riskiest_cells

def print_results(df):
    cols_to_show = [
        "row",
        "col",
        "biome",
        "depth_m",
        "pressure_atm",
        "risk_score",
        "type",
        "severity",
        "stability",
        "speed_mps",
    ]
    print(
        df[cols_to_show].to_string(
            index=False,
            float_format=lambda x: f"{x:0.3f}"
        )
    )


def main():
    print("Loading Abyssal World data and computing RISK scores...\n")
    df = prepare_dataframe()

    while True:
        print("\n=== Abyssal Risk Analyzer ===")
        print("1) Show safest cells (lowest risk)")
        print("2) Show riskiest cells (highest risk)")
        print("3) Exit")
        choice = input("Choose an option [1-3]: ").strip()

        if choice == "1":
            results = get_safest_cells(df)
            print("\nTop SAFE cells (good for exploration):\n")
            print_results(results)

        elif choice == "2":
            results = get_riskiest_cells(df)
            print("\nTop HIGH-RISK cells (danger zones):\n")
            print_results(results)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
