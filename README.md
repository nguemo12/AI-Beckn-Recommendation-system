# HOSPITALITY AI-ST


The approach we're taking here is straightforward: given the absence of user data, we'll base our recommendations on the descriptions provided. 

For example, if a user asks: 

- "Recommend me an affordable hotel in Colombes." 

- We would recommend "ADAGIO Colombes." 


To achieve this, we'll rely on the 'text' column containing the address, description, and contact information of each location. If a description mentions, for instance, that hotel X is very affordable and located in Colombes, then it's this hotel X, with a description matching the user's query, that will be recommended. 

Our approach is built upon an architecture integrating transformers and vector databases. This architecture will enable us to analyze location descriptions and compare them to user queries to provide relevant recommendations. 

## Setup:
```bash
git clone https://github.com/nguemo12/AI-Beckn-Recommendation-system/tree/annoy_rec
cd AI-Beckn-Recommendation-system-annoy_rec
```

After this we need to install all the dependency
```bash
pip install -r requirements.txt
```

`annoy_index.ann` and `emebedding_data.npy` represent respectively the vectorizer database and the embdeding database of the dataset use (in our case it was place/hotels/restaurant)


 
## 2.1. Architecture: 

 

HOSPITALITY AI -ST comprises a Transformers component used to compute embeddings for each text word contained in the dataset. We use the 'SentenceTransformer' as our transformer model, which is pre-trained on nearly 100 different languages and is based on a BERT model. Sentence Transformers is a Siamese neural model of transformers working together and at the end performs a similarity cosine to obtain efficient results. 


However, we use DistilBert to enhance speed. 

The embeddings are then stored in a vector database. A vector database is a database used to store high-dimensional vectors, allowing data searches based on their similarity. For our vector database, we use Annoy developed by Spotify, which enables data searches based on nearest neighbors, similar to KNN and KMeans. 

In this use case, the user enters a prompt, which is converted into a vector representation. This vector representation is then sent to the vector database to search for embeddings close to the user's prompt. The database returns the indices, and based on these indices, we query the Île-de-France database to retrieve the corresponding locations. 

 

## 2.2. Training: 

We begin by loading the SentenceTransformers model, which will be used to compute embeddings for our dataset. We utilize 'cuda' for computation, although the model can be used on a CPU without any issues, albeit with slightly longer processing times. 

With 'cuda', it takes around 0.81 minutes to compute the embeddings for 6040 observations. 

After computing the embeddings for each row of the 'text' column, we initialize the vector database with a size equal to the output dimension of the embeddings. For SentenceTransformers, the output dimension is 512.  

We create the vector database and instantiate 10 trees to efficiently process the data. This operation takes only a few seconds. 

This process ensures that we have the embeddings of our dataset ready for further processing, enabling us to efficiently retrieve similar embeddings based on user queries, as described earlier. 

### 2.3. Inference:

Check the `Preparation.ipynb` to understand how to use the model

| Metric   | Value                  |
|----------|------------------------|
| Time elapsed | 0.906 min           |
| Precision    | 0.9963582188379407  |
| Recall       | 0.9963582188379407  |
| Accuracy     | 0.9963582188379407  |


Thanks!
