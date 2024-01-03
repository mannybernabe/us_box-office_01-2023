
# Inflation Adjusted Box Office Revenue Analysis

![Main Presentation Image](https://github.com/mannybernabe/us_box-office_01-2023/output/figures/US Box Office Inflation Adjusted.png)

## Project Overview
This project involves analyzing box office revenues over several years and adjusting them for inflation using actual CPI rates. The goal is to understand the real value of box office revenues when accounting for the changes in purchasing power over the years.

## Data Sources
- `box_office_data.csv`: Contains the raw box office revenue data over various years.
- `inflation_rates.csv`: Contains the annual inflation rates based on the Consumer Price Index (CPI).

## Files in the Project
- `analysis_script.py`: Python script for data loading, cleaning, merging, inflation adjustment, and plotting.
- `inflation_adjusted_box_office_actual_cpi_chart.png`: Inflation-adjusted box office revenue line chart.
- `inflation_adjusted_box_office_actual_cpi_bar_chart.png`: Inflation-adjusted box office revenue bar chart.

## Setup and Running the Project
1. Ensure that Python and necessary libraries (pandas, matplotlib) are installed.
2. Place the data files (`box_office_data.csv` and `inflation_rates.csv`) in the appropriate directory.
3. Run `analysis_script.py` to perform the analysis and generate the charts.

## Analysis Overview
The analysis script performs the following steps:
1. Loads the box office revenue data and the inflation rates data.
2. Cleans and preprocesses the data as necessary.
3. Merges the datasets based on the year.
4. Adjusts the box office revenues for inflation using the CPI rates.
5. Generates a line chart and a bar chart to visualize the inflation-adjusted revenues.






## Analysis Visualizations

### Inflation Adjusted Box Office Revenue (Line Chart)
![Inflation Adjusted Box Office Revenue Over Years - Line Chart](https://github.com/mannybernabe/us_box-office_01-2023/blob/main/output/figures/line_chart.png "Line Chart")

### Inflation Adjusted Box Office Revenue (Bar Chart)
![Inflation Adjusted Box Office Revenue Over Years - Bar Chart](https://github.com/mannybernabe/us_box-office_01-2023/blob/main/output/figures/bar_chart.png "Bar Chart")


## Note
The original source data for this analysis was obtained from [Box Office Mojo](https://www.boxofficemojo.com/year/).