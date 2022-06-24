# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total nubmer of votes each candidate won.
4. Determine the winner of the election base on popular vote.

## Resources
*Data Source: election_results.csv
*Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% if the vote and 11,606 votes
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes

## (Challenge) Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks in addition to the previous project to complete the election audit of a local congressional election.

1. Get a complete list of the counties in the election.
2. Calculate the total number of votes that were counted in each county.
3. Determine the county with the largest voter turnout.

## (Challenge) Election-Audit Results
- There were 369,711 votes cast in the election.
- The counties in the election were:
  - Arapahoe
  - Denver
  - Jefferson
- The results in each county were:
  - Arapahoe: 6.7% of voter turnout with 24,801 votes
  - Denver: 82.8% of voter turnout with 306,005 votes
  - Jefferson: 10.5% of voter turnout with 38,855 votes
- The county with the largest turnout was:
  - Denver: 82.8% of voter turnout with 306,005 votes
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23% of the vote and 85,213 votes
  - Diana DeGette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% if the vote and 11,606 votes
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes

## (Challenge) Election Audit Summary
The code used to calculate the election results provided for analysis is also mutable and can be adjusted to fit other data. On way that the code can be altered to fit alternative data, for example election data for the entire country, is to edit the for loop which counts the votes in each county and returns the percentage vote in that county and the total votes recorded,
```
for county_name in county_votes:
  cvotes = county_votes.get(county_name)
  cvote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
```
can be edited to count states instead. Similarly, if the data were to include the party of the candidate a for loop similar to the one which counts the votes for individual candidates could be created to instead count the votes and percentages that went to each recorded party, i.e. Democrat, Republican, Independent, etc.
