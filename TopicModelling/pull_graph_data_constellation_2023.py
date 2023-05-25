from neo4j import GraphDatabase

uri = "neo4j://amraelp00007371.pfizer.com:7687"
db_name = "constellation.graph.2022"
user = "neo4j"
password = "neo4jpoc"


if __name__ == "__main__":

    query = """
    MATCH (n:STUDY)-[:HAS_DATA_COLLECTION]->(crf:DATA_COLLECTION)
    , (n)-[:HAS_DOCUMENT]->(p:PROTOCOL)
    , (n)-[:HAS_DOCUMENT]->(sap:SAP)
    RETURN n, crf, p, sap
    """

    with driver.session() as session:
        result = session.run(query)

        # Use a set to keep track of the nodes already seen
        seen_nodes = set()

        for record in result:
            # Check if the study node has been seen before
            if record["n"] in seen_nodes:
                continue

            # Print the nodes and add the study node to the set
            print(record["n"], record["crf"], record["p"], record["sap"])
            seen_nodes.add(record["n"])
            input()

        session.close()
        driver.close()
