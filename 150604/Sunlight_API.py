
# coding: utf-8

# In[620]:

import requests
from pprint import pprint
import json
import numpy as np
import pandas as pd
import sklearn as sk
import sunlight


# In[621]:

votes = sunlight.congress.votes(fields='chamber,bill_id,breakdown.total,question,required,voted_at',vote_type='passage',per_page=500)


# In[622]:

votes = pd.DataFrame.from_dict(votes)
votes = votes[votes.question.str.contains('Passage')]


# In[623]:

votes['yeas'] = np.zeros(len(votes))
votes['nays'] = np.zeros(len(votes))
votes['no_votes'] = np.zeros(len(votes))
votes['split'] = np.zeros(len(votes))


# In[624]:

for i in votes.index: 
    votes['yeas'][i] = votes['breakdown'][i]['total']['Yea']
    votes['nays'][i] = votes['breakdown'][i]['total']['Nay']
    votes['no_votes'][i] = votes['breakdown'][i]['total']['Not Voting']
    votes['split'][i] = votes['yeas'][i]/(votes['yeas'][i]+votes['nays'][i])


# In[625]:

votes = votes.drop('breakdown',1)


# In[626]:

votes.head(1)


# In[629]:

bills = sunlight.congress.bills(fields='bill_id,bill_type,last_action_at,official_title,short_title,popular_title,nicknames,keywords,summary,summary_short,history.active_at,sponsor_id,cosponsor_ids,cosponsors_count,withdrawn_cosponsor_ids,withdrawn_cosponsors_count,committee_ids,related_bill_ids',per_page=500)
bills = pd.DataFrame.from_dict(bills)

# It would be cool to do this part below by in general checking for the type of a column to be a list and then doing the operation. But don't know how to generalize column name that way.
bills = pd.concat([bills, bills['committee_ids'].str.join(sep=', ').str.get_dummies(sep=', ')], axis=1, join='outer')
bills = pd.concat([bills, bills['cosponsor_ids'].str.join(sep=', ').str.get_dummies(sep=', ')], axis=1, join='outer')
bills = pd.concat([bills, bills['related_bill_ids'].str.join(sep=', ').str.get_dummies(sep=', ')], axis=1, join='outer')
bills = pd.concat([bills, bills['keywords'].str.join(sep=', ').str.get_dummies(sep=', ')], axis=1, join='outer')
bills = pd.concat([bills, bills['withdrawn_cosponsor_ids'].str.join(sep=', ').str.get_dummies(sep=', ')], axis=1, join='outer')
bills = bills.drop(['committee_ids','cosponsor_ids','related_bill_ids','keywords','withdrawn_cosponsor_ids'],1)

bills.head(1)


# In[630]:

complete = pd.concat([bills, votes], axis=1, join='outer')


# In[631]:

complete.head(20)



