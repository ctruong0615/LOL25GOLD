# League of Legends Gold Difference Analysis

This is a final project for DSC 80 at UCSD which determines how likely a professional League of Legends Esports team is to win a match given gold differences at particular times and the number of drakes. Using many different forms of analysis such as statistical methods of hypothesis testing, the baseline model of a decision tree, and fairness analysis, this projects intends to foster better decision-making within the popular game to improve strategies and win rates.

Authors: Calvin Truong and Jake Wanderer

## Introduction
### Background
League of Legends (LoL) is one of the most popular video games in the world classified as a multiplayer online battle arena (MOBA). In the game, teams of 5 are split among 5 positions that occupy different parts of the map (that being Top, Jungle, Middle, Bottom, and Support) to compete against each other and destroy the enemy's 'nexus', an important objective that ends the game with its destruction. Developed by the North American video game developer and publisher, Riot Games, League of Legends is often one of, if not the most, popular game in the Esports industry. As a result, achieving victories and championship titles is crucial for players and organizations to generate thousands upon millions of dollars, so constantly adapting and developing new strategies for success is crucial to survive.

That being said, achieving a high win rate isn't necessarily obtained by simply being good at the game mechanically--understanding when and how to prioritize getting gold, the game's in-game currency, is equally, or debatably more, important. Since your character becomes stronger by securing more and more gold throughout several segments of the game, having more gold than your opponent can be seen as key to maximizing your chances of winning. Although you passively gain gold and can easily earn a small amount of gold by killing small creatures known as minions, bigger objectives like drakes (also known as dragons, but the term can be used interchangeably) can grant higher amount of golds. Though, it is actually the effects known as 'buffs' that objectives are targeted for, which can completely shift the odds of winning a match with powerful traits for a team.

With this in mind, we want to focus on this central question: **"How impactful is prioritizing elemental drakes in comparison to prioritizing gold to a team for their chances of winning?"**

### About the Dataset
The dataset in which we are working with is recorded professionally and thoroughly by Oracle's Elixir. In particular, we are focusing on data extracted from professional League of Legends matches that took place in 2025. Adding on, this dataset contains important information about statistics and results that can be used by players to understand ideal courses of action within their own games and lead others to strategically dominate against their opponents. Diving into a bit more about specific data collected from these matches, this includes features such as the differences in gold for teams at particular intervals, elemental drakes each team has slain, and results of each match.

Within the dataset offers a vast amount of matches, with there being 118932 rows containing information about those matches. Of the many columns that also help categorize all of the data, the following consists of the ones that were relevant to our central question and a brief description of each:

- `league`: This column indicates the Esports tournament in which a game was played.

- `side`: This column represents the side of a specific team or player in the game. There are two sides that are played indicated by the color `blue` and `red`.

- `goldat10`: This column represents how much gold a player or a team has at the 10-minute mark of a match.

- `goldat15`, `goldat20`, and `goldat25`: These columns function the same way `goldat10` does, but represent the amount of gold at the 15, 20, and 25-minute marks of a match respectively.

- `opp_goldat10`: This column represents how much gold an enemy player or enemy team has at the 10-minute mark of a match.
  
- `opp_goldat15`, `opp_goldat20`, and `opp_goldat25`: Similarly, each of these columns represent the same thing as `opp_goldat10`, but for their respective times within the match.

- `firstdragon`: This column indicates which team/player from a team was able to secure the first dragon slain in the match, which is represented with a **1** if successful and **0** if unsuccessful.
  
- `elementaldrakes`: This column quantifies the amount of elemental drakes that a player's team has slain in the match.
  
- `opp_elementaldrakes`: Similarly to `elementaldrakes`, this quantifies the amount of elemental drakes a player's opposing team has slain in the match.

- `dragons` and `opp_dragons`: These columns function similarly to `elementaldrakes` and `opp_elementaldrakes`, but are used to quantify every drake regardless of their elemental type.
  
- `result`: This column represents the outcome of a professional match with **1** representing a win and **0** representing a loss for a particular team or team member. 

## Data Cleaning and Exploratory Data Analysis
### Data Cleaning
When cleaning our data, only a handful of columns out of the dozens were kept while the other columns were dropped. We keep the columns `league`, `side`, `goldat10`, `goldat15`, `goldat20`, `goldat25`, `opp_goldat10`, `opp_goldat15`, `opp_goldat20`, `opp_goldat25`, `firstdragon`, `elementaldrakes`, `opp_elementaldrakes`, `dragons`, `opp_dragons`, and `result`. After getting all of the relevant columns for later steps, the head of the dataframe is what is displayed below. Additionally, it is important to note that this dataset will be further modified and explained based on the different analysis we need later.

[insert head of the dataframe]

### Univariate Analysis
For the univariate analysis, it was performed on the gold differences seen across different time intervals of the game, that being the 10, 15, 20, and 25-minute mark. The following histograms show those distributions on a histogram with the matching times respectively.

<iframe
  src="assets/univ1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/univ2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/univ3.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/univ4.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Seeing how each histogram contains data from very similar columns, we generalized the descriptions and elaborations of the plots.

Each histogram displays that the distribution of `golddiffat10`, `golddiffat15`, `golddiffat20`, and `golddiffat25` are each all normal. We can conclude that this data is balanced and predictable with its behavior, so each distribution can be used well for analysis.

### Bivariate Analysis
For our bivariate analysis, it was performed with each of the four gold differences columns and `result`.

<iframe
  src="assets/bivar1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/bivar2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/bivar3.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

<iframe
  src="assets/bivar4.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Again, since the bivariate analysis consisted of similar columns, we generalized the descriptions and elaborations of the plot.

