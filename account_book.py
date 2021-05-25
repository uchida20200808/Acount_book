#エクセルを操作するためにpandasをインポートする
import pandas as pd

#うっちゃんの家計簿に支払い者としてhiroを入れる
hiro = pd.read_excel('hiro.xls')
hiro['payer'] = 'hiro'

#妻の家計簿に支払い者としてmisaを入れる
misa = pd.read_excel('misa.xls')
misa['payer'] = 'misa'

#クレジットカード払などのデータを読み込む
credit = pd.read_excel('credit.xls')

#3つのエクセルファイルを統合する
df = pd.concat([hiro,misa,credit])

#統合した家計簿をmerge_data.xlsとして保存する
df.to_excel('merge_data.xls',index=False)

#収入の合計額を計算・表示
get_df = df.loc[df['収入/支出'] == '収入']
get_money = get_df['合計'].sum()
print('収入の合計：')
print(get_money)

#支出の合計額を計算・表示
pay_df = df.loc[df['収入/支出'] == '支出']
pay_money = pay_df['合計'].sum()
print('支出の合計：')
print(pay_money)

#今月の収支を計算
print('今月の収支：')
print(get_money + pay_money)

#収支がプラスなら黒字、マイナスなら赤字と表示
if (get_money + pay_money) >= 0:
    print('今月は黒字です')
else:
    print('今月は赤字です')

print('-' * 10)

#支出の項目を自動集計して計算する
list = ['食費','日用','治療','交通','教育','葬祭','家賃','水光熱','ローン','通信','投資','わり','立て替え']
for i in list:
    each_df = df.loc[df['メモ'].str.contains(i)]
    print(each_df)
    print(i + 'の小計：')
    print(each_df['合計'].sum())

print('-' * 10)

#割り勘の合計額を計算
hiro_devide = df.loc[(df['メモ'].str.contains(list[11])) & (df['payer'] == 'hiro')]
hiro1 = hiro_devide['合計'].sum()
misa_devide = df.loc[(df['メモ'].str.contains(list[11])) & (df['payer'] == 'misa')]
misa1 = misa_devide['合計'].sum()

#立て替えの合計額を計算
hiro_back = df.loc[(df['メモ'].str.contains(list[12])) & (df['payer'] == 'hiro')]
hiro2 = hiro_back['合計'].sum()
misa_back = df.loc[(df['メモ'].str.contains(list[12])) & (df['payer'] == 'misa')]
misa2 = misa_back['合計'].sum()

#割り勘と立て替えの合計額からうっちゃんと妻のどちらが多く支払っているか計算
pay1 = (hiro1 + misa1) / 2 
pay2 = pay1 - misa1
pay3 = pay2 + misa2 - hiro2

#生活費を均等に払うためにお金を渡す額を表示
if pay3 < 0:
    print('misa→hiroに支払い：')
    print(0 - pay3)
elif pay3 > 0:
    print('hiro→misaに支払い：')
    print(pay3)
else:
    print('支払いなし')
