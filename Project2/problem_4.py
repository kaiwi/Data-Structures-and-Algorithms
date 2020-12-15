# Do NOT change this code!
import numpy as np
import pandas as pd

# np.random.seed(25)
# ar = np.random.randn(1000)
# ar = ar * 100
# ar = ar.astype('int8')
# ar = ar.reshape((200, 5))
#
# max = np.max(ar)
# min = np.min(ar)
# mean = np.mean(ar)
# print(max)
# print(min)
# print(mean)
#
# print(ar)
# locA = ar[7, 1]
# print(locA)
# g_mean = ar > np.mean(ar)
# print(np.count_nonzero(g_mean))
#
# # Using numpy, what is the sum of the values of the array ar that are greater than -5 and less than or equal to 20.
# # Create array of bool to pass to np.sum() where condition is true
# conditions = (ar > -5) & (ar < 20)
# # print(conditions)
# print(np.sum(ar, None, None, None, np._NoValue, np._NoValue, conditions))
# print(np.where(ar == max))

################################################
def scrub(col):
    data = pd.read_csv('2019_production_reports.csv', usecols=col)
    return data.dropna()

#data = scrub(['report_date','oil_vol'])
#print(data.loc[data['oil_vol'].idxmax()])
df = scrub(['api_county_code','report_date'])
print(df)


dates = df.loc[df['report_date'].str[-2:] == '19']
print(dates)
print(dates.groupby(['api_county_code']).size().idxmax())


# Total gas flared



#oil_max = data['oil_vol'].idxmax()
#print(data['oil_vol'].argmax())
#print(data.loc([776424],'report_date'))




