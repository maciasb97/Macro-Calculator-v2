# ══════════════════════════════════════════════ calculator.py ══════════════════════════════════════════════
# This file contains the main logic for calculating TDEE and macro breakdowns based on user input.

# Constants for dropdown options and their corresponding values
HEIGHT_OPTIONS = [
    "4ft 7in", "4ft 8in", "4ft 9in", "4ft 10in", "4ft 11in",
    "5ft 0in", "5ft 1in", "5ft 2in", "5ft 3in", "5ft 4in",
    "5ft 5in", "5ft 6in", "5ft 7in", "5ft 8in", "5ft 9in",
    "5ft 10in", "5ft 11in", "6ft 0in", "6ft 1in", "6ft 2in",
    "6ft 3in", "6ft 4in", "6ft 5in", "6ft 6in", "6ft 7in",
    "6ft 8in", "6ft 9in", "6ft 10in", "6ft 11in", "7ft 0in"
]

HEIGHT_TO_CM = [
    139.7, 142.24, 144.78, 147.32, 149.86, 152.4, 154.94, 157.48,
    160.02, 162.56, 165.1, 167.64, 170.18, 172.72, 175.26, 177.8,
    180.34, 182.88, 185.42, 187.96, 190.5, 193.04, 195.58, 198.12,
    200.66, 203.2, 205.74, 208.28, 210.82, 213.36
]

ACTIVITY_OPTIONS = [
    "Sedentary (office job/no exercise)",
    "Lightly active (1-2 days/week)",
    "Moderately active (3-5 days/week)",
    "Very active (6-7 days/week)",
    "ATHLETE (2x day)"
]

ACTIVITY_MULTIPLIERS = [1.2, 1.375, 1.55, 1.725, 1.9]


def calculate_tdee(age, weight_lbs, gender, height_label, activity_label, body_fat=0):
    """
    Returns TDEE (total daily energy expenditure) as a rounded integer.

    Parameters:
        age          : int
        weight_lbs   : int/float
        gender       : str  — "male" or "female"
        height_label : str  — must match one of HEIGHT_OPTIONS exactly
        activity_label: str — must match one of ACTIVITY_OPTIONS exactly
        body_fat     : int  — optional, 0 means not provided
    """
    height_cm = HEIGHT_TO_CM[HEIGHT_OPTIONS.index(height_label)]
    weight_kg = round(weight_lbs / 2.20462, 2)

    if body_fat > 0:
        # Katch-McArdle — more accurate when body fat is known
        lbm = weight_kg * (1 - (body_fat / 100))
        bmr = 370 + (21.6 * lbm)
    elif gender == "male":
        # Mifflin-St Jeor for males
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        # Mifflin-St Jeor for females
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    multiplier = ACTIVITY_MULTIPLIERS[ACTIVITY_OPTIONS.index(activity_label)]
    return round(bmr * multiplier)


def calculate_macros(tdee):
    """
    Returns a dict with macro breakdowns for maintenance, cut, and bulk.
    Each goal contains three macro splits: moderate_carb, lower_carb, higher_carb.

    Calorie targets:
        maintenance : tdee
        cut         : tdee - 500
        bulk        : tdee + 500

    Macro splits (protein/fat/carb ratios):
        moderate_carb : 30/35/35
        lower_carb    : 40/40/20
        higher_carb   : 30/20/50
    """

    def split(calories, protein_ratio, fat_ratio, carb_ratio):
        # protein & carbs = 4 cal/g, fat = 9 cal/g
        return {
            "protein": f"{round((calories * protein_ratio) / 4)}g",
            "fat":     f"{round((calories * fat_ratio) / 9)}g",
            "carbs":   f"{round((calories * carb_ratio) / 4)}g",
        }

    def all_splits(calories):
        return {
            "moderate_carb": split(calories, 0.30, 0.35, 0.35),
            "lower_carb":    split(calories, 0.40, 0.40, 0.20),
            "higher_carb":   split(calories, 0.30, 0.20, 0.50),
        }

    return {
        "maintenance": {"calories": tdee,       "splits": all_splits(tdee)},
        "cut":         {"calories": tdee - 500, "splits": all_splits(tdee - 500)},
        "bulk":        {"calories": tdee + 500, "splits": all_splits(tdee + 500)},
    }