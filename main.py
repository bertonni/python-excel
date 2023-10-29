import pandas as pd
import math

answer = True

def format_date(date):
  formatted = pd.to_datetime(date, errors='coerce').strftime("%d/%m/%Y")
  return formatted

def remove_last_chars(value):
  value = str(value)
  value = value[:-4]
  
  return value

def get_unique_values(data):
  unique_list = []

  for val in data:
    if val not in unique_list:
      unique_list.append(val)
  
  return unique_list

try:
  global df
  global debit_accounts
  global credit_accounts
  global cost_center_debit
  global cost_center_credit
  global descriptions

  global unique_debit_accounts
  global unique_credit_accounts
  global unique_cost_center_debit
  global unique_cost_center_credit
  global unique_descriptions
  
  xl = pd.read_excel('211008005-2022.xlsx', header=2)
  df = pd.DataFrame(data=xl)

  df = df.dropna(how='all')
  df['Cta Debito'] = df['Cta Debito'].to_string()

  df2 = df.copy()
  df2['Cta Debito'] = df2['Cta Debito'].map(remove_last_chars)
  print(df2)

  #dates = list(df['Data Lcto'].dropna(how='any'))
  #formatted_dates = list(map(format_date, dates))
  #debit_accounts = list(map(remove_last_chars, df['Cta Debito'].dropna(how='any')))
  #credit_accounts = list(map(remove_last_chars, df['Cta Credito'].dropna(how='any')))
  #cost_center_debit = list(map(remove_last_chars, df['C Custo Deb'].dropna(how='any')))
  #cost_center_credit = list(map(remove_last_chars, df['C Custo Cred'].dropna(how='any')))
  #descriptions = df['Hist Lanc'].dropna(how='any')

  #unique_debit_accounts = get_unique_values(debit_accounts)
  #unique_credit_accounts = get_unique_values(credit_accounts)
  #unique_cost_center_debit = get_unique_values(cost_center_debit)
  #unique_cost_center_credit = get_unique_values(cost_center_credit)
  #unique_descriptions = descriptions.unique()


except FileNotFoundError as e:
  print('the file doesnt exists')


def menu():
  print("""
  1.Show debit accounts
  2.Show credit accounts
  3.Show cost debit
  4.Show cost credit
  5.Show descriptions
  6.Show data
  7.Exit/Quit
  """)
"""
def show_debit_accounts():
  global answer
  for val in unique_debit_accounts:
    print(val, sep=' ')

  answer = input("press 0 to get back: ")

def show_credit_accounts():
  global answer
  for val in unique_credit_accounts:
    print(val, sep=' ')

  answer = input("press 0 to get back: ")

def show_cost_debit():
  global answer
  for val in unique_cost_center_debit:
    print(val, sep='\n')

  answer = input("press 0 to get back: ")

def show_cost_credit():
  global answer
  for val in unique_cost_center_credit:
    print(val, sep='\n')

  answer = input("press 0 to get back: ")

def show_descriptions():
  global answer
  for val in unique_descriptions:
    print(val, sep='\n')

  answer = input("press 0 to get back: ")

def show_data():
  global answer
  print(df)
  answer = input("press 0 to get back: ")

while answer:
  menu()
  answer = input("Option: ")

  if answer == "1":
    show_debit_accounts()
  elif answer == "2":
    show_credit_accounts()
  elif answer == "3":
    show_cost_debit()
  elif answer == "4":
    show_cost_credit()
  elif answer == "5":
    show_descriptions()
  elif answer == "6":
    show_data()
  elif answer == "7":
    answer = None
"""