import pandas as pd
import numpy as np
germancars={
    'company':['ford','mercedes','BMW','Audi'],
    'price':[23845,171995,153925,71400]
}

japanescars={
    'company':['Toyota','Honda','Nissan','Mitsubishi'],
    'price':[29995,23600,61500,58900]
}

df=pd.DataFrame(germancars)
fg=pd.DataFrame(japanescars)

print('Germancars','\n',df)
print()
print('Japanesecars','\n',fg)
carprice={
    'company':['Toyota','Honda','BMW','Audi'],
    'price':[23845,17995,135925,71400]
}

car_Horsepower={
    'company':['Toyota','Honda','BMW','Audi'],
    'Horsepower':[141,80,182,160]
}

ff=pd.DataFrame(carprice)
gg=pd.DataFrame(car_Horsepower)


print('carprice','\n',ff)
print()
print('car_Horsepower','\n',gg)


#merging two dataframes

result=ff.merge(gg)
print("\n",result)

ex_col=gg['Horsepower']
ff=ff.join(ex_col)
print(ff)





