import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = r"C:\Users\Arwa Mohamed\Desktop\Final_of_Final_HR.xlsx"
sheets = pd.read_excel(file, sheet_name=None)

# Merge all sheets on 'Employee ID'
df = sheets[list(sheets.keys())[0]]
for name, sheet in sheets.items():
    if name != list(sheets.keys())[0]:
        df = pd.merge(df, sheet, on='Employee ID', how='outer')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')
numeric_df = df.select_dtypes(include=['number'])

# calculate correlation matrix
corr_matrix = numeric_df.corr()
sns.set(font_scale=2.7) 


#Correlation Heatmap
plt.figure(figsize=(16, 10))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    annot_kws={"size": 16},
    linewidths=0.5,
    square=False,
    cbar_kws={"shrink": 0.77,
              "ticks":[-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0]}
)
plt.title('Correlation Heatmap of HR Numeric Features', fontsize=24)
plt.xticks(rotation=45, ha='right', fontsize=14)
plt.yticks(rotation=0, fontsize=14)
plt.tight_layout()
plt.show()


# Monthly Income by Job Level
sns.boxplot(x='Job Level', y='Monthly Income', data=df, palette='Set2')
plt.title('Monthly Income Distribution by Job Level')
plt.xlabel('Job Level')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.show()

#count of company reputation
plt.figure(figsize=(22, 12))
df['Company Reputation'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['steelblue', 'yellow', 'tomato'])
plt.title('Company Reputation Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

#Job Satisfaction by Company Size
plt.figure(figsize=(18, 12))
size_satisfaction = df.groupby('Company Size')['Job Satisfaction'].mean().reindex(['Small', 'Medium', 'Large'])
size_satisfaction.plot(kind='bar', color='gold')
plt.title('Job Satisfaction by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Average Job Satisfaction')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



#Count plot of Job Roles
plt.figure(figsize=(18, 12))
sns.countplot(data=df, y='Job Role', order=df['Job Role'].value_counts().index, palette='Paired')
plt.title('Employee Count by Job Role')
plt.xlabel('Number of Employees')
plt.ylabel('Job Role')
plt.tight_layout()
plt.show()



#Attrition by Income 
attrition_income = df.groupby('Monthly Income')['Attrition'].value_counts().unstack().fillna(0)
attrition_income.plot(kind='bar', stacked=True, color=['tomato', 'lightgreen'])
plt.title('Attrition by Income Level')
plt.xlabel('Monthly Income')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# histograms for numerical columns
numerical_columns=df.select_dtypes(include=['int','float']).columns
len(numerical_columns)
df[numerical_columns].hist(figsize=(20,15),bins=30);
plt.tight_layout()  
plt.show()

