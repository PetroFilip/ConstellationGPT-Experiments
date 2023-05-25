from neo4j import GraphDatabase

# NOTE Here I try to pull information by obtaining the subtrees of any document type recursively to generalize to any document


uri = "neo4j://amraelp00007371.pfizer.com:7687"
db_name = "constellation.graph.2022"
user = "neo4j"
password = "neo4jpoc"

driver = GraphDatabase.driver(uri, database=db_name, auth=(user, password))

# in constellation.graph.2022, each study has an SAP and PROTOCOL only, they connect to standards and other docs though
# constellation.grpah.2023 only has protocols loaded
DOCUMENT_LABELS = ["SAP", "PROTOCOL", "DATA_COLLECTION"]


def grab_study_nodes():
    pass


def get_subtree_recursive(study_id, session):
    query = (
        "MATCH (n:STUDY)\n"
        + f"WHERE n.name='{study_id}'"
        + """\n CALL apoc.path.expandConfig(n, {relationshipFilter: "", uniqueness: "NODE_GLOBAL", bfs:true, maxLevel: 9999}) YIELD path
        RETURN nodes(path), relationships(path) LIMIT 5000
    """
    )

    result = session.run(query)

    # for record in result:
    #     nodes = record["nodes(path)"]
    #     rels = record["relationships(path)"]
    #     print(nodes)
    #     print(rels)
    #     input()

    print(result.data())


if __name__ == "__main__":

    query = """
    MATCH (n:STUDY)-[:HAS_DATA_COLLECTION]->(crf:DATA_COLLECTION)
    , (n)-[:HAS_DOCUMENT]->(p:PROTOCOL)
    , (n)-[:HAS_DOCUMENT]->(sap:SAP)
    RETURN n, crf, p, sap
    """

    with driver.session() as session:
        get_subtree_recursive("C4591001", session)
        # result = session.run(query)

        # # Use a set to keep track of the nodes already seen
        # seen_nodes = set()

        # for record in result:
        #     # Check if the study node has been seen before
        #     if record["n"] in seen_nodes:
        #         continue

        #     # Print the nodes and add the study node to the set
        #     print(record["n"], record["crf"], record["p"], record["sap"])
        #     seen_nodes.add(record["n"])
        #     input()

        session.close()
        driver.close()
