import pandas as pd
import numpy as np

file_path = r"C:\Users\Arwa Mohamed\Desktop\Final_of_Final_HR-1.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# years of experience

for sheet_name, df in sheets.items():
    if 'Job Level' in df.columns:

        if 'Years at Company' in df.columns:
            df.rename(columns={"Years at Company": "Years of Experience"}, inplace=True)

        def assign_experience(level):
            if level == 'entry':
                return np.random.randint(1, 6)
            elif level == 'mid':
                return np.random.randint(6, 11)
            else:
                return np.random.randint(11, 21)

        df['Years of Experience'] = df['Job Level'].apply(assign_experience)



# hire date

        def generate_hire_date(row):
            level = row['Job Level']
            experience = row['Years of Experience']

            if level == 'entry':
                year_range = (2020, 2025)
            elif level == 'mid':
                year_range = (2017, 2022)
            else:  
                year_range = (2015, 2020)

            max_hire_year = 2025 - experience
            
            hire_year = np.clip(max_hire_year, year_range[0], year_range[1])
            month = np.random.randint(1, 13)
            day = np.random.randint(1, 29)
            return pd.Timestamp(year=hire_year, month=month, day=day)

        df['Hire Date'] = df.apply(generate_hire_date, axis=1)
        df['Hire Date'] = df['Hire Date'].dt.strftime('%m-%d-%Y')

    sheets[sheet_name] = df

output_path = r"C:\Users\Arwa Mohamed\Desktop\Final_of_Final_HR-2.xlsx"
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet_name, df in sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        
        
        
        
        
        
        
        
        