import rdflib
import pandas as pd
import random
from datetime import datetime, timedelta
import yaml


# Load Configuration
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

#KG_path = config["KG_output_path"]
KG_train = config["KG_train_path"]
KG_val = config["KG_val_path"]

ontology_format = config["ontology_format"]
inst_prefix = config["instance_prefix"]


# Load KG
def load_graph(kg: str):
    import rdflib

    graph = rdflib.Graph()

    if kg == "train":
        graph.parse(KG_train, format=ontology_format)
    elif kg == "val":
        graph.parse(KG_val, format=ontology_format)
    else:
        raise ValueError("kg argument must be 'train' or 'val'")

    return graph

##########################################################################################
###############################  AGNOSTIC DATASET GENERATOR ################################

def list_all_individuals_with_prefix(kg: str) -> list:
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    SELECT DISTINCT ?s
    WHERE {
        ?s rdf:type ?class .
        
        FILTER(?class != owl:Class &&
               ?class != owl:ObjectProperty &&
               ?class != owl:DatatypeProperty &&
               ?class != rdf:Property &&
               ?class != owl:Ontology)
    }
    ORDER BY ?s
    """

    graph = load_graph(kg)
    results = graph.query(query)
    individuals = []

    for row in results:
        uri = row['s']

        # Skip blank nodes
        if isinstance(uri, rdflib.term.BNode):
            continue

        try:
            prefix, namespace, name = graph.compute_qname(uri)
        except Exception:
            prefix = "ns"
            name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri.split('/')[-1])
        
        individuals.append((prefix, name))

    return individuals

###########################################################################################

def list_all_classes_with_prefix(kg: str) -> list:
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    SELECT DISTINCT ?s
    WHERE {
        ?s a owl:Class .
    }
    ORDER BY ?s
    """
    graph = load_graph(kg)
    results = graph.query(query)
    classes = []

    for row in results:
        uri = row['s']

        # Skip blank nodes (just in case)
        if isinstance(uri, rdflib.term.BNode):
            continue

        try:
            prefix, namespace, name = graph.compute_qname(uri)
        except Exception:
            prefix = "ns"
            name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]

        classes.append((prefix, name))

    return classes

###########################################################################################

