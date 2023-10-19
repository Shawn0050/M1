# %%
import pandas as pd

# 创建包含值的字典
data = {
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E'],
    'Column3': [10.1, 20.2, 30.3, 40.4, 50.5]
}

# 使用字典创建DataFrame
df = pd.DataFrame(data)

def get(t,df,type):
    return min(df.iloc[-(t+1):-1][type])
a = get(3,df,'Column3')
print(a)
# %%
for i in range(41,60):
    print(f'schedule.every().hour.at(":{i}").do(run_jobs)')
# %%





