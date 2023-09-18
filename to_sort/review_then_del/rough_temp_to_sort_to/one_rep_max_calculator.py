def calculate_estimated_1rm(mod_rep_weight, rep_range):
    return (mod_rep_weight * rep_range * 0.0333) + mod_rep_weight

def main():
    mod_rep_weight = int(input("Please enter the weight you lifted for your moderate rep range: "))
    rep_range = int(input("Please enter the number of reps you performed for the given weight: "))
    est_one_rep_max = calculate_estimated_1rm(mod_rep_weight, rep_range)
    print("Your estimated one-rep max (1RM):", est_one_rep_max)

if __name__ == "__main__":
    main()

