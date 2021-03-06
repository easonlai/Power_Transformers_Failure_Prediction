# Power Transformers Failure Prediction

This is a sample code repository of the power transformer's health state (index) analysis or prediction by the regression model for experiment and learning purposes. The sample dataset is also published in [Kaggle (Sample Power Transformers Health Condition Dataset).](https://www.kaggle.com/easonlai/sample-power-transformers-health-condition-dataset)


Health Index and Transformer Expected Lifetime reference table from [ResearchGate paper (An Approach to Determine the Health Index of Power Transformers)](https://www.researchgate.net/publication/4345290_An_Approach_to_Determine_the_Health_Index_of_Power_Transformers)
![alt text](https://github.com/easonlai/Power_Transformers_Failure_Prediction/blob/main/health-index-and-transformer-expected-lifetime.png)

Contents:
* power_transformer_health_state_data_analysis.ipynb <-- Sample of basic data exploration and analytic.
* data/Health index2.csv <-- Sample dataset of power transformer conditions with corresponding health state (index).
* aml_endpoint_test.py <-- Script to test prediction endpoint from [Azure Machine Learning (AML)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=azcli).


Reference:
* [12 on-site checks to inspect the transformer's health](https://electrical-engineering-portal.com/transformers-health-on-site-checks)
* [ResearchGate - Calculation of power transformers health indexes](https://www.researchgate.net/publication/228582140_Calculation_of_power_transformers_health_indexes)
* [ResearchGate - An Approach to Determine the Health Index of Power Transformers](https://www.researchgate.net/publication/4345290_An_Approach_to_Determine_the_Health_Index_of_Power_Transformers)