# %%
a = 2
b = 3 
if a > b-1:
    print('yes')
else:
    print('no')

def run(a,b):
    if a > b-1:
        print('yes')
    else:
        a += 1
        run(a,b)

run(2,3)
# %%
