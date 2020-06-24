#%%
import numpy as np
import pandas as pd
import lifelines

# %%
#setting up first arm of trial
patient_ids = [x for x in range(100)]
followup = list(np.random.choice(50,size=100,replace=True))
followup.sort()
# %%
eventtype = list(np.random.binomial(1,0.6,size=100))
data = [{'patient_id':id,'followup':followups,'eventtype':eventtypes} for id,followups,eventtypes in zip(patient_ids,followup,eventtype)]
df = pd.DataFrame(data)
df['scenario'] = 'A'

# %%
df.loc[(df['followup']>=48),'eventtype'] = 0
df.loc[(df['followup']>=48),'followup'] = 48
# %%
df

# %%
#setting up second arm of trial
patient_ids_b = [x for x in range(100)]
followup_b = list(np.random.choice(65,size=100,replace=True))
followup_b.sort()

# %%
eventtype_b = list(np.random.binomial(1,0.5,size=100))
data_b = [{'patient_id':id,'followup':followups,'eventtype':eventtypes} for id,followups,eventtypes in zip(patient_ids_b,followup_b,eventtype_b)]
df_b = pd.DataFrame(data_b)
df_b['scenario'] = 'B'
df_b

# %%
df_b.loc[(df_b['followup']>=48),'eventtype'] = 0
df_b.loc[(df_b['followup']>=48),'followup'] = 48

# %%
df_b

# %%
final_dataset = pd.concat([df,df_b],ignore_index=True)
final_dataset.head()

# %%
import matplotlib.pyplot as plt

ax = plt.subplot(111)
kmf = lifelines.KaplanMeierFitter()

for name, grouped_df in final_dataset.groupby('scenario'):
    kmf.fit(grouped_df['followup'], grouped_df['eventtype'], label=name)
    kmf.plot(ax=ax)



#%%




# %%

# %%


# %%
