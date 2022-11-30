### UMN EPSY 5122 Fall 2022
### Programming for Social Science Researchers
### Jeffrey K. Bye, Ph.D.

# Assignment 11: Due Tuesday, November 29, 2022 by 2:30pm

# NAME:

## Instructions
# For problems that require you to write code, write your code in the appropriate section below
# For problems that require you to provide a written response, write your answer as a comment (#)

# You should expect to make mistakes on this assignment. That is part of the learning process.
# Whenever you make a mistake, document the mistake AND what you learned from it in the section AT THE BOTTOM.

# As always, document any help you receive from online or friends.
# You must attempt each problem on your own first though! (Otherwise, you won't learn as well!)


# Problem 0
#
# If you've made it to this document, you likely already did Problem 0 from the readme. But just in case, here it is again!
#
# a) Let's watch some videos! I recommend all the videos in this series (for future learning), but we will just focus on two now. Watch the first half of this video (https://www.youtube.com/watch?v=_NrSWLQsDL4&list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV&index=3) -- just the part about forking, you can ignore pull requests! Then watch this video: https://www.youtube.com/watch?v=yXT1ElMEkW8&list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV&index=6 (you don't have to do the terminal git commands, you can use the clone strategy we used in class)
#
# b) Using what you learned in 0a, fork my GitHub repository (remote repo) to your own account, then clone to your hard drive (local repo) using GitKraken (or use the command-line if you want the extra challenge). After finishing EACH problem below, make sure to STAGE and COMMIT with a comment (e.g., "Just finished Part 1! Git is fun!" or whatever). Then PUSH back to GitHub.
# Note on privacy!
#
# By default, GitHub repos are public (promoting open source sharing of code), but of course you are more than welcome to make your code for this assignment private, as is your right! Unfortunately, it's a little bit complicated because GitKraken recently made a change that the free version of their software doesn't allow for private repo access, and you need the paid version. So here are 3 ways to do this privately:
#
# 1) GitKraken partners with GitHub to provide a free pack of resources (including the pro version of GitKraken) for students. That's you! So you can sign up here only if you want to do this: https://education.github.com/pack?utm_source=github+gitkraken
#
# 2) Just keep your GitHub repo public while you're working on this project. Use free GitKraken. Then switch the GitHub repo to Private only when you're done using GitKraken to push to GitHub.
#
# 3) Keep the repo private and use the terminal git commands in the YouTube video for Problem 0a.
#
# To make the repo private: On your GitHub repo, go to Settings > Manage Access > Manage (under Public Repository) > Change Visibility. Then add me (jkbye) as a 'collaborator' so I can see it: Settings > Manage Access > Invite a Collaborator (green button) > add 'jkbye'.
# Problem 1
#
# Now let's get to programming
#
# a) Import any helpful libraries

# b) Load the MA_Public_Schools_2017.csv file as a pandas data frame. Note: these data are from Kaggle: https://www.kaggle.com/ndalziel/massachusetts-public-schools-data and I have already removed a lot of columns.
#
# c) Adapt the example code in the chunk below to replace all spaces in column names with underscores. This is good practice in order to not cause problems with functions that don't allow spaces in variable names (e.g., smf.ols).
#
# d) Adapt the code from 1c to replace "%" sign with "Perc", because it is also good practice not to start column names with symbols.
#
# e) Find the descriptives for numeric columns.
#
# f) Commit your changes and push to GitHub!
#
# # Problem 1 code here (can split into multiple code chunks if you want)
#
# ​
#
# # starter code for 1c -- replace school_data w/ your dataframe name
#
school_data.columns = school_data.columns.str.replace(' ', '_') # notice this replaces the 1st argument w/ the 2nd
#
# Problem 2
#
# a) Remove the District Code column.
#
# b) Create a new column called "TOTAL_Enrollment" that is the sum of all columns that end in "Enrollment".
#
# c) Compute the mean of "TOTAL_Enrollment" for each District. (Hint: groupby)
#
# d) Commit your changes and push to GitHub!
#
# # Problem 2 code here (can split into multiple code chunks if you want)
#
# Problem 3
#
# a) Visualize each bivariate relationship among Average_Class_Size, Average_Salary, Perc_Economically_Disadvantaged, and Perc_English_Language_Learner. Use the Seaborn function pairplot. The argument to pairplot should be school_data[['Average_Class_Size', 'Average_Salary', 'Perc_Economically_Disadvantaged', 'Perc_English_Language_Learner']], which will just pull those columns out from the full data frame.
#
# b) Describe what you see from the plots.
#
# c) Based on your observations from 3b, and as a completely post-hoc, exploratory analysis, choose one of the 4 measures from 3a to be an outcome variable, and a second measure to be a predictor variable. Then run a linear regression, print the summary, and write a sentence interpreting the results (does not need to be detailed, just practice retrieving the relevant info on predictor significance, etc.)
#
# d) Commit your changes and push to GitHub!
#
# # Problem 3 code here (can split into multiple code chunks if you want)
#
# Problem 4
#
# a) Create a new linear regression model that takes the model from 3c and adds both of the remaining variables from 3a as additional predictor variables. To do this, the formula interface would look like "outcome_name ~ predictor1_name + predictor2_name + predictor3_name"
#
# b) Print the summary from 4a, and write a short interpretation of the results, especially comparing it to Problem 3c.
#
# c) Add School_Type as another predictor to your model. Interpret the new predictor in your output. How is it different from the other predictors?
#
# d) Commit your changes and push to GitHub!
#
# # Problem 4 code here (can split into multiple code chunks if you want)
#
# Problem 5
#
# a) Make sure this Python script is saved.
#
# b) Stage, commit, and push all changes to your GitHub repository.
#
# c) Submit a link to your repository as your submission for the assignment on Canvas. Remember the note from Problem 0: you can keep your repo private and add me as a collaborator.
