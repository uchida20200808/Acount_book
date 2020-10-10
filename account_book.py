import pandas as pd

#read hiro's data:change file name.
hiro = pd.read_excel('hiro.xls')
hiro['payer'] = 'hiro'

#read misa's data:change file name.
misa = pd.read_excel('misa.xls')
misa['payer'] = 'misa'

#read credit's data:change file name.
credit = pd.read_excel('credit.xls')

#Merge hiro ,misa and credit into a single file
df = pd.concat([hiro,misa,credit])

#Clean up the df(empty columns)
df = df.dropna()

#save the single file
df.to_excel('merge_data.xls',index=False)

#How much did we pay and get money?
get_df = df.loc[df['収入/支出'] == '収入']
get_money = get_df['合計'].sum()

pay_df = df.loc[df['収入/支出'] == '支出']
pay_money = pay_df['合計'].sum()

print('収入の合計：')
print(get_money)

print('支出の合計：')
print(pay_money)

print('今月の収支：')
print(get_money + pay_money)

if (get_money + pay_money) >= 0:
    print('今月は黒字です')
else:
    print('今月は赤字です')

print('-' * 10)
#show each paytment
list = ['食費','日用','治療','交通','教育','葬祭','家賃','水光熱','ローン','通信','投資','わり','立て替え']
for i in list:
    each_df = df.loc[df['メモ'].str.contains(i)]
    print(each_df)
    print(i + 'の小計：')
    print(each_df['合計'].sum())

print('-' * 10)

#pay equally
hiro_devide = df.loc[(df['メモ'].str.contains(list[11])) & (df['payer'] == 'hiro')]
hiro1 = hiro_devide['合計'].sum()
misa_devide = df.loc[(df['メモ'].str.contains(list[11])) & (df['payer'] == 'misa')]
misa1 = misa_devide['合計'].sum()

#pay back
hiro_back = df.loc[(df['メモ'].str.contains(list[12])) & (df['payer'] == 'hiro')]
hiro2 = hiro_back['合計'].sum()
misa_back = df.loc[(df['メモ'].str.contains(list[12])) & (df['payer'] == 'misa')]
misa2 = misa_back['合計'].sum()

#payment in house
pay1 = (hiro1 + misa1) / 2 
pay2 = pay1 - misa1
pay3 = pay2 + misa2 - hiro2

if pay3 < 0:
    print('misa→hiroに支払い：')
    print(0 - pay3)
elif pay3 > 0:
    print('hiro→misaに支払い：')
    print(pay3)
else:
    print('支払いなし')






