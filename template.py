#!/usr/bin/env python
# coding: utf-8

# # League of Legends 
# 
# **Name(s)**: (Calvin Truong, Jake Wanderer)
# 
# **Website Link**: (your website link)

# In[1]:


import pandas as pd
import numpy as np
from pathlib import Path

import plotly.express as px
pd.options.plotting.backend = 'plotly'

# from dsc80_utils import * # Feel free to uncomment and use this.


# In[2]:


lol_fp = Path('data') / '2025_lol_data.csv'
matches = pd.read_csv(lol_fp)


# In[3]:


#matches[['gameid', 'position', 'playername', 'playerid', 'teamname', 'teamid', 'participantid', 'result']].head(24)

temp = matches[['gameid','gamelength','golddiffat10']]
temp[temp['golddiffat10'].isna()]
#temp[temp['gamelength'] <= 1500]


# In[4]:


#matches[['firstdragon','elementaldrakes', 'opp_elementaldrakes', 'infernals', 'mountains', 'chemtechs', 'hextechs', 'oceans', 'clouds', 'hextechs', 'dragons (type unknown)']]


# In[5]:


gold_dif_vs_win_percentage = matches.columns[matches.columns.str.contains('golddiffat')].tolist()
#gold_dif_vs_win_percentage.extend(['gameid','result'])
gold_dif_vs_win_percentage.append('result')
gold_differences = matches[sorted(gold_dif_vs_win_percentage)]
#gold_differences.head(12)
gold_columns = [col for col in gold_differences.columns if col.startswith('golddiffat')]
gold_columns


# ## Step 1: Introduction

# Q1: Approximately how much gold at 10 minutes is a first dragon "worth" and void grubs (in terms of winning the game)? Q2: What is more important..Void Grubs or First Dragon? Also herald or second dragon? Q3: What side is more likely to win the game, and how is it related to who gets the objectives (e.g. dragons, baron)? Q4: How well do heavily banned champions actually perform?
# 
# We are likely going to put more emphasis on question 1. We can compare the number of drakes and the number of drakes the opponent has. For our visualization, we should try...For the bivariate analysis, we need two plots --> two good ones could be one with a plot of gold difference and win percentage (and basically have a different line/different color for each gold difference at the different minute intervals) and one with number of dragons vs. number of opponent dragons

# ## Step 2: Data Cleaning and Exploratory Data Analysis

# In[6]:


lol_fp = Path('data') / '2025_lol_data.csv'
matches = pd.read_csv(lol_fp)


# In[7]:


matches


# In[8]:


# gold_dif_and_win_percentage = matches.columns[matches.columns.str.contains('golddiffat')].tolist()
# gold_dif_and_win_percentage.append('result')
# gold_differences = matches[sorted(gold_dif_vs_win_percentage)]
# gold_columns = [col for col in gold_differences.columns if col.startswith('golddiffat')]

cleaned = matches.copy(deep=False)
gold_info = matches.columns[matches.columns.str.contains('gold')]
gold_df = matches[gold_info]
#cleaned = cleaned.set_index(['gameid','gameid', 'league','side']).loc['11715-11715_game_1'][gold_info]
cleaned = cleaned.set_index(['gameid', 'league','side'])[gold_info]
cleaned = cleaned.reset_index()
cleaned


# In[9]:


gold_dif_vs_win_percentage = matches.columns[matches.columns.str.contains('golddiffat')].tolist()
gold_dif_vs_win_percentage.append('result')
gold_differences = matches[sorted(gold_dif_vs_win_percentage)]
gold_columns = [col for col in gold_differences.columns if col.startswith('golddiffat')]
for col in gold_columns:
    fig = px.histogram(
        gold_differences,
        x=col,
        title=f'Gold Difference Distribution at {col[10:]} Minutes',
        labels={col: f'Gold Differences at {col[10:]} mins.'}
    )
    fig.show()


# In[10]:


# melted = gold_differences.melt(
#     id_vars=['result'],
#     var_name='Time In-Game', 
#     value_name='Gold Difference'
# )
# melted['Result'] = melted_gold['result'].map({0: 'Loss', 1: 'Win'})

# fig2 = px.box(
#     melted, 
#     x='Time In-Game', 
#     y='Gold Difference', 
#     color='Result',
#     title='Gold Difference Distribution - Wins vs Losses'
# )
# fig2.show()

gold_columns = [col for col in gold_differences.columns if col.startswith('golddiffat')]
for col in gold_columns:
    fig = px.scatter(gold_differences, x=col, y='result')
    mean_loss = gold_differences.loc[gold_differences['result'] == 0, col].mean()
    mean_win = gold_differences.loc[gold_differences['result'] == 1, col].mean()
    
    # Add vertical lines
    fig.add_vline(x=mean_loss, line_dash="dash", line_color="red",
                  annotation_text="Mean Loss", annotation_position="top left")
    fig.add_vline(x=mean_win, line_dash="dash", line_color="green",
                  annotation_text="Mean Win", annotation_position="top right")
    fig.show()

#best to do scatter plot, win or lose is going to be a 1 or 0, gold difference on the x axis, result on the y axis


# ## Step 3: Assessment of Missingness

# In[11]:


cleaned['golddiffat10_missing'] = cleaned['golddiffat10'].isna()
#cleaned

