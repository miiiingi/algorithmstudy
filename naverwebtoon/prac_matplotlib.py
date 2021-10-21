import seaborn as sns
from matplotlib import pyplot as plt
anscombe = sns.load_dataset('anscombe')
data_1 = anscombe.loc[anscombe['dataset'] == 'I']
data_2 = anscombe.loc[anscombe['dataset'] == 'II']
data_3 = anscombe.loc[anscombe['dataset'] == 'III']
data_4 = anscombe.loc[anscombe['dataset'] == 'IV']
fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)
axes1.plot(data_1['x'], data_1['y'], 'o')
axes2.plot(data_2['x'], data_2['y'], 'o')
axes3.plot(data_3['x'], data_3['y'], 'o')
axes4.plot(data_4['x'], data_4['y'], 'o')
axes1.set_title('data_1')
axes2.set_title('data_2')
axes3.set_title('data_3')
axes4.set_title('data_4')
plt.tight_layout()
plt.savefig('fig.png')
plt.clf()

tips = sns.load_dataset('tips')
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'])
plt.savefig('total_bill.png')
plt.clf()

fig_scatter = plt.figure()
sc_axes1 = fig_scatter.add_subplot(1, 1, 1)
sc_axes1.scatter(tips['total_bill'], tips['tip'])
sc_axes1.set_xlabel('total bill')
sc_axes1.set_ylabel('tip')
plt.tight_layout()
plt.savefig('total_bill to tips.png')
plt.clf()

fig_box = plt.figure()
bx_axes1 = fig_box.add_subplot(1, 1, 1)
bx_axes1.boxplot([tips.loc[tips['sex'] == 'Female', 'tip'], tips.loc[tips['sex'] == 'Male', 'tip']], labels = ['Female', 'Male'])
bx_axes1.set_xlabel('Sex')
bx_axes1.set_ylabel('tip')
plt.tight_layout()
plt.savefig('bxplot.png')
plt.clf()

tips.loc[tips['sex'] == 'Female', 'sex_color'] = 1
tips.loc[tips['sex'] == 'Male', 'sex_color'] = 0
fig_scatter2 = plt.figure()
sc_axes2 = fig_scatter2.add_subplot(1, 1, 1)
sc_axes2.scatter(x = tips['total_bill'], y = tips['tip'], s = tips['size'], c = tips['sex_color'])
sc_axes2.set_xlabel('total_bill')
sc_axes2.set_ylabel('tip')
plt.tight_layout()
plt.savefig('sc2.png')

