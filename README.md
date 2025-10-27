# Time-series Forecasting With Consuemr Spending ONS Data
![Main_Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/opengraph.png)

Office For National Statistics is publicly accessed government economic data. The goal with this project is to be able to forecasting Consumer Spending across all sectors to identify where people are chosing to spend their money. This project can aid business's in deciding where they should focuse their marketing efforts and inventory allocation and adapt pricing stratgies based on sector specific spending strends.

By incorperating ETL-processed consumer spending data, inflation metrics and consumer confidence indicators, the project adjusts fro economic shifts like recessions. It employs three predictive models, with time-series and a manual lag and utilising cross validation with GrideSearch CV. The metrics used to select the model and parameters with best lag are R2 Train/Test Score and Negative MSE Cross-Validation against Negative MSE Test. The plan is to introduce more features that could influence the consumer spending outcomes for a more robust forecast.





* [Data ETL🔎](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%202%20Spending%20Insights%20Sector%20Prepaired%202025.ipynb)
  
  
* [EDA with Seaborn/Matplotlib](https://github.com/Drook93/IBM-Data-Science-Capstone-SpaceX/blob/main/SpaceX%20EDA%20with%20SQL.ipynb)
* 
* [EDA with Visulaization Lab](https://github.com/Drook93/IBM-Data-Science-Capstone-SpaceX/blob/main/EDA%20with%20Data%20Visulisation.ipynb)

  ### Process Summary: Testing Inflation Lag Impact on Consumer Spending
  See link below to view the file:
* [Hypothesis Test With Granger Causality/ Pearson Correlation]([https://github.com/Drook93/IBM-Data-Science-Capstone-SpaceX/blob/main/SpaceX%20Locations%20Analysis%20with%20Folium.ipynb)](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Inflation_lag_correlation_test_and_granger_test.ipynb)

1. **Data Preparation**:
   - Load consumer spending and CPIH data.
   - Calculate percentage changes for spending and inflation.
   - ![Data Preparation Image][path/to/data_prep.png](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Data%20Prep%20Inflation%20Lag%20Screenshot.png)

2. **Correlation Analysis**:
   - Compute correlations between spending changes and lagged inflation.
   - Pearson Corrleation lag.
   - ![Correlation Analysis Image][(path/to(https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Pearson%20Correlation%20Manual%20LAG.png)

3. **Granger Causality Tests**:
   - Test if inflation Granger-causes spending changes (up to 13 lags).
   - Significant at lags 3, 4, 6-13 (p < 0.05).
   - ![Granger Test Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Granger%20Causality%20Model.png)
   - 

4. **Lag-Specific Regression**:
   - Shift inflation mean by 3 and 4 lags.
   - Identify the direction of causation with OLS mode
   - Run OLS on spending vs. lagged inflation.
   - Coefficients: +8.75 (lag 3), (This identifies that when Inflation Accelerates over a quater that 3 quaters later Consumer Spending increases as a result).
   - ![Regression Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/OLS%20Model.png)

5. **Export Results**:
   - Save CPIH with lags to Excel.
   - ![Export Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Saved%20CPIH%20Hypothesis%20Test.png)



* [Model Selection and Predictive Analytics] - Machine Learning Lab](https://github.com/Drook93/IBM-Data-Science-Capstone-SpaceX/blob/main/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb)
* [Final Presentation (Slide)](https://github.com/Drook93/IBM-Data-Science-Capstone-SpaceX/blob/main/Data-Science-Capstone-SpaceX%20Powerpoint%20Presentation%20Project.pdf)
