import pandas as pd
import matplotlib.pyplot as plt




data = pd.read_csv("./data/raw/us-box-office_raw.csv")

data.dtypes

data['box office'] = data['box office'].replace({'\$': '', ',': ''}, regex=True).astype(float)

data.dtypes

data.tail()

data=data.sort_values(by='year', ascending=True)



data.to_csv("./data/processed/us-box-office_clean.csv",index=False)



# Load the inflation rates data
inflation_rates_data = pd.read_csv("./data/raw/inflation_rates.csv")

# Rename columns for consistency
inflation_rates_data.rename(columns={'Year': 'year'}, inplace=True)

# Merge the box office data with the inflation rates data
merged_data = pd.merge(data, inflation_rates_data, on='year', how='left')

# Define the base year for inflation adjustment
base_year = merged_data['year'].max()

# Function to adjust values for inflation
def adjust_for_inflation(row):
    inflation_rate = row['Inflation Rate (%)'] / 100
    years_since_base = base_year - row['year']
    inflation_factor = (1 + inflation_rate) ** years_since_base
    return row['box office'] / inflation_factor

# Apply inflation adjustment
merged_data['inflation_adjusted_box_office'] = merged_data.apply(adjust_for_inflation, axis=1)


presentation_df=merged_data[["year","inflation_adjusted_box_office"]]

presentation_df=presentation_df.sort_values(by='year', ascending=True)

presentation_df.columns=["year","box_office_inf_adj"]

presentation_df["box_office_inf_adj"]=presentation_df["box_office_inf_adj"]/1000000000

presentation_df.columns=["Year","Box Office ($B)"]

presentation_df.to_csv("./data/processed/us-box-office_presentation.csv")




# Creating a line chart with the inflation-adjusted data
plt.figure(figsize=(10, 6))
plt.plot(merged_data['year'], merged_data['inflation_adjusted_box_office'], marker='o', color='b')
plt.title('Inflation Adjusted Box Office Revenue Over Years (Actual CPI Rates)')
plt.xlabel('Year')
plt.ylabel('Inflation Adjusted Box Office ($)')
plt.grid(True)
plt.xticks(merged_data['year'], rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('./output/figures/line_chart.png')

# Show the plot
plt.show()


# creating a bar chart 


# Creating a bar chart with the inflation-adjusted data using the actual inflation rates
plt.figure(figsize=(12, 8))
plt.bar(merged_data['year'], merged_data['inflation_adjusted_box_office'], color='b')
plt.title('Inflation Adjusted Box Office Revenue Over Years (Actual CPI Rates)')
plt.xlabel('Year')
plt.ylabel('Inflation Adjusted Box Office ($)')
plt.grid(True)
plt.xticks(merged_data['year'], rotation=45)  # Set the x-ticks to be the years, rotated for readability
plt.tight_layout()

# Save the bar chart
plt.savefig('./output/figures/bar_chart.png')

# Show the bar chart
plt.show()

