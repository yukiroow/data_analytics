import re
import pandas as pd

shows = pd.read_csv("prelimact3/shows.csv");

# Drop irrelevant columns
shows = shows.drop(columns=['Peak', 'All Time Peak', 'Ref.'])

# Re-arrange columns to better display data
shows = shows[['Rank', 'Tour title', 'Artist', 'Year(s)', 'Shows', 'Actual gross', 'Actual gross (in 2022 dollars)', 'Average gross']]

# Function to remove the dollar signs ($), commas (,), and unwanted characters ([e], [b], etc.)
# Also type casts the cleaned value to an integer
def clean_monetary_value(num): 
    return int(re.sub(r'[\$,]|(\[.*?\])', '', num))

# Clean numeric fields and convert to Integers
shows['Actual gross'] = shows['Actual gross'].apply(clean_monetary_value)
shows['Actual gross (in 2022 dollars)'] = shows['Actual gross (in 2022 dollars)'].apply(clean_monetary_value)
shows['Average gross'] = shows['Average gross'].apply(clean_monetary_value)

print(shows.info())