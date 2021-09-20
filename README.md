# Laptop-Price-Prediction
#### A python interface to predict the price of the laptop according to the specifications of the laptop ####

**Dataset used** : [Laptop Price Prediction Kaggle Dataset](https://www.kaggle.com/ionaskel/laptop-prices) <br/><br/>

**Shape of the Dataset** : (1302, 11) <br/> Rows: 1302 <br/> Columns: 12 <br/> <br/>

### Description of Dataset : 
![Description of Dataset](/assets/images/dataset.png)

### Check for Null Values : 
![Check for Null Values in the dataset](/assets/images/null_values.png)
<br>
![Check for Null Values in the dataset](/assets/images/null_values_code.png)
<br>
There is no Null Value in the Dataset <br/><br/>


### Description of different Features : 

![](/assets/images/company.png)
Count Plot for CPU <br/>

![](/assets/images/touchscreen.png)
Count Plot for Touchscreen Feature <br/><br/>

![](/assets/images/inch.png)
Count Plot for Screen Size <br/><br/><br/>

![](/assets/images/Typename.png)
Count Plot for Type Name <br/><br/>

![](/assets/images/RAM.png)
Count Plot for RAM <br/><br/>

![](/assets/images/OS.png)
Count Plot for OS <br/><br/>


### Price vs Other Features : 

![](/assets/images/CPUvsprice.png)
CPU vs Price Plot <br/><br/>

![](/assets/images/RAMvsprice.png)
RAM vs Price Plot <br/><br/>

![](/assets/images/WeightVSprice.png)
Laptop Weight(in kg) vs Price Plot <br/><br/>

![](/assets/images/touchscreenVSprice.png)
Touchscreen vs Price Plot <br/><br/>



### Correlation between Features : 

![](/assets/images/correlation.png)
Heatmap for correlation between different features <br/><br/>


### Features in the final Dataset : <br/>
#### Input Features 
- Company	
- Type Name	
- RAM(GB)	
- Weight(kg)	
- Touchscreen	
- IPS	
- PPI	
- CPU Brand	
- HDD	
- SSD	
- GPU Brand	
- OS

#### Output Feature
- Price

![](/assets/images/Final_dataset.png)
Final Dataset before encoding <br/><br/>


### One Hot Encoding : 

![](/assets/images/encoding.png)
Code for One Hot Encoding where the number of features increases to 38<br/><br/>


**Library & Frameworks used** : 
- Pandas 
- Numpy
- Pickle
- Sklearn
- PyCaret
- Streamlit <br/><br/>

**Machine Learning Models used** : 
1. Light Gradient Boosting Machine
2. CatBoost Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. Extreme Gradient Boosting
6. Ridge Regression
7. Linear Regression
8. K Neighbors Regressor	
9. Bayesian Ridge
10. Extra Trees Regressor
11. Huber Regressor
12. AdaBoost Regressor
13. Orthogonal Matching Pursuit
14. Decision Tree Regressor
15. Least Angle Regression
16. Passive Aggressive Regressor
17. Lasso Regression
18. Elastic Net	
19. Lasso Least Angle Regression
<br/><br/>