league_gold10_prop = (
    cleaned
    .groupby(['golddiffat10_missing', 'league'])
    .size()
    .reset_index(name='count')
    .groupby('golddiffat10_missing')
    .apply(lambda x: x.assign(proportion=x['count'] / x['count'].sum()))
    .reset_index(drop=True)
)
fig = px.bar(
    league_gold10_prop,
    x='proportion',
    y='league',
    color='golddiffat10_missing',
    barmode='group',
    orientation='h',
    labels={'golddiffat10_missing': 'Gold Difference at 10 Minutes - Missing'}
)
fig.update_layout(
    title='League by Gold Difference at 10 Minutes Missingness',
    xaxis_title='Proportion',
    yaxis_title='League',
    width=900,
    height=500
)
fig.show()


# In[30]:


def tvd(p, q):
    return 0.5 * np.abs(p - q).sum()
obs = league_gold10_prop.pivot(
    index='league',
    columns='golddiffat10_missing',
    values='proportion'
)
observed_stat = tvd(obs[False], obs[True])

stats = []
for i in range(100):
    shuffled = cleaned.assign(
        golddiffat10_missing=np.random.permutation(cleaned['golddiffat10_missing'])
    )
    temp = (
        shuffled
        .groupby(['golddiffat10_missing', 'league'])
        .size()
        .reset_index(name='count')
    )
    temp['proportion'] = (
        temp.groupby('golddiffat10_missing')['count']
           .transform(lambda x: x / x.sum())
    )
    temp_pivot = temp.pivot(
        index='league',
        columns='golddiffat10_missing',
        values='proportion'
    )
    stat = tvd(temp_pivot[False], temp_pivot[True])
    stats.append(stat)
p_value = (np.array(stats) >= observed_stat).mean()
p_value


# In[20]:


tvd(obs[False], obs[True])


# In[24]:


stats_array = np.array(stats)
plt.figure(figsize=(10,5))
plt.hist(stats_array, bins=30, color='blue')
plt.axvline(observed_stat, color='red', linestyle='solid', linewidth=2, label='Observed TVD')
plt.xlabel('Total Variation Distance (TVD)')
plt.ylabel('Probability')
plt.title('Empirical Distribution of TVD')
plt.legend()
plt.show()


# In[25]:


league_gold10_prop2 = (
    cleaned
    .groupby(['golddiffat10_missing', 'side'])
    .size()
    .reset_index(name='count')
    .groupby('golddiffat10_missing')
    .apply(lambda x: x.assign(proportion=x['count'] / x['count'].sum()))
    .reset_index(drop=True)
)
fig = px.bar(
    league_gold10_prop2,
    x='proportion',
    y='side',
    color='golddiffat10_missing',
    barmode='group',
    orientation='h',
    labels={'golddiffat10_missing': 'Gold Difference at 10 Minutes - Missing'}
)
fig.update_layout(
    title='League by Gold Difference at 10 Minutes Missingness',
    xaxis_title='Proportion',
    yaxis_title='Side',
    width=900,
    height=500
)
fig.show()


# In[29]:


obs = league_gold10_prop2.pivot(
    index='side',
    columns='golddiffat10_missing',
    values='proportion'
)
observed_stat2 = tvd(obs[False], obs[True])
stats2 = []
for i in range(100):
    shuffled = cleaned.assign(
        golddiffat10_missing=np.random.permutation(cleaned['golddiffat10_missing'])
    )
    temp2 = (
        shuffled
        .groupby(['golddiffat10_missing', 'side'])
        .size()
        .reset_index(name='count')
    )
    temp2['proportion'] = (
        temp2.groupby('golddiffat10_missing')['count']
           .transform(lambda x: x / x.sum())
    )
    temp_pivot2 = temp2.pivot(
        index='side',
        columns='golddiffat10_missing',
        values='proportion'
    )
    stat2 = tvd(temp_pivot2[False], temp_pivot2[True])
    stats2.append(stat)
p_value2 = (np.array(stats2) >= observed_stat2).mean()
p_value2


# In[28]:


stats_array2 = np.array(stats2)
plt.figure(figsize=(10,5))
plt.hist(stats_array2, bins=30, color='blue')
plt.axvline(observed_stat, color='red', linestyle='solid', linewidth=2, label='Observed TVD')
plt.xlabel('Total Variation Distance (TVD)')
plt.ylabel('Probability')
plt.title('Empirical Distribution of TVD')
plt.legend()
plt.show()


# ## Step 4: Hypothesis Testing

# In[15]:


# def permutation_test(df, n_permutations=10000):
#     gold = df['golddiffat10'].values
#     results = df['result'].values
#     winning_gold = df[df['result'] == 1]['golddiffat10']
#     losing_gold = df[df['result'] == 0]['golddiffat10']
#     observed_diff = winning_gold.mean() - losing_gold.mean()
#     permuted_diffs = []
#     for _ in range(n_permutations):
#         shuffled_results = np.random.permutation(results)
#         shuffled_winning = gold[shuffled_results == 'Win']
#         shuffled_losing = gold[shuffled_results == 'Loss']
#         diff = shuffled_winning.mean() - shuffled_losing.mean()
#         permuted_diffs.append(diff)
#     p_value = np.mean(np.array(permuted_diffs) >= observed_diff)
#     return observed_diff, p_value, permuted_diffs
# observed_diff, p_value, permuted_diffs = permutation_test(gold_differences, n_permutations=10000)
# print(f"Observed difference in means: {observed_diff}")
# print(f"P-value: {p_value}")


# ## Step 5: Framing a Prediction Problem

# In[16]:


# TODO


# ## Step 6: Baseline Model

# In[17]:


# TODO


# ## Step 7: Final Model

# In[18]:


# TODO


# ## Step 8: Fairness Analysis

# In[19]:


# TODO

