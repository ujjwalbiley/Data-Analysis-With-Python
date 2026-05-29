import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():

    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # First line of best fit
    res = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years_extended = np.arange(1880, 2051)

    predicted = res.slope * years_extended + res.intercept

    ax.plot(years_extended, predicted, 'r')

    # Second line of best fit (2000 onwards)
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = np.arange(2000, 2051)

    predicted_recent = (
        res_recent.slope * years_recent
        + res_recent.intercept
    )

    ax.plot(years_recent, predicted_recent, 'green')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save figure
    fig.savefig('sea_level_plot.png')

    return fig