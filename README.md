
# Time-series Forecasting With Consumer Spending ONS Data
![Main_Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/opengraph.png)

Office For National Statistics is publicly accessed government economic data. The goal with this project is to be able to forecasting Consumer Spending across all sectors to identify where people are chosing to spend their money. This project can aid business's in deciding where they should focuse their marketing efforts and inventory allocation and adapt pricing stratgies based on sector specific spending strends.

By incorperating ETL-processed consumer spending data, inflation metrics and consumer confidence indicators, the project adjusts fro economic shifts like recessions. It employs three predictive models, with time-series and a manual lag and utilising cross validation with GrideSearch CV. The metrics used to select the model and parameters with best lag are R2 Train/Test Score and Negative MSE Cross-Validation against Negative MSE Test. The plan is to introduce more features that could influence the consumer spending outcomes for a more robust forecast.



#### ↓↓↓Links to Folders↓↓↓
*[Data ETL🔎](Drook93/ONS-Govenment-Public-Spending-Forecast/ETL)
*[EDA with Seaborn/Matplotlib](Drook93/ONS-Govenment-Public-Spending-Forecast/EDA)
*[Hypothesis Tests](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/tree/main/Hypothesis%20Test)
*[Predictive Models](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/tree/main/Predictive%20Models)
*[Final Presentation & Findings]()

## Demo Dashboard (in-progress)🖥️

![Dashboard Demo(In-progress)](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Dashboard.gif)


  ## Testing Inflation Lag Impact on Consumer Spending🧪

From these test's, we are looking to see if Inflation as any causel affect on Consumer Spending. We start by identifying if there is any correlation between them with setting manual lags. I'm looking for negative values to see any inverse relationship but there are weak coefficience relationships across all the lags.  

 *See link below to view the file ↓*
* [Hypothesis Test With Granger Causality/ Pearson Correlation](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/tree/main/Hypothesis%20Test)

1. **Data Preparation**:
   - Load consumer spending and CPIH data.
   - Calculate percentage changes for spending and inflation.
   - ![Data Preparation Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Loading%20CPIH%20and%20Consumer%20Spending.png)

2. **Correlation Analysis**:
   - Compute correlations between spending changes and lagged inflation.
   - Manual lag loop for correlation
Pearson's Correlation Coefficient is used as a first test to see if there is any strong correlation between the features. In this case, it is weak in Coefficience
   - ![Correlation Analysis Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Pearson%20Correlation%20Manual%20LAG.png)

3. **Granger Causality Tests**:
   - Test if inflation Granger-causes spending changes (up to 13 lags).
   - Significant at lags 3, 4, 6-13 (p < 0.05).

We then test across different Inflation metrics against Consumer Spending using Granger Causality, for further evidence to determine if there is any statistical significance between them. The best lag across each of the metrics is measured to see if the p-values dip below 0.05 but with the highest degrees-of-freedom from rolling cross-validation windows.
   - ![Granger Test Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Granger%20Causality%20Model.png)
     
4. **Lag-Specific Regression**:
   - Shift inflation mean by 3 and 4 lags.
   - Identify the direction of causation with OLS mode
   - Run OLS on spending vs. lagged inflation.
   - Coefficients: +8.75 (lag 3)
Using the top performing lag from Granger, we test the direction; does that metric boost or drag spending. Magnitudes are revelaed in the coeffient size. Bigger postitives mean they surge together and bigger negatives mean higher prices reduces peoples spending capacity.
   - ![Regression Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/OLS%20Model.png)
  
5. **VAR multi-variable autoregression (IRF)**:
   - Use loop for lags for AIC to identify best lag across features.
   - Use granger test on VAR residuals
   -  Use IRF (Impulse Response Function) from VAR to see shock and responses.
Using the top performing lag from Granger, we test the direction; does that metric boost or drag spending. Magnitudes are revelaed in the coeffient size. Bigger postitives mean they surge together and bigger negatives mean higher prices reduces peoples spending capacity.

   - ![Var Model](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/VAR%20Results.png)
   - ![IRF (Impulse Response Functions](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Shock%20response.png) 

6. **Export Results**:
   - Save CPIH with lags to Excel.
   - ![Export Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Saved%20CPIH%20Hypothesis%20Test.png)

## Process Summary: Forecasting Consumer Spending with Lagged Inflation🔮

This notebook builds forecasting models for consumer spending using lagged inflation data, employing Lasso, Ridge, and RandomForest with GridSearchCV.
* [Model Selection and Predictive Analytics] - Machine Learning Lab](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Model%20Results.png)
* 
1. **Library Installation and Imports**:
   - Install statsmodels.
   - Import pandas, numpy, sklearn for modeling and evaluation.
   - ![Library Installation Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Importing%20Relevant%20Packages.png)

2. **Data Preparation**:
   - Load CPIH and consumer spending data.
   - Create lagged features (e.g., Inflation_Acceleration_lag3).
   - For this we must keep NaN's before dropping any rows with the merged df with consumer spending.
   - The Inflation metrics in earlier code would have been shifted as per the results of the best lag.
   - We MUST keep the row order for the inflation lag features in tack against the consumer spending. By executing this **"Merged_df_copy_split_rows_test = Merged_df.copy()
Merged_df_copy_split_rows_test.dropna(inplace=True)
Merged_df_copy_split_rows_test.reset_index(drop=True, inplace=True)"**
   - We allow for the first rows and beyond to be aligned with the lag in Axis 0 for the model to be trained and tested correctly.
   - ![Data Preparation Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Loading%20CPIH%20and%20Consumer%20Spending.png)

3. **Model Definition and Hyperparameter Tuning**:
   - Define Lasso, Ridge, RandomForest models with parameters.
   - TimeSeriesSplit and train test split.
     **ENSURE** the order of the code block remains the same to prevent data leakage for training and testing the model, this will give incorrect readings for the metrics otherwise. Also you **MUST** apply:         **"shuffle=False"** for the train-test split to preserve temporal order.
   - ![Model Definition Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Lag%20Options%20And%20Models.png)
   - ![Timeseries Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Time%20Series%20And%20TrainTest%20Split.png)

4. **Training and Prediction**:
   - Apply lagging and scaling.
   - Fit models, predict on test data.
   - Creating GrideSearch CV with cross-validation folders across the models
   - The first main loop is identifying the most frequent best lag across sectors with GrideSearch CV with the coresponding models and their parameters. 
   - ![Lag Loop 1 Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Manual%20Lag%20Most%20Frequent.png)
   - Ensure the best lag is applied to X-test and t-train with preocess StandardScaler for better computation accuracy.
   - The Model is then trained for each sector with the chosen lag amd applied to GrideSearch CV with ".fit.
   - ![Lag Loop 2 Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Applying%20Best%20Lag%20To%20Model.png)
    

5. **Evaluation and Results**:
   - Compute R2, MSE, RMSE.
   - Print best model, parameters, CV score.
   - Export results.
   - ![Evaluation Image](https://github.com/Drook93/ONS-Govenment-Public-Spending-Forecast/blob/main/Project%20Images/Model%20Metrics.png)



  
* [Final Presentation (Slide)]

