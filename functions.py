from neo4j import GraphDatabase, basic_auth

uri = "neo4j+s://3edb56e6.databases.neo4j.io"
user = "neo4j"
password = "DMtRKJnPD_xuKfQcStxuBzKg-6vUJiZ9l53yxM2P9I4"
driver = GraphDatabase.driver(uri, auth=(user, password))


def get_people():
    query = "MATCH (p:Person) RETURN (p)"
    with driver.session() as session:
        return session.run(query).data()


def add_new_person(born, name):
    query = "CREATE (p:Person {born: '" + born + "', name: '" + name + "'})"
    if not find_a_person(name):
        with driver.session() as session:
            return session.run(query).data()
    else:
        return False


def delete_one_person(name):
    query = "MATCH (p:Person {name: '" + name + "'}) DETACH DELETE p"
    with driver.session() as session:
        return session.run(query).data()


def find_a_person(name):
    query = 'MATCH (p:Person {name: "' + name + '"}) RETURN p'
    with driver.session() as session:
        return session.run(query).data()


def get_actor_movies(name):
    query = 'OPTIONAL MATCH (p:Person {name:"' + name + '"})-[r:ACTED_IN]-(m:Movie) RETURN m'
    with driver.session() as session:
        return session.run(query).data()


def add_new_movie(tagline, title, released):
    query = "CREATE (m:Movie {tagline: '" + tagline + "', title: '" + title + "', released: '" + released + "'})"
    if not find_a_movie(title):
        with driver.session() as session:
            return session.run(query).data()
    else:
        return False


def get_movies():
    query = "MATCH (m:Movie) RETURN m"
    with driver.session() as session:
        return session.run(query).data()


def delete_one_movie(title):
    query = "MATCH (m:Movie {title: '" + title + "'}) DETACH DELETE m"
    with driver.session() as session:
        return session.run(query).data()


def find_a_movie(title):
    query = 'MATCH (m:Movie {title: "' + title + '"}) RETURN m'
    with driver.session() as session:
        return session.run(query).data()


def get_actors(title):
    query = 'OPTIONAL MATCH (m:Movie {title:"' + title + '"})-[r:ACTED_IN]-(p:Person) RETURN p'
    with driver.session() as session:
        return session.run(query).data()


def get_directors(title):
    query = 'OPTIONAL MATCH (m:Movie {title:"' + title + '"})-[r:DIRECTED]-(p:Person) RETURN p'
    with driver.session() as session:
        return session.run(query).data()


def add_actor_to_movie(name, title):
    query = "MATCH (m:Movie {title: '" + title + "'}),(p:Person {name: '" + name + "'}) MERGE(m)-[r:ACTED_IN]->(p) " \
                                                                                   "RETURN m,p "
    with driver.session() as session:
        return session.run(query).data()
