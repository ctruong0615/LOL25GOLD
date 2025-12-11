# League of Legends Gold Difference Analysis

This is a final project for DSC 80 at UCSD which determines how likely a professional League of Legends Esports team is to win a match given gold differences at particular times and the number of drakes. Using many different forms of analysis such as statistical methods of hypothesis testing, the baseline model of a decision tree, and fairness analysis, this projects intends to foster better decision-making within the popular game to improve strategies and win rates.

Authors: Calvin Truong and Jake Wanderer

## Introduction
### Background
League of Legends (LoL) is a popular video games in the world classified as a multiplayer online battle arena (MOBA). In the game, teams of 5 are split among 5 positions that occupy different parts of the map (that being Top, Jungle, Middle, Bottom, and Support) to compete against each other and destroy the enemy's 'nexus', an important objective that ends the game with its descrution. Developed by the North American video game developer and publishered, Riot Games, League of Legends is often one of, if not the most, popular game in the Esports industry. As a result, achieving victories and championship titles is crucial for players and organizations to generate thousands upon millions of dollars, so constantly adapting and developing new strategies for success is crucial to survive.

That being said, achieving a high win rate isn't necessarily obtained by simply being good at the game mechanically--understanding when and how to prioritize getting gold, the game's in-game currency, is equally, or debatably more, important. Since your character becomes stronger by securing more and more gold throughout several segments of the game, having more gold than your opponent can be seen as key to maximizing your chances of winning. Although you passively gain gold and can easily earn a small amount of gold by killing small creatures known as minions, bigger objectives like drakes (also known as dragons, but the term can be used interchangeably) grant massive amount of golds that can completely shift the odds of winning a match. Each game also spawns in different types of unique drakes (e.g. Chemtech, Infernal, Mountain, etc.), and being able to slay the first drake at earlier stages of the game has the potential to drastically impact the odds of the match positively for that team from its gold and effects.

With this in mind, we want to focus on this central question: **"How impactful is prioritizing elemental drakes in terms of gold differences and win rates for a team?"**

### About the Dataset
The dataset in which we are working with is recorded professionally and thoroughly by Oracle's Elixir. In particular, we are focusing on data extracted from professional League of Legends matches that took place in 2025. Adding on, this dataset contains important information about statistics and results that can be used by players to understand ideal courses of action within their own games and lead others to strategically dominate against their opponents. Diving into a bit more about specific data collected from these matches, this includes features such as the differences in gold for teams at particular intervals, elemental drakes each team has slain, and results of each match.

Within the dataset offers a vast amount of matches, with there being 118932 rows containing information about those matches. Of the many columns that also help categorize all of the data, the following consists of the ones that were relevant to our central question and a brief description of each:

-`league`:

-`side`:

- `golddiffat10`: This column represents the difference in gold between a player and the player of the corresponding position on the opposing team at the 10-minute mark of a match. A positive value represents that the player is ahead in gold to their opponent while a negative value indicates that a player is behind in gold.
  
- `golddiffat15`, `golddiffat20`, and `golddiffat25`: Similarly, each of these columns represent the same thing as `golddiffat10`, but for their respective times within the match.

- `firstdragon`: This column indicates which team/player from a team was able to secure the first dragon slain in the match, which is represented with a **1** if successful and **0** if unsuccessful.
  
- `elementaldrakes`: This column quantifies the amount of elemental drakes that a player's team has slain in the match.
  
- `opp_elementaldrakes`: Similarly to `elementaldrakes`, this quantifies the amount of elemental drakes a player's opposing team has slain in the match.

- `dragons` and `opp_dragons`: These columns function similarly to `elementaldrakes` and `opp_elementaldrakes`, but are used to quantify every drakes regardless of their elemental type.
  
- `infernals`: N/A
  
- `mountains`: N/A
  
- `clouds`: N/A
  
- `oceans`: N/A
  
- `chemtechs`: N/A
  
- `hextechs`: N/A
  
- `dragons (type unknown)`: N/A

- `result`: This column represents the outcome of a professional match with **1** representing a win and **0** representing a loss for a particular team or team member. 

## Data Cleaning and Exploratory Data Analysis
### Data Cleaning
lalalalalallalallala

### Univariate Analysis
lalalalalala

### Bivariate Analysis
lalallala

### Interesting Aggregates
lalalalalalalal

## Assessment of Missingness
### NMAR Analysis
Within the entire dataset, there seems to be a several columns that are not missing at random (NMAR), which includes `ban1`, `ban2` `ban3` `ban4` `ban5`. When analyzing these columns, it is apparent that missingness does not depend on any other columns, and it is only these columns whose values are not missing based on a pattern or trend of some sort. When thinking about this from the perspective of a player, the player can simply choose to not ban a champion, perhaps due to strategic reasons. As a result, these columns should be NMAR because there is a chance that missingness just depends on the actual missing value as players cause this missing value from deciding not to ban.

Additionally, there is a rather simple method of obtaining the data needed to explain the missingness, which would make these columns missing at random (MAR_. To do this, we can organize data into a column `used_all_bans`, which contains a value **1** for every ban has been made by players, and a **0** if every ban has not been made.

### Missingness Dependency
This section uses permutation tests to determine whether or not the missingness of `golddiffat10` depends on two different columns, that being `league` and `side`. For both of the permutation tests, the test statistic chosen is Total Variance Distance (TVD) and the significance level that is chosen is 0.5.

To start off, `golddiffat10` will be tested with `league` to demonstrate that the missingness in `golddiffat10` is dependent on `league`.

We establish a null hypothesis and alternative hypothesis.
**Null Hypothesis:** The distribution of `league` when `golddiffat10` is missing is the same when `golddiffat10` is not missing.
**Alternative Hypothesis:** The distribution of `league` when `golddiffat10` is missing is ***not*** the same when `golddiffat10` is not missing.


As for `golddiffat10` and `side`, we will test to demonstrate that the missingness in `golddiffat10` is not dependent on `league`, with the following null and alternative hypothesis in mind.

**Null Hypothesis:** The distribution of `side` when `golddiffat10` is missing is the same when `golddiffat10` is not missing.
**Alternative Hypothesis:** The distribution of `side` when `golddiffat10` is missing is ***not*** the same when `golddiffat10` is not missing.


## Hypothesis Testing

## Framing a Prediction Problem

## Baseline Model

## Final Model

## Fairness Analysis
