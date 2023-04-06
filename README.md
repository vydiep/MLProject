# CSCI0451 Project: Classical Music Classification 

## Abstract
In this project, we will work to identify a composer of classical music. More specifically, we will identify whether a piece of classical music is Beethoven or not. In order to accomplish this, we will be using a dataset with audio files of songs from different composers and metadata about those songs. Through strategic feature selection based on knowledge about patterns in classical music, we hope to yield successful results, in that our model is able to correctly classify whether a piece of music is Beethoven's at least 90% of the time. 

## Motivation and Question
We are both avid music listeners, who sometimes hear songs we are unfamiliar with, but want to quickly identify. To begin to address this minute, but everyday problem we encounter, we found a dataset focused on classical music. We felt that this dataset would allow us to start picking at this larger problem with our current computing power and machine learning skills. This dataset has wav files of classical music by 10 different composers, almost half of which is Beethoven. This dataset also has metedata about each audio file, including the composer, composition, and ensemble. Each wav file also has a csv file with information about which note, instrument, and more are being played at specific times in the song using dynamic time warping. By training a model on this dataset, we hope to classify whether a piece of music is Beethoven or not. Ultimately, this is related to this larger problem of identifying unknown music that we do not have the resources to solve yet. 

## Planned Deliverables
For our deliverables, we aim to have a Python package containing all code used for algorithms and analysis, including documentation. We will also have at least one Jupyter Notebook illustrating the use of the package to analyze data. Lastly, we will have written deliverables in the form of a blog post on our project. We will evaluate our deliverables based on the following criteria:

- Full Success: 
    - A model that can identify whether a piece of classical music is composed by Beethoven or not
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
Working with audio files that map to metadata comes with risks that could potentially hold us back from achieving the full deliverable above. It might take longer to train a model using audio files. We also may encounter new and more challenging bugs related to mapping the files to the metadata or extracting defining features from the audio. With neither of us having worked with audio files in this way before, it may be a challenge to preprocess the files in an efficient and effective way. Since audio files are more simplified than MP3 files, there may be features in our music that we'd want to explore, but don't have the quality files to do so. With the additional online resources we found that aims to make this MusicNet dataset more accessible, we hope that we will be able to overcome these risks. 

## Ethics Statement
We believe our project could potentially benefit classical music listeners and/or people who want to get into classical music because it will help them be able to differentiate Beethoven, one of the greatest and most influential composers of Western classical music, from other composers. We would like to acknowledge that our project may exclude people with hearing disabilities since we are working with audio files. 

Will the world become an overall better place because we made our project? Maybe. Under the assumptions that:

1. A piece of music can be classified by composers based on features like tempo and rhythm, and 
2. Most people don't truly know what makes music by Beethoven special,

our project may help people become more knowledgable about composers and make them appreciative of classical music.

## Tentative Timeline
After three weeks of working on this project, we hope to have multiple machine learning models trained on our data with some exploratory analysis. By week six of working on this project, we hope to have found and trained a model with our desired results of 90% accuracy, cleaned up our code, synthesized our analysis, and completed all required deliverables. 

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