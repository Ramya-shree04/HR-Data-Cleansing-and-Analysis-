# Importing required libraries
import pandas as pd

#Load the dataset
file_path = r"C:\Users\Ravi\OneDrive\Desktop\afame\HRanalytics\data\HR Data.csv"  # Replace with the actual file path
hr_data = pd.read_csv(file_path)
print(hr_data.head())

# Removing unnecessary columns
columns_to_remove = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
hr_data_cleaned = hr_data.drop(columns=columns_to_remove)
print(f"Remaining columns: {hr_data_cleaned.columns.tolist()}")


# Rename columns
columns_rename = {
    'Attrition': 'Employee_Attrition',
    'BusinessTravel': 'Travel_Frequency',
    'DistanceFromHome': 'Distance_Home',
    'EducationField': 'Field_of_Education',
    'JobRole': 'Job_Role',
    'MonthlyIncome': 'Monthly_Income',
    'YearsAtCompany': 'Years_at_Company',
    'YearsInCurrentRole': 'Years_in_Current_Role',
    'YearsSinceLastPromotion': 'Years_Since_Last_Promotion',
    'YearsWithCurrManager': 'Years_with_Current_Manager'
}
hr_data_cleaned.rename(columns=columns_rename, inplace=True)
print(f"Renamed columns: {hr_data_cleaned.columns.tolist()}")


# Removing duplicate rows
hr_data_cleaned.drop_duplicates(inplace=True)
print(f"Number of rows after removing duplicates: {len(hr_data_cleaned)}")


# Verifing categorical columns
categorical_columns = ['Employee_Attrition', 'Travel_Frequency', 'Department', 
                       'Field_of_Education', 'Gender', 'Job_Role', 
                       'MaritalStatus', 'OverTime']

for col in categorical_columns:
    print(f"Unique values in {col}: {hr_data_cleaned[col].unique()}")


# handling missing values
missing_values = hr_data_cleaned.isnull().sum()
print(f"Missing values:\n{missing_values}")


# cleaned dataset
output_path = r"C:\Users\Ravi\OneDrive\Desktop\afame\HRanalytics\HR_Data_Cleaned.csv"  # Replace with your desired output path
hr_data_cleaned.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to {output_path}")