def list_all_properties_with_prefix(kg: str) -> list:

    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>

    SELECT DISTINCT ?p
    WHERE {
        ?p rdf:type ?type .
        FILTER(?type = owl:DatatypeProperty || ?type = owl:ObjectProperty)
    }
    ORDER BY ?p
    """
    graph = load_graph(kg)
    results = graph.query(query)
    properties = []

    for row in results:
        uri = row['p']

        # Skip blank nodes just in case
        if isinstance(uri, rdflib.term.BNode):
            continue

        try:
            prefix, namespace, name = graph.compute_qname(uri)
        except Exception:
            # fallback if namespace is unknown
            prefix = "ns"
            name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]

        properties.append((prefix, name))

    return properties

###########################################################################################

def list_all_datatypes_with_prefix(kg: str) -> list:

    query = """
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    SELECT DISTINCT ?datatype
    WHERE {
        ?s ?p ?o .
        FILTER(isLiteral(?o))
        BIND(datatype(?o) AS ?datatype)
        FILTER(BOUND(?datatype))
    }
    ORDER BY ?datatype
    """
    graph = load_graph(kg)
    results = graph.query(query)
    datatypes = []

    for row in results:
        uri = row['datatype']

        # Skip blank nodes just in case
        if isinstance(uri, rdflib.term.BNode):
            continue

        try:
            prefix, namespace, name = graph.compute_qname(uri)
        except Exception:
            # fallback if no known namespace
            prefix = "ns"
            name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]

        datatypes.append((prefix, name))

    return datatypes

##########################################################################################
###############################  DOAMIN DATASET GENERATOR ################################

def list_all_units(csv_file="units_table.csv"):
    df = pd.read_csv(csv_file)

    # Add prefix column first
    df["prefix"] = inst_prefix

    # Return tuples with prefix as the first field
    return list(df[['prefix', 'kind', 'unit']].itertuples(index=False, name=None))

##########################################################################################

def list_random_messages(kg: str, n: int):
    """
    Return n random dbc:Message individuals from the RDF graph `g`.
    Each message is returned as a (prefix, name) tuple with prefix 'dbc'.
    """
    query = """
    PREFIX dbc: <https://paitools.github.io/DBCOntology/DBC.owl#>
    SELECT DISTINCT ?message
    WHERE {
        ?message a dbc:Message .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    messages = []

    for row in results:
        uri = row['message']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        messages.append((inst_prefix, name))

    if not messages:
        return []

    n = min(n, len(messages))
    return random.sample(messages, n)

##########################################################################################

def list_random_signals(kg: str, n: int):
    """
    Return n random dbc:Signal individuals from the RDF graph `g`.
    Each signal is returned as a (prefix, name) tuple with prefix 'dbc'.
    """
    query = """
    PREFIX dbc: <https://paitools.github.io/DBCOntology/DBC.owl#>
    SELECT DISTINCT ?signal
    WHERE {
        ?signal a dbc:Signal .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    signals = []

    for row in results:
        uri = row['signal']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        signals.append((inst_prefix, name))

    if not signals:
        return []

    n = min(n, len(signals))
    return random.sample(signals, n)

###########################################################################################
def list_random_nodes(kg: str, n: int):
    """
    Return n random dbc:Node individuals from the RDF graph `g`.
    Each node is returned as a (prefix, name) tuple with prefix 'dbc'.
    """
    query = """
    PREFIX dbc: <https://paitools.github.io/DBCOntology/DBC.owl#>
    SELECT DISTINCT ?node
    WHERE {
        ?node a dbc:Node .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    nodes = []

    for row in results:
        uri = row['node']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        nodes.append((inst_prefix, name))

    if not nodes:
        return []

    n = min(n, len(nodes))
    return random.sample(nodes, n)

###########################################################################################

def list_random_sensors(kg: str, n: int):
    """
    Return n random sosa:Senosr individuals from the RDF graph `g`.
    Each sensor is returned as a (prefix, name) tuple with prefix 'sosa'.
    """
    query = """
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    SELECT DISTINCT ?sensor
    WHERE {
        ?sensor a sosa:Sensor .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    sensors = []

    for row in results:
        uri = row['sensor']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        sensors.append((inst_prefix, name))

    if not sensors:
        return []

    n = min(n, len(sensors))
    return random.sample(sensors, n)

###########################################################################################

def list_random_platforms(kg: str, n: int):
    """
    Return n random sosa:Platform individuals from the RDF graph `g`.
    Each platform is returned as a (prefix, name) tuple with prefix 'sosa'.
    """
    query = """
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    SELECT DISTINCT ?platform
    WHERE {
        ?platform a sosa:Platform .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    platforms = []

    for row in results:
        uri = row['platform']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        platforms.append((inst_prefix, name))

    if not platforms:
        return []

    n = min(n, len(platforms))
    return random.sample(platforms, n)

###########################################################################################
def list_random_temp_signals(kg: str, n: int):
    """
    Return n random dbc:Signal individuals from the RDF graph `g`.
    Each tempsignal is returned as a (prefix, name) tuple with prefix 'dbc'.
    """
    query = """
    PREFIX dbc: <https://paitools.github.io/DBCOntology/DBC.owl#>
    PREFIX ex: <http://example.org/individuals#>

    SELECT DISTINCT ?tempsignal
    WHERE {
        ?tempsignal a dbc:Signal ;
                    qudt:hasUnit ex:DEG_C .
    }
    """
    graph = load_graph(kg)
    results = graph.query(query)
    tempsignals = []

    for row in results:
        uri = row['tempsignal']
        # Extract only the local name
        name = str(uri).split('#')[-1] if '#' in str(uri) else str(uri).split('/')[-1]
        tempsignals.append((inst_prefix, name))

    if not tempsignals:
        return []

    n = min(n, len(tempsignals))
    return random.sample(tempsignals, n)

###########################################################################################

def list_random_dates(n: int):
    """
    Generate a list of n random dates between 2021-01-01 and 2026-12-31.
    Each date is returned as a tuple: (input_date, query_date)
    input_date: dd.mm.yyyy
    query_date: yyyy-mm-dd
    """
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2026, 12, 31)
    delta_days = (end_date - start_date).days

    dates = []
    for _ in range(n):
        random_day = start_date + timedelta(days=random.randint(0, delta_days))
        input_date = random_day.strftime("%d.%m.%Y")
        query_date = random_day.strftime("%Y-%m-%d")
        dates.append((input_date, query_date))

    return dates

###########################################################################################

def list_random_values(n: int):
    """
    Generate n random integer values between 15 and 45.
    Returns pairs: (input_value, query_value)
    input_value  -> string integer for sentence
    query_value  -> decimal string for SPARQL
    """
    values = []
    
    for _ in range(n):
        v = random.randint(15, 45)
        values.append((str(v), f"{v}.0"))
    
    return values
