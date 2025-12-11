# League of Legends Gold Difference Analysis
This is a final project for DSC 80 at UCSD which determines how likely a professional League of Legends Esports team is to win a match given gold differences at particular times and the number of drakes/types of drakes slain. Using many different forms of analysis such as statistical methods of hypothesis testing, the baseline model of a decision tree, and fairness analysis, this projects intends to foster better decision-making within the popular game to improve strategies and win rates.

Authors: Calvin Truong and Jake Wanderer

## Introduction
### Background
League of Legends (LoL) is a popular video games in the world classified as a multiplayer online battle arena (MOBA). Developed by the North American video game developer and publishered, Riot Games, League of Legends is often one of, if not the most, popular game in the Esports industry. As a result, achieving victories and championship titles is crucial for players and organizations to generate thousands upon millions of dollars, so constantly adapting and developing new strategies for success is crucial to survive.

That being said, achieving a high win rate isn't necessarily obtained by simply being good at the game mechanically--understanding when and how to prioritize getting gold, the game's in-game currency, is equally, or debatably more, important. Since your character becomes stronger by securing more and more gold throughout several segments of the game, having more gold than your opponent can be seen as key to maximizing your chances of winning. Although you passively gain gold and can easily earn a small amount of gold by killing small creatures known as minions, bigger objectives like drakes grant massive amount of golds that can completely shift the odds of winning a match. Each game also spawns in different types of unique drakes (e.g. Chemtech, Infernal, Mountain, etc.), and being able to slay the first drake at earlier stages of the game has the potential to drastically impact the odds of the match positively for that team from its gold and effects.

With this in mind, we want to focus on this central question: **"How impactful is prioritizing elemental drakes in terms of gold differences and win rates for a team?"**

### About the Dataset
The dataset in which we are working with is recorded professionally and thoroughly by Oracle's Elixir. In particular, we are focusing on data extracted from professional League of Legends matches that took place in 2025. Adding on, this dataset contains important information about statistics and results that can be used by players to understand ideal courses of action within their own games and lead others to strategically dominate against their opponents. Diving into a bit more about specific data collected from these matches, this includes features such as the differences in gold for teams at particular intervals, elemental drakes each team has slain, and results of each match.

Within the dataset offers a vast amount of matches, with there being 118932 rows containing information about those matches. Of the many columns that also help categorize all of the data, the following consists of the ones that were relevant to our central question and a brief description of each:

- `golddiffat10`: test
  
- `golddiffat15`: test
  
- `golddiffat20`: test
  
- `golddiffat25`: test
  
- `elementaldrakes`: test
  
- `opp_elementaldrakes`: test
  
- `infernals`: test
  
- `mountains`: test
  
- `clouds`: test
  
- `oceans`: test
  
- `chemtechs`: test
  
- `hextechs`: test
  
- `dragons (type unknown)`: test

- `result`: test

## Data Cleaning and Exploratory Data Analysis

## Assessment of Missingness

## Hypothesis Testing

## Framing a Prediction Problem

## Baseline Model

## Final Model

## Fairness Analysis
