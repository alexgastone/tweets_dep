# Project Goal

With COVID-19 intensifying around the world, so have levels of anxiety and depression. A recent study has linked rising stress and depression levels in the US to the pandemic, specifically to COVID-related losses and media consumption (University of California, Irvine - *Science Advances*). 

Given that depression is usually self-assessed, in the way that you yourself have to decide whether or not to seek treatment, how can data insights help those that are, especially now, struggling with this self-awareness step?

This is where text analysis comes in: performing a linguistic analysis with advanced NLP tools (which are areguably getting more and more advanced by the month at this point) on social media posts to detect whether its users may be prone to depression-like thoughts and sentiments. We can train a model to do a simple binary classification task with the text data, and create a web app for real time inference of user-provided tweets. 

The project is not, however, meant to be a strict self-assessment tool; the key is to **explain** the given prediction in order for the user to understand and eventually possibly act on the results, or seek help if needed. A non-interpretable solution, in this case, would be useless. In order to do so, the goal of this project will be to use the trained model combined with calculated LIME values, which will provide how much each word in the specified text contributed to the text's predicted classification.

# Data

In terms of which social media channel to choose, twitter provides enough anonymity for users to more freely express themselves. 

The biggest obstacle to the project is coming up with a  ground truth dataset. Since we don't have any labeled users (label = depression risk / no depression risk), and I haven't found any available datasets online, we'll have to come up with our own. 

To note that this is different from a sentiment analysis task. There are datasets available for sentiment analysis (one if which I used in another project with Kaggle), but none for depression analysis.

We can extract Tweets with a given set of filters (ex. selecting for specific keywords such as 'depression', 'helpless', etc...) to make sure we capture relevant tweets in building our dataset. Then we would manually label them. Having a degree a Psychology and being intimately familiar with the mood disorder, I feel confident in the labels assigned; a better option would nevertheless be having a second judge label the dataset and resolve disagreements with discussion.

# Model
BERT Transformer model for word embeddings, followed by a Dense activation layer for binary classification. Can try other variations of the BERT model (RoBERTa, DistilBERT, ALBERT... all available through HuggingFace) and hyperparameter tuning with Keras.


# Web App
After model training, the web app can be easily set up with Streamlit, with simple visualizations for model inferences and LIME values with user-provided text. Eventually could dockerize and deploy the app on the cloud.