# The data we need to retrieve
#1. The total number of votes
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. the total number of vote each candidate won
#5. the winnder of the election based on popular vote
import csv

import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote couter
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes = total_votes + 1

    # Print the candidate name from each row
        candidate_name = row[2]

    # If the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            # Add candidate name to list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote cout
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate through the counts

    # Iterate throught the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of the votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidates name, vote count and percentage of votes to terminal

        # Determine winning vore count and candidate

        # Determine if the votes is greater that the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winnig_count = votes and winning_percent = vote+percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set teh winning_candidate to the candidate's name
            winning_candidate = candidate_name

    # To do: print out the winning candidate, vote count, and vote percentage to termial

        # Print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
 




    