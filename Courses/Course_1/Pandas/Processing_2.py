import pandas as pd
import numpy as np

path = 'dataset/data6.xlsx'
df = pd.read_excel(path, sheet_name='Лист2')
print(df)

# **********************************************************************************************************************
# Example 7. Обработка пропусков
# **********************************************************************************************************************
df_new = df.dropna(axis=0, subset=['region']) # удаление NaN из выбранных столбцов
df['region'] = df['region'].fillna(method='ffill') # заполнение пустот вышестоящими значениями
df['value'] = df['value'].fillna(value=round(df['value'].mean(),1)) # заполнение пустот расчетным средним
print(df)
# **********************************************************************************************************************
# Example 8. Замена неверно введенных значений
# **********************************************************************************************************************
df['product'] = df['product'].replace('BBB_','BBB') # вариант 1. замена одного единсвенного значения
name_dict = {'AAA':'AAA','AA_':'AAA','BBB':'BBB','BBB_':'BBB','bbb':'BBB','CCC':'CCC', 'C':'CCC','DDD':'DDD',
             'EEE':'EEE','FFF':'FFF'}
df['product'] = df['product'].map(name_dict) # вариант 2. замена множества значений через словарь
print(df)
# **********************************************************************************************************************
# Example 9. Перестройка данных
# **********************************************************************************************************************
df_new1 = pd.DataFrame({'a':[1, 2, 3],
                    'b': [4, 5, 6],
                    'c': [7, 8, 9]},
                   index = [0, 1, 2]) # создание первого датафрейма
df_new2 = pd.DataFrame({'a':[11, 12, 13],
                    'b': [14, 15, 16],
                    'c': [17, 18, 19]},
                   index = [0, 1, 2]) # создание второго датафрейма

print(df_new1)
print(df_new2)

df_new3 = pd.concat([df_new1,df_new2], axis = 0) # объединение датафреймов по вертикали
df_new3 = pd.concat([df_new1,df_new2], axis = 1) # объединение датафреймов по горизонтали

df_new3 = pd.melt(df_new1).rename(columns={'variable':'var','value':'val'}) # ... (переводится как расплавление)
df_new4 = df_new3.pivot(index = None, columns='var', values='val') # операция обратная melt

print(df_new4)
# **********************************************************************************************************************
# Example 10. Комбинирование датафреймов
# **********************************************************************************************************************
df_new1 = pd.DataFrame({'x1':[1, 2, 3],
                    'x2': [4, 5, 6]},
                   index = [0, 1, 2]) # создание первого датафрейма
df_new2 = pd.DataFrame({'x1':[1, 2, 4],
                    'x3': [7, 8, 9]},
                   index = [0, 1, 2]) # создание второго датафрейма
print(df_new1)
print(df_new2)

df_new3 = pd.merge(df_new1,df_new2,how='left',on="x1")
df_new3 = pd.merge(df_new1,df_new2,how='right',on="x1")
df_new3 = pd.merge(df_new1,df_new2,how='inner',on="x1")
df_new3 = pd.merge(df_new1,df_new2,how='outer',on="x1")
print(df_new3)
# **********************************************************************************************************************
# Example 11. Еще варианты комбинирования датафреймов
# **********************************************************************************************************************
df_new1 = pd.DataFrame({'x1': [1, 2, 3],
                    'x2': [4, 5, 6]},
                   index=[0, 1, 2])  # создание первого датафрейма
df_new2 = pd.DataFrame({'x1': [1, 2, 4],
                    'x2': [4, 5, 9]},
                   index=[0, 1, 2])  # создание второго датафрейма
print(df_new1)
print(df_new2)

df_new3 = pd.merge(df_new1, df_new2)
df_new3 = pd.merge(df_new1, df_new2, how='inner')
df_new3 = pd.merge(df_new1, df_new2, how='outer')
print(df_new3)
# **********************************************************************************************************************
# Example 12. Группировка данных
# **********************************************************************************************************************
df = pd.read_excel(path, sheet_name='Лист1')
print(df)
df_new = df.groupby(by=['region']).agg({'value':['sum','min','max','count']}).T # группировка данных по 4 метрикам
                                                                                # с последующим траспонированием
df_new=df.groupby(by=['region']).size().to_frame(name='count_product').reset_index() # Группировка данных с
                                                    # последующим расчетом количества продаж по каждому региону
df['rank']=df.groupby(by=['region'])['value'].rank(method='first',ascending=True) # Применение группировки для
                                                                                    # ранжирования
print(df)
# **********************************************************************************************************************