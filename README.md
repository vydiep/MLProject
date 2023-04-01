# CSCI0451 Project: Classical Music Classification 

## Abstract
In this project, we will work to identify a composer of classical music. More specifically, we will identify whether a piece of classical music is Beethoven or not. In order to accomplish this, we will be using a dataset with MIDI files of songs from different composers and metadata about those songs. Through strategic feature selection based on knowledge about patterns in classical music, we hope to yield successful results, in that our model is able to correctly classify whether a piece of music is Beethoven's at least 95% of the time. 

## Motivation and Question
We are both avid music listeners, who sometimes hear songs we are unfamiliar with, but want to quickly identify. To begin to address this minute, but everyday problem we encounter, we found a small dataset focused on classical music, which we felt would allow us to start picking at this larger problem with our current computing power and machine learning skills. This dataset has MIDI files of classical music by different composers, almost half of which is Beethoven. This dataset also has metedata about each MIDI file, including the composer, composition, and ensemble. By training a model on this dataset, we hope to classify whether a piece of music is Beethoven or not. Ultimately, this is related to this larger problem of identifying unknown music that we do not have the resources to solve yet. 

## Planned Deliverables
Concisely state what you are aiming to create and what capabilities it will have. For most projects, I would expect the deliverable to include:

A Python package containing all code used for algorithms and analysis, including documentation.
At least one Jupyter notebook illustrating the use of the package to analyze data.
However, your specific idea might imply different deliverables (e.g. an essay). Consult with me if you’re not sure.

You should describe what your deliverable will be able to do and how you will evaluate its effectiveness. Please consider two scenarios:

“Full success.” What will your deliverable be if everything works out for you exactly as you plan?
“Partial success.” What useful deliverable will you be able to offer even if things don’t 100% work out? For example, maybe you aren’t able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan!

## Written Deliverables
You’ll also write a blog post on your project; you don’t have to discuss this post in your proposal though.

## Resources Required
What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

Please pay special attention to the question of data. If your project idea involves data, include at least one link to a data set you can use. If you can’t find data for your original idea, that’s ok! Think of something related to your group’s interests for which you can find data.

Most projects should involve data in some way, but certain projects may not require data. Ask me if you’re not sure.

## What We Will Learn
Each group member should return to their stated goals from the reflective goal-setting assignment at the beginning of the course. Then, in this section, please state what each group member intends to learn through working on the project, relating your intentions to your stated goals. You might be thinking of certain algorithms, software packages, version control, project management, effective teamwork, etc.

Katie: 

## Risk Statement
Working with MIDI files and using files that map to metadata comes with risks that could potentially hold us back from achieving the full deliverable above. It might take longer to train a model using MIDI files. We also may encounter new and more challenging bugs related to mapping the files to the metadata or extracting defining features from the audio that may take longer to address. 

## Ethics Statement
All projects we undertake involve decisions about whose interests matter; which problems are important; and which tradeoffs are considered acceptable. Take some time to reflect on the potential impacts of your project on its prospective users and the broader world. Address the following questions:

- What groups of people have the potential to benefit from our project?
- What groups of people have the potential to be excluded from benefit or even harmed from our project?
- Will the world become an overall better place because we made our project? Describe at least 2 assumptions behind your answer. 

For example, if your project aims to make it easier to predict crime, your assumptions might include:
Criminal activity is predictable based on other features of a person or location.
The world is a better place when police are able to perform their roles more efficiently.

If your project involves making decisions or recommendations, then you will also need to consider possible forms of algorithmic bias in your work. Here are some relevant examples:

A recipe recommendation app can privilege the cuisines of some locales over others. Will your user search recipes by ingredients? Peanut butter and tomato might seem an odd combination in the context of European cuisine, but is common in many traditional dishes of the African diaspora. A similar set of questions applies to recommendation systems related to style or beauty.
A sentiment analyzer must be trained on specific languages. What languages will be included? Will diverse dialects be included, or only the “standard” version of the target language? Who would be excluded by such a choice, and how will you communicate about your limitations?

## Tentative Timeline
After three weeks of working on this project, we hope to have multiple machine learning models trained on our data with some exploratory analysis. By week six of working on this project, we hope to have found and trained a model with our desired results of 95% accuracy, cleaned up our code, synthesized our analysis, and completed all required deliverables. 

Below is an overview of our tentative timeline ... 
- Around 4/10 
  - Classical music feature research complete
  - Potential model research complete 
- Around 4/17 
  - Features selected based on feature research 
  - Multiple models selected and trained 
  - Rough draft of exploratory analysis in shared jupyter notebook
- Around 4/27 
  - Most successful model chosen 
  - Cleaned up Python training code 
  - Started creating final presentation 
- Around 5/8 
  - Model chosen and fully trained with desired performance 
  - Deliverables finalized 