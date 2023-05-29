from bertopic import BERTopic
from pull_graph_data_constellation_2023 import (
    driver,
    get_all_study_names,
    grab_all_doc_content_ordered,
    reconstruct_document,
)


topic_model = BERTopic(embedding_model="emilyalsentzer/Bio_ClinicalBERT")
# "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
# "emilyalsentzer/Bio_ClinicalBERT"

# topics, probs = topic_model.fit_transform(docs)
