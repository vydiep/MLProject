# CSCI0451 Project: Classical Music Classification 

## Abstract
In this project, we will work to identify a composer of classical music. More specifically, we will identify whether a piece of classical music is Beethoven or not. In order to accomplish this, we will be using a data set with audio files of songs from different composers and metadata about those songs. Through strategic feature selection and potentially deep learning, we hope to yield successful results, in that our model is able to correctly classify whether a piece of music is Beethoven's at least 80-85% of the time given that there's a labeling error rate of 4% in our data set. 

## Motivation and Question
We are both avid music listeners, who sometimes hear songs we are unfamiliar with, but want to quickly identify. To begin to address this minute, but everyday problem we encounter, we found a data set focused on classical music. We felt that this data set would allow us to start picking at this larger problem with our current computing power and machine learning skills. This data set has WAV files of classical music by 10 different composers, almost half of which is Beethoven. This data set also has metedata about each audio file, including the composer, composition, and ensemble. Each WAV file also has a CSV file with information about which note, instrument, and more are being played at specific times in the song using dynamic time warping. By training a model on this data set, we hope to classify whether a piece of music is Beethoven or not. Ultimately, this is related to this larger problem of identifying unknown music that we do not have the resources to solve yet. 

## Planned Deliverables
For our deliverables, we aim to have a Python package containing all code used for algorithms and analysis, including documentation. We will also have at least one Jupyter Notebook illustrating the use of the package to analyze data. Lastly, we will have written deliverables in the form of a blog post on our project. We will evaluate our deliverables based on the following criteria:

- Full Success: 
    - A model that can identify whether a piece of classical music is composed by Beethoven or not about 80-85% of the time
    - Jupyter Notebook that demonstrates our understanding and results

- Partial Success:
    - A model that does not correctly classify whether a piece of classical music is composed by Beethoven
    - Jupyter Notebook that explains our process and what we tried to achieve

## Resources Required
In order to complete this project, we will need data set(s) with audio files of classical music by Beethoven and other composers. A data set we plan on using was found on Kaggle called [MusicNet Dataset](https://www.kaggle.com/datasets/imsparsh/musicnet-dataset). To assist us in using this dataset, we also found a [website by Jong Wook Kim](https://musicnet-inspector.github.io/) dedicated to inspecting this data and a [PyTorch interface for accessing the MusicNet dataset](https://github.com/jthickstun/pytorch_musicnet) available on GitHub. 

## What We Will Learn
Katie: Throughout this project, we will be experimenting with different machine learning models. By doing so, I hope that I will learn more about the limitations of different models and be better at communicating their results. By working collaboratively with my partner, I hope to also improve my communication skills and learn more about how to be an effective teammate. 

Vy: Similar to what Katie said, a large portion of our project will be experimenting with different machine learning models. I hope to use the knowledge learned from those experimentations, as well as the skills I've gained through class lectures and the blog posts we've done, to become better at implementing efficient machine learning model. I would also like to use this opportunity to further improve my communication and time management skills.

## Risk Statement
Working with audio files that map to metadata comes with risks that could potentially hold us back from achieving the full deliverable above. It might take longer to train a model using audio files. We also may encounter new and more challenging bugs related to mapping the files to the metadata or extracting features from the audio. With neither of us having worked with audio files in this way before, it may be a challenge to preprocess the files in an efficient and effective way. 
Since our data set is fairly small, we intend to research more on music theory to better understand patterns we can use as features to identify Beethoven's music. However, we are not sure whether it's plausible for us to extract these features from WAV files and might have to rely on using a deep learning model, which might result in overfitting. 

## Ethics Statement
We believe our project could potentially benefit music theory researchers, classical music listeners, and people who want to get into classical music. Our project can help these listeners differentiate Beethoven, one of the greatest and most influential composers of Western classical music, from other composers. It can provide the research community with more information on patterns in Beethoven's music. We would like to acknowledge that our project excludes other composers, or more specifically non-Western composers.

We believe the our project could make the world a slightly better place, under the assumptions that ...  
1. There are specific patterns in Beethoven's music 
2. The world is a better place when people are more educated about classical music

## Tentative Timeline
After three weeks of working on this project, we hope to have multiple machine learning models trained on our data with some exploratory analysis. By week six of working on this project, we hope to have found and trained a model with our desired results of 80-85% accuracy, cleaned up our code, synthesized our analysis, and completed all required deliverables. 

Below is an overview of our tentative timeline ... 
- Around 4/10 
  - Classical music feature research complete
  - Potential model research complete 
  - More comfortable using data set in code
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