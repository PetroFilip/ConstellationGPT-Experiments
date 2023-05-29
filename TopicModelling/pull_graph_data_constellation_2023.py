from neo4j import GraphDatabase


# instantiate graph db connection
uri = "neo4j://amraelp00007371.pfizer.com:7687"
db_name = "constellation.graph.2023"
user = "neo4j"
password = "neo4jpoc"
driver = GraphDatabase.driver(uri, database=db_name, auth=(user, password))


def get_all_study_names(session):
    # gets all study IDs present in db
    query = f"""MATCH (study:STUDY) RETURN labels(study)"""
    result = session.run(query)

    study_ids = []
    for record in result:
        labels = record["labels(study)"]
        labels.remove("STUDY")
        study_ids.append(labels[0])

    return study_ids


def grab_all_doc_content_ordered(study_id, session):
    # grabs all the document_content nodes under the protocol and orders them by the node ids (assuming they were loaded into the graph in order,
    #   node ids may have preserved the top-down order of the original document)
    # returns a list of strings, each string being text property from each node ordered by their IDs
    query = f"""MATCH (doc_content:{study_id}:PROTOCOL:SECTION_CONTENT) RETURN doc_content ORDER BY doc_content.id"""
    result = session.run(query)

    return [i["doc_content"]["text_content"] for i in result.data()]


def reconstruct_document(docs_list):
    # appends all the string given into one string, representative of "document"
    # assumes the chunks are in order
    doc = ""
    for chunk in docs_list:
        doc += chunk

    return doc


def show_chunk_length_statistics(session):
    study_ids = get_all_study_names(session)
    # print(study_ids)

    total_across_studies = 0
    for study_id in study_ids:
        chunks = grab_all_doc_content_ordered(study_id, session)

        total_length = 0
        above_500 = 0
        above_1000 = 0
        for i in chunks:
            length = len(i)
            total_length += length

            if length > 500:
                above_500 += 1

            if length > 1000:
                above_1000 += 1

        avg_length = total_length / len(chunks)
        total_across_studies += avg_length

        msg = f"""
        ----------------------------
        Study ID: {study_id}
        Average Chunk Length (characters): {int(avg_length)}
        Number of Documents with over 500 characters: {above_500}
        Number of Documents with over 1000 characters: {above_1000}
        Total Chunks: {len(chunks)}
        ----------------------------
        """
        print(msg)

    avg_across_studies = int(total_across_studies / len(study_ids))
    print(f"Average Chunk Length Across all studies (characters): {avg_across_studies}")


if __name__ == "__main__":

    with driver.session() as session:
        # show_chunk_length_statistics(session)

        study_ids = get_all_study_names(session)[:3]

        docs = []  # holds reconstructed protocols for each study has strings
        for study_id in study_ids:
            doc_chunks = grab_all_doc_content_ordered(study_id, session)

            reconstructed_doc = reconstruct_document(doc_chunks)
            # print(reconstructed_doc)

            docs.append(reconstructed_doc)

        session.close()
        driver.close()
