import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read CSV file
    df = pd.read_csv(
        "adult.data.csv",
        header=None,
        skipinitialspace=True,
        names=[
            'age', 'workclass', 'fnlwgt', 'education',
            'education-num', 'marital-status', 'occupation',
            'relationship', 'race', 'sex', 'capital-gain',
            'capital-loss', 'hours-per-week',
            'native-country', 'salary'
        ]
    )

    # Clean salary column
    df['salary'] = (
        df['salary']
        .astype(str)
        .str.replace("'", "")
        .str.strip()
        .str.upper()
    )

    # -------------------------------
    # Race count
    # -------------------------------
    race_count = df['race'].value_counts()

    # -------------------------------
    # Average age of men
    # -------------------------------
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(),
        1
    )

    # -------------------------------
    # Percentage with Bachelors
    # -------------------------------
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100,
        1
    )

    # -------------------------------
    # Higher education
    # -------------------------------
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    lower_education = ~higher_education

    # -------------------------------
    # Rich people
    # -------------------------------
    rich = df['salary'] == '>50K'

    # Higher education rich %
    higher_education_rich = round(
        (
            (higher_education & rich).sum()
            / higher_education.sum()
        ) * 100,
        1
    )

    # Lower education rich %
    lower_education_rich = round(
        (
            (lower_education & rich).sum()
            / lower_education.sum()
        ) * 100,
        1
    )

    # -------------------------------
    # Minimum work hours
    # -------------------------------
    min_work_hours = df['hours-per-week'].min()

    # Workers with minimum hours
    num_min_workers = df[
        df['hours-per-week'] == min_work_hours
    ]

    # Rich percentage
    rich_percentage = round(
        (
            num_min_workers['salary'] == '>50K'
        ).mean() * 100,
        1
    )

    # -------------------------------
    # Country with highest rich %
    # -------------------------------
    country_rich = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts()
        /
        df['native-country'].value_counts()
        * 100
    )

    highest_earning_country = country_rich.idxmax()

    highest_earning_country_percentage = round(
        country_rich.max(),
        1
    )

    # -------------------------------
    # Top occupation in India
    # -------------------------------
    top_IN_occupation = (
        df[
            (df['native-country'] == 'India') &
            (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    # -------------------------------
    # PRINT RESULTS
    # -------------------------------
    if print_data:

        print("Race Count:")
        print(race_count)

        print("\nAverage age of men:",
              average_age_men)

        print("\nPercentage with Bachelors:",
              percentage_bachelors)

        print("\nHigher education rich:",
              higher_education_rich)

        print("\nLower education rich:",
              lower_education_rich)

        print("\nMin work hours:",
              min_work_hours)

        print("\nRich percentage:",
              rich_percentage)

        print("\nHighest earning country:",
              highest_earning_country)

        print("\nHighest earning country percentage:",
              highest_earning_country_percentage)

        print("\nTop occupation in India:",
              top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }