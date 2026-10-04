import pandas as pd
import ast

df = pd.read_csv("universityDetails/research.csv", encoding="cp1252")
datarecord = []
# data = []

# for _, row in df.iterrows():
#     row_dict = {}

#     for column in df.columns:
#         value = row[column]

#         if pd.isna(value):
#             row_dict[column] = None
#         elif isinstance(value, str):
#             try:
#                 row_dict[column] = ast.literal_eval(value)
#             except (ValueError, SyntaxError):
#                 row_dict[column] = value
#         else:
#             row_dict[column] = value

#     data.append(row_dict)

# print(data)

# for i in range(0, len(df)-1):
#     print(df.iloc[i], "\n\n")

for i in range(0, 1):
    record = {
        "USA": [
            {
                "university_courses_details": {
                    "university_name": df.iloc[i, 1],
                    "location": df.iloc[i, 2],
                    "available_courses": ast.literal_eval(df.iloc[i, 3]),
                    "program_duration": ast.literal_eval(df.iloc[i, 4]),
                    "tuition_fees": ast.literal_eval(df.iloc[i, 5]),
                    "cost_of_attendance": ast.literal_eval(df.iloc[i, 6]),
                }
            },
            {
                "expenses_details": {
                    "estimated_living_expenses": df.iloc[i, 7],
                }
            },
            {
                "enrollment_requirements": {
                    "admission_requirements": ast.literal_eval(df.iloc[i, 8]),
                    "academic_or_gpa_requirements": ast.literal_eval(df.iloc[i, 9]),
                    "language_requirements": ast.literal_eval(df.iloc[i, 10]),
                    "required_tests": ast.literal_eval(df.iloc[i, 11]),
                    "application_requirements_and_documents": ast.literal_eval(df.iloc[i, 12]),
                    "application_deadlines_and_intakes": ast.literal_eval(df.iloc[i, 13]),
                    "application_fees": ast.literal_eval(df.iloc[i, 14]),
                    "proof_of_financial_support": ast.literal_eval(df.iloc[i, 20]),
                }
            },
            {
                "additional_info": {
                    "scholarships_and_aids": ast.literal_eval(df.iloc[i, 15]),
                    "opportunities": ast.literal_eval(df.iloc[i, 16]),
                    "housing_and_accomodation": ast.literal_eval(df.iloc[i, 17]),
                    "insurances": df.iloc[i, 18],
                    "acceptable_international_students": ast.literal_eval(df.iloc[i, 19]),
                }
            },
        ]
    }
    datarecord.append(record)

print(datarecord)
