from bertopic import BERTopic
from pull_graph_data_constellation_2023 import (
    driver,
    get_all_study_names,
    grab_all_doc_content_ordered,
)

# create graphdb session
session = driver.session()

topic_model = BERTopic(embedding_model="emilyalsentzer/Bio_ClinicalBERT")
# "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
# "emilyalsentzer/Bio_ClinicalBERT"

# topics, probs = topic_model.fit_transform(docs)

# query graph for document data
study_ids = get_all_study_names(session)[:3]

docs = []  # holds reconstructed protocols for each study has strings
for study_id in study_ids:
    # gather document chunks from graph
    doc_chunks = grab_all_doc_content_ordered(study_id, session)
    docs.extend(doc_chunks)


topics, probs = topic_model.fit_transform(docs)

df = topic_model.get_topic_info()
print(df)

# Write DataFrame to a CSV file
df.to_csv("topics.csv", index=False)


# close graphdb session at end
session.close()
driver.close()
