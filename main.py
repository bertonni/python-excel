import pandas as pd
import pyperclip

answer = True
selection = ""
copy = ""
filtered = ""

def format_date(date):
  formatted = pd.to_datetime(date, errors='coerce').strftime("%d/%m/%Y")
  return formatted

def remove_last_chars(value):
  value = str(value)
  splitted = value.split(".")
  return splitted[0]

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

  df = df.dropna(how='any')

  df2 = df.copy()
  df2['Data Lcto'] = df2['Data Lcto'].map(format_date)
  df2['Cta Debito'] = df2['Cta Debito'].map(remove_last_chars)
  df2['Cta Credito'] = df2['Cta Credito'].map(remove_last_chars)
  df2['C Custo Deb'] = df2['C Custo Deb'].map(remove_last_chars)
  df2['C Custo Cred'] = df2['C Custo Cred'].map(remove_last_chars)

  #dates = list(df['Data Lcto'].dropna(how='any'))
  formatted_dates = df2['Data Lcto']
  debit_accounts = df2['Cta Debito']
  credit_accounts = df2['Cta Credito']
  cost_center_debit = df2['C Custo Deb']
  cost_center_credit = df2['C Custo Cred']
  descriptions = df['Hist Lanc'].dropna(how='any')

  unique_debit_accounts = get_unique_values(debit_accounts)
  unique_credit_accounts = get_unique_values(credit_accounts)
  unique_cost_center_debit = get_unique_values(cost_center_debit)
  unique_cost_center_credit = get_unique_values(cost_center_credit)
  unique_descriptions = descriptions.unique()


except FileNotFoundError as e:
  print('the file doesnt exists')


def menu():
  print("""
  1. Filtrar contas de débito
  2. Filtrar contas de crédito
  3. Filtrar centro de custo débito
  4. Filtrar centro de custo crédito
  5. Filtrar descrição
  6. Copiar todos os dados
  7. Exit/Quit
  """)

def show_debit_accounts():
  global answer
  global selection
  global filtered

  for val in unique_debit_accounts:
    print(val, sep=' ')

  selection = input("Digite o número da conta: ")
  if selection != "":
    filtered = df2.query('`Cta Debito` == @selection')
    if filtered.empty:
      print("Não há lançamentos nesta conta")
    else:
      print(filtered)
      filtered.to_clipboard(index=False)

    selection = ""
    return
  answer = input("press 0 to get back: ")

def show_credit_accounts():
  global answer
  global selection

  for val in unique_credit_accounts:
    print(val, sep=' ')

  selection = input("Digite o número da conta: ")
  if selection != "":
    filtered = df2.query('`Cta Credito` == @selection')
    if filtered.empty:
      print("Não há lançamentos nesta conta")
    else:
      print(filtered)
      filtered.to_clipboard(index=False)
    
    selection = ""
    answer = 0
    return
  answer = input("press 0 to get back: ")

def show_cost_debit():
  global answer
  global selection

  for val in unique_cost_center_debit:
    print(val, sep='\n')

  selection = input("Digite o número da conta: ")
  if selection != "":
    filtered = df2.query('`C Custo Deb` == @selection')
    if filtered.empty:
      print("Não há lançamentos nesta conta")
    else:
      print(filtered)
      filtered.to_clipboard(index=False)
    
    selection = ""
    answer = 0
    return
  answer = input("press 0 to get back: ")

def show_cost_credit():
  global answer
  global selection

  for val in unique_cost_center_credit:
    print(val, sep='\n')

  selection = input("Digite o número do centro de custo")
  if selection != "":
    filtered = df2.query('`C Custo Cred` == @selection')
    if filtered.empty:
      print("Não há lançamentos nesta conta")
    else:
      print(filtered)
      filtered.to_clipboard(index=False)
    
    selection = ""
    answer = 0
    return
  answer = input("press 0 to get back: ")

def show_descriptions():
  global answer
  global selection

  for val in unique_descriptions:
    print(val, sep='\n')

  selection = input("Digite o número do centro de custo")
  
  answer = input("press 0 to get back: ")

def show_data():
  global answer
  global copy

  print(df2)
  copy = input("Digite 8 para copiar o conteudo: ")
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
  elif answer == "8":
    pyperclip.copy(df2)
    print('Dados copiados para a área de transferência')
