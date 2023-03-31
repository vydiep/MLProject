# MLProject

2 Write Your Project Proposal

Write your project proposal in your project repository. For now, you can just use the file README.md to hold your proposal; this has the benefit that GitHub.com will automatically render it for you. Specs for your proposal are below. Here’s what I’m looking for from your proposal:

Expected Sections
You should include sections in your proposal that address the following topics. Feel free to include additional sections as needed. Remember that you can create Markdown sections using the # character.

Abstract
In 3-4 sentences, concisely describe:

What problem your project addresses.
The overall approach you will use to solve the problem.
How you propose to evaluate your success against your stated goals.

Motivation and Question
Describe your motivation for your project idea. Some (shortened) examples of good types of motivations:

We have a scientific data set for which predictive or expoloratory models would help us generate hypotheses.
We have user information for which predictive models would help us give users better experiences.
We have performance data (e.g. from sports teams) for which predictive models could help us make better decisions.
Algorithmic bias is an increasingly urgent challenge as machine learning products proliferate, and we want to explore it more deeply.
You should be more specific than these: describe your specific data set (if applicable); your scientific questions; the type of decisions your model could inform; etc.

Planned Deliverables
Concisely state what you are aiming to create and what capabilities it will have. For most projects, I would expect the deliverable to include:

A Python package containing all code used for algorithms and analysis, including documentation.
At least one Jupyter notebook illustrating the use of the package to analyze data.
However, your specific idea might imply different deliverables (e.g. an essay). Consult with me if you’re not sure.

You should describe what your deliverable will be able to do and how you will evaluate its effectiveness. Please consider two scenarios:

“Full success.” What will your deliverable be if everything works out for you exactly as you plan?
“Partial success.” What useful deliverable will you be able to offer even if things don’t 100% work out? For example, maybe you aren’t able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan!

Written Deliverables
You’ll also write a blog post on your project; you don’t have to discuss this post in your proposal though.

Resources Required
What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

Please pay special attention to the question of data. If your project idea involves data, include at least one link to a data set you can use. If you can’t find data for your original idea, that’s ok! Think of something related to your group’s interests for which you can find data.

Most projects should involve data in some way, but certain projects may not require data. Ask me if you’re not sure.

What You Will Learn
Each group member should return to their stated goals from the reflective goal-setting assignment at the beginning of the course. Then, in this section, please state what each group member intends to learn through working on the project, relating your intentions to your stated goals. You might be thinking of certain algorithms, software packages, version control, project management, effective teamwork, etc.

Risk Statement
What are two things that could potentially stop you from achieving the full deliverable above? Maybe it turns out that the pattern you thought would be present in the data just doesn’t exist? Or maybe your idea requires more computational power than is available to you? What particular risks might be applicable for your project?

Ethics Statement
All projects we undertake involve decisions about whose interests matter; which problems are important; and which tradeoffs are considered acceptable. Take some time to reflect on the potential impacts of your project on its prospective users and the broader world. Address the following questions:

What groups of people have the potential to benefit from our project?
What groups of people have the potential to be excluded from benefit or even harmed from our project?
Will the world become an overall better place because we made our project? Describe at least 2 assumptions behind your answer. For example, if your project aims to make it easier to predict crime, your assumptions might include:
Criminal activity is predictable based on other features of a person or location.
The world is a better place when police are able to perform their roles more efficiently.

If your project involves making decisions or recommendations, then you will also need to consider possible forms of algorithmic bias in your work. Here are some relevant examples:

A recipe recommendation app can privilege the cuisines of some locales over others. Will your user search recipes by ingredients? Peanut butter and tomato might seem an odd combination in the context of European cuisine, but is common in many traditional dishes of the African diaspora. A similar set of questions applies to recommendation systems related to style or beauty.
A sentiment analyzer must be trained on specific languages. What languages will be included? Will diverse dialects be included, or only the “standard” version of the target language? Who would be excluded by such a choice, and how will you communicate about your limitations?

Tentative Timeline
We will have a checkpoint for the project in Week 9 or 10, and then final presentations in Week 12. With this in mind, please describe what you expect to achieve after three and six. Your goal by the three-week check-in should be to have “something that works.” For example, maybe in three weeks you’ll ready to demonstrate the data acquisition pipeline and show some exploratory analysis, and in the last couple weeks you’ll actually implement your machine learning models.

Your proposal is acceptably complete if if:

The proposal is hosted on GitHub as the top-level README.md file in a repository hosted by one of the group members.
Each team member has made at least two commits to this file, which in total demonstrate substantial commitments to the writing of the proposal.
The proposal contains thoughtful discussion in each of the required sections, which addresses all of the relevant questions posed in each one.
The proposal is written in clear English prose. Within reason, grammatical mistakes are not a problem.
You have submitted a URL to your GitHub repository on Canvas.

Length
There is no specifically required length for the proposal. Generally speaking, I would expect a thoughtful proposal to require around 600-900 words (roughly the length of 2-3 double-spaced pages). However, any length is acceptable provided that it provides thoughtful discussion of each of the required components.

4 Optional Practice: Collaborative Workflows in Git

Your proposal should be written on GitHub and contain commits by multiple team members. This is the same workflow that you’ll use for collaborating on your project itself. If members of your team are not familiar with collaborative workflows in Git and GitHub, then you should complete this activity with your team in order to get up to speed.

Working through this mini activity with your group is optional but strongly recommended.

Make a Grid
It’s possible that your repository already has a top-level file named README.md. If not, a new group member (not the one who created the repo) should create one. Then, this group member should create a code block in the file README.md containing a 3x3 grid of dots, like the below:

. . . 
. . .
. . .
Save, commit, and push. All other group members should now pull, so that they have the grid of dots as well.

Play Tic-Tac-Toe
If you have more than two people, separate into two teams – it’s ok if they are not the same size. Play a few games of Tic-Tac-Toe by replacing the dots in the grid you made with the symbol X or O. Here’s how to make a move:

A member of Team X deletes a dot and replaces it with an X.
This member commits and pushes their change.
All other team members pull, so that the move is reflected in their file.
A member of Team O deletes a dot and replaces it with an O…
By playing some Tic-Tac-Toe, you practice the fundamental pull-commit-push workflow of collaboration. Make sure that every group member gets a chance to make a move, commit their move, and push at least twice.

Merging
Create a new, blank Tic-Tac-Toe game. Imagine that Team X and Team O miscommunicated about who would go first, so they both make moves simultaneously. Test out the following scenarios.

Scenario 1:

Team X makes the following move:

. . . 
. . .
. X .
Team O makes the following move:

. O . 
. . .
. . .
Both teams should now attempt to commit and push. One team will be prompted to pull prior to pushing. This pull will prompt a merge, since two changes were made to the same file. Observe what happens, commit, and then push. Pull as needed so that both teams have both moves in their file.

Scenario 2:

Team X makes the following move:

. . . 
. X .
. . .
Team O makes the following move:

. . . 
. O .
. . .
The current representative of each team should commit these respective moves, and attempt to push.

Whoops! One team will be prompted to pull, and after pulling will be informed that there is a merge conflict in the repository. Inspect the file. Notice that the relevant part of the file now looks very weird. If you look closely, you can find lines corresponding both to the X move and to the O move. Pick one (arbitrarily), and commit/push the result.

This is an example of the process used to handle merge conflicts, which occur when separate team members have modified the same file in conflicting ways.

It’s recommended, but not required, that your team members take some time on their own to do a little reading on how merge conflicts work. This page gives a good explanation, and also covers the (optional but highly useful) topic of branching.