Based on the four scatter plots, it is visually clear that when a player/team is ahead in gold compared to their opponent, with players/teams winning as they maintain a higher gold difference later into the game.

### Interesting Aggregates
[insert aggregates dataset]
Above displays some interesting aggregates that may be useful in our analysis. Here, we groupby firstdragon in our cleaned dataset and calculuate the mean of the statistics with numeric values. When examing each of the columns with one another, we are able to easily see at a first glance that teams that secure the first dragon are, on average, in the lead in terms of gold, elemental dragons slain, and wins. This could potentially show that securing the first dragon of the game can typically put a team ahead of gold, and will greatly support a team in winning a match.

## Assessment of Missingness
### NMAR Analysis
Within the entire dataset, there seem to be several columns that are not missing at random (NMAR), which include `goldat20`, `opp_goldat20`, `goldat25`, and `opp_goldat25`. These values can be NaN, even when `goldat10` and `goldat15` are not. That is because it is possible for the game to end before this time. I would argue that the true values here should be the values at the time the game ended. This means the true values should typically be smaller values, making the missingness dependent on the values.

### Missingness Dependency
This section uses permutation tests to determine whether or not the missingness of `golddiffat10` depends on two different columns, that being `league` and `side`. For both of the permutation tests, the test statistic chosen is Total Variance Distance (TVD) and the significance level that is chosen is 0.5.

To start off, `golddiffat10` will be tested with `league` to demonstrate that the missingness in `golddiffat10` is dependent on `league`.

We establish a null hypothesis and alternative hypothesis.
**Null Hypothesis:** The distribution of `league` when `golddiffat10` is missing is the same when `golddiffat10` is not missing.
**Alternative Hypothesis:** The distribution of `league` when `golddiffat10` is missing is ***not*** the same when `golddiffat10` is not missing.

The table below represents a distribution of `league` when `golddiffat10` is missing and when it is not missing.

<iframe
  src="assets/missingness1.html"
  width="900"
  height="900"
  frameborder="0"
></iframe>

Here, we find a TVD of 0.9907631405322191 and a p-value of 0.0 after performing the permutation test on the two columns. Below displays the empirical distribution of the TVDs. Using this information, we reject the null hypothesis in favor of the alternative hypothesis because the p-value is less than or equal to our significance level, which means that the distribution of `league` when `golddiffat10` is missing is ***not*** the same when `golddiffat10` is not missing. As a result, this demonstrates that the missingness of `golddiffat10` does depend on the `league` column.

<iframe
  src="assets/TVD1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

As for `golddiffat10` and `side`, we will test to demonstrate that the missingness in `golddiffat10` is not dependent on `league`, with the following null and alternative hypothesis in mind.

**Null Hypothesis:** The distribution of `side` when `golddiffat10` is missing is the same when `golddiffat10` is not missing.
**Alternative Hypothesis:** The distribution of `side` when `golddiffat10` is missing is ***not*** the same when `golddiffat10` is not missing.

Below is the observed distribution of `side` when `golddiffat10` is missing and when it is not missing.

<iframe
  src="assets/missingness2.html"
  width="900"
  height="900"
  frameborder="0"
></iframe>

Once finished performing permutation tests on the two columns, we find a TVD of 0.0 and a p-value of 1.0. Below shows the empirical distribution of the TVDs. Using this information, we fail to reject the null hypothesis in favor of the alternative hypothesis because the p-value is greater than our significance level, which means that the distribution of `side` when `golddiffat10` is missing is the same when `golddiffat10` is not missing. As a result, this demonstrates that the missingness of `golddiffat10` does not depend on the `side` column.

<iframe
  src="assets/TVD2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

## Hypothesis Testing

Our hypothesis test is conducted to determine if there is a significant difference between a team's amount of gold at 10 minutes when they secure the first dragon and a team's amount of gold at 10 minutes when they lose the first dragon. This testing is necessary because it will help us determine how impactful slaying the first dragon is for gold at 10 minutes for a teams, which can be important in understanding better decision-making and shifting strategies when trying to win a match of League of Legends.

**Null Hypothesis:** Team gold at 10 min for teams who won first dragon is equal to team gold at 10 min for teams who lost first dragon.

**Alternative Hypothesis:** Team gold at 10 min for teams who won first dragon is not equal to team gold at 10 min for teams who lost first dragon.

**Test Statistic:** Mean difference between team gold at 10 min for teams who won first dragon and lost first dragon.

**Significance Level:** 0.05

We chose to do a one-sided hypothesis test because it is expected that the team that got the firstdragon is ahead in the game, and therefore has more gold. Because we are doing a one-sided test, we are using Mean difference as our test statistic.

After performing our hypothesis test, we obtain a p-value of 0.0, which means we reject the null hypothesis in favor of the alternative hypothesis. We conclude that team gold at 10 minutes when teams win first drake is **not** the same as a team's gold when they lose first dragon, which can suggest that knowing how to play around the early dragon spawns can drastically favor the odds of winning for a team seeing how they can earn more gold and become stronger than their opponents.

## Framing a Prediction Problem

## Baseline Model

## Final Model

## Fairness Analysis

It is generally considered easier for red side to secure dragons, and blue side to get other objectives, such as baron and rift herald. Because we only used dragons in our model, we will investigate if this makes our model unfair for the blue or red side.

We will run a one sided hypothesis test to test if red has a greater recall than blue. This is what we would expect because it is easier for red to get dragons (which our model uses), and it is easier for blue to get other objectives like baron (which our model does not use). 

**Null Hypothesis:** The recall for blue side is greater than or equal to the recall for red side.

**Alternative Hypothesis:** The recall for red side is greater than the recall for blue side.

**Test Statistic:** Difference in recall between blue side and red side with the test set.

**Significance Level:** 0.05

