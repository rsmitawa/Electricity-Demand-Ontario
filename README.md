## Project Setup and Execution Guide

### Project Overview
This project predicts electricity demand for the next 24 hours using historical data and machine learning. It involves two main Jupyter Notebook files: `main.ipynb` and `machine_learning.ipynb`.

### Environment Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rsmitawa/Electricity-Demand-Ontario.git
   cd Electricity-Demand-Ontario
   ```
   
If you encounter issues with XGBoost installation due to Apple M3 chip, install XGBoost manually  
2. **Install XGBoost (if needed):**
   ```bash
   pip install xgboost
   ```

### Running the Project  
   ```bash
   jupyter lab
   ```
1. **Run `main.ipynb`:**
   - Open `main.ipynb` in Jupyter Notebook
 
2. **Run `machine_learning.ipynb`:**
   - Open `machine_learning.ipynb` in Jupyter Notebook

### Data Files
- All data files are located in the `data` folder within the project directory:
  - `Sample Dataset.csv`
  - `electricity_data_pre_ml.pkl`
    
**Note:** For optimal viewing and functionality, please download this repo and open it in Jupyter Notebook. Some internal links may not work correctly on GitHub due to the specific rules of GitHub Flavored Markdown.
