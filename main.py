from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from TopicModelling.pull_graph_data_constellation_2023 import (
    driver,
    get_all_study_names,
    grab_all_doc_content_ordered,
    reconstruct_document,
)
import numpy as np

# create graphdb session
session = driver.session()

# instantiate topic model
topic_model = BERTopic()

# instantiate sentence model for producing the embeddings
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
# "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
# "emilyalsentzer/Bio_ClinicalBERT"


def mean_pooling(sent_embeddings):
    """To combine sentence embeddings into a single document embedding"""
    # Calculate the mean along the sequence length axis
    doc_embedding = np.mean(sent_embeddings, axis=0)
    return doc_embedding


# query graph for document data
study_ids = get_all_study_names(session)[:3]

docs = []  # holds reconstructed protocols for each study has strings
doc_embeddings = []  # holds a single document embedding that representes entire doc
for study_id in study_ids:
    # gather document chunks from graph
    doc_chunks = grab_all_doc_content_ordered(study_id, session)

    # embedd each chunk of the document
    chunk_embeddings = sentence_model.encode(doc_chunks, show_progress_bar=True)

    # mean pool them down into a single doc embedding
    doc_embedding = mean_pooling(chunk_embeddings)
    doc_embeddings.append(doc_embedding)

    # build entire document into single string
    reconstructed_doc = reconstruct_document(doc_chunks)
    # print(reconstructed_doc)
    docs.append(reconstructed_doc)


# perform topic modeling using the embeddings
topics, probs = topic_model.fit_transform(docs, doc_embeddings)
# print(topics, probs)

df = topic_model.get_topic_info()
print(df)

# Write DataFrame to a CSV file
df.to_csv("topics.csv", index=False)


# close graphdb session at end
session.close()
driver.close()
