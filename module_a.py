import pandas as pd
from sklearn.model_selection import train_test_split
import kg_reader as kgr


#####################################################################################################################################

# 1a.1
def describe_individual_1(kg: str):
    list1 = [
        "Describe", "Extract all information about", "Extract all info about",
        "Retrieve data of", "Retrieve information of", "Inspect details of",
        "List properties of", "List all properties of", "Get the data from",
        "Get the info from", "Get the information from",
        "Explore", "Explore characteristics of"
    ]
    
    list2 = kgr.list_all_individuals_with_prefix(kg)     
    list3 = ["instance", "individual"]

    data = []    
    for item1 in list1:
        for prefix, instance in list2:
            for item3 in list3:
                sentence = f"{item1} {instance} {item3}"
                query = f"""SELECT DISTINCT ?property ?value\nWHERE {{\n {prefix}:{instance} ?property ?value . \n}}"""               
                data.append([sentence, query])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 1a.2
def describe_individual_2(kg: str):
    list1 = [
        "Describe", "Extract all information about", "Extract all info about",
        "Retrieve data of", "Retrieve information of", "Inspect details of",
        "List properties of", "List all properties of", "Get the data from",
        "Get the info from", "Get the information from",
        "Explore", "Explore characteristics of"
    ]
    
    list2 = kgr.list_all_individuals_with_prefix(kg)
    list3 = ["instance", "individual"]

    data = []    
    for item1 in list1:
        for prefix, instance in list2:
            for item3 in list3:
                sentence = f"{item1} {prefix}:{instance} {item3}"
                query = f"""SELECT DISTINCT ?property ?value\nWHERE {{\n {prefix}:{instance} ?property ?value . \n}}"""               
                data.append([sentence, query])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

####################################################################################################################################

# 2a.1
def list_instances_of_class_1(kg: str):

    list1 = ["List", "Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["instances", "individuals"]
    list3 = ["of"]
    list4 = kgr.list_all_classes_with_prefix(kg)   
    list5 = ["class", ""]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {class_name} {item5}"
                        second_column = f"SELECT ?instance\nWHERE {{\n ?instance a {prefix}:{class_name} . \n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 2a.2
def list_instances_of_class_2(kg: str):

    list1 = ["List", "Retrieve", "Get", "show me", "Fetch", "give me", "Show", "Display"]
    list2 = ["instances", "individuals"]
    list3 = ["of"]
    list4 = kgr.list_all_classes_with_prefix(kg)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    sentence = f"{item1} {item2} {item3} {prefix}:{class_name}"
                    second_column = f"SELECT ?instance\nWHERE {{\n ?instance a {prefix}:{class_name} . \n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

######################################################################################################################################

# 3a
def list_all_classes_ontop():
    list1 = ["List all", "Retrieve all", "give me", "Get all", "get me all", "show me all", "Show all", "Display all"]
    list2 = ["classes", "DBC classes", "system classes", "ontology classes", "classes in the system", "defined classes"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT DISTINCT ?class\nWHERE {{\n ?instance a ?class .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 4a
def list_all_properties():
    list1 = ["List all", "Retrieve all", "Get all", "show me all", "give me all", "Show all", "Display all"]
    list2 = ["properties", "defined properties", "DBC properties", "system properties", "ontology properties", "properties in the system"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?s ?property ?o .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 5a
def list_all_object_properties():
    list1 = ["List all", "Retrieve all", "Get all", "give me all", "show me all", "Show all", "Display all"]
    list2 = ["object properties", "defined object properties", "system's object properties", "DBC object properties", "object properties in the system", "object properties of the ontology"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?property\nWHERE {{\n ?property a owl:ObjectProperty .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

########################################################################################################################################

# 6a
def list_all_data_properties():
    list1 = ["List all", "Retrieve all", "Get all", "give me all", "show me all", "Show all", "Display all"]
    list2 = ["data properties", "defined data properties", "system's data properties", "datatype properties", "DBC data properties", "data properties in the system", "ontology data properties"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?property\nWHERE {{\n ?property a owl:DatatypeProperty .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##########################################################################################################################################

# 7a.1
def list_all_insances_of_class_1(kg: str):

    list1 = ["List", "Retrieve", "Get", "Fetch", "show me", "give me", "Show", "Display"]
    list2 = ["instances", "individuals"]
    list3 = ["of", "within"]
    list4 = kgr.list_all_classes_with_prefix(kg) 
    list5 = ["class, including subclasses", "class, including its subclasses", "including subclasses"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {class_name} {item5}"
                        second_column = f"SELECT ?instance\nWHERE {{\n ?instance a/rdfs:subClassOf* {prefix}:{class_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 7a.2
def list_all_insances_of_class_2(kg: str):

    list1 = ["List all", "Retrieve all", "Get all", "give me all", "show me all", "Show all", "Display all"]
    list2 = ["instances", "individuals"]
    list3 = ["of", "within"]
    list4 = kgr.list_all_classes_with_prefix(kg) 
    list5 = ["class", ""]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {prefix}:{class_name} {item5}"
                        second_column = f"SELECT ?instance\nWHERE {{\n ?instance a/rdfs:subClassOf* {prefix}:{class_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 8a
def list_instances_with_property(kg: str):

    list1 = ["List", "Retrieve", "Get", "give me", "show", "List all", "Retrieve all", "Get all", "give me all", "show me all", "Show all", "Display all"]
    list2 = ["instances", "individuals"]
    list3 = ["with", "having", "which have", "exhibiting", "containing"]
    list4 = kgr.list_all_properties_with_prefix(kg)
    list5 = ["property"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, prop_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {prop_name} {item5}"
                        second_column = f"SELECT ?instance\nWHERE {{\n ?instance {prefix}:{prop_name} ?o .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################################################################
##################################################################################################################################################################################

# 9a
def list_subclasses_of_class(kg: str):

    list1 = ["List", "Retrieve", "Get", "show", "give me", "show me"]
    list2 = ["subclasses", "sub-classes"]
    list3 = ["of", "within"]
    list4 = kgr.list_all_classes_with_prefix(kg) 
    list5 = ["class", ""]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {class_name} {item5}"
                        second_column = f"SELECT DISTINCT ?subclass\nWHERE {{\n ?subclass rdfs:subClassOf {prefix}:{class_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################################################

# 10a
def list_all_subclasses_of_class(kg: str):

    list1 = ["List all", "Retrieve all", "Get all", "show all", "show me all", "list me all", "give me all"]
    list2 = ["subclasses"]
    list3 = ["of", "within"]
    list4 = kgr.list_all_classes_with_prefix(kg)
    list5 = [" class", ", including sub-subclasses", " class, including its subclasses"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, class_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {class_name}{item5}"
                        second_column = f"SELECT DISTINCT ?subclass\nWHERE {{\n ?subclass rdfs:subClassOf+ {prefix}:{class_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

# 11a.1
def list_all_individuals_1():
    list1 = ["List all", "Retrieve all", "Get all", "Show all", "give me all", "show me all"]
    list2 = ["instances", "individuals", "user defined instances", "named individuals", "existing instances", "system instances", "individuals in the system", "system individuals"]
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?individual\nWHERE {{\n ?individual a owl:NamedIndividual .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df


# 11a.2
def list_all_individuals_alternative():
    list1 = ["List all", "Retrieve all", "Get all", "Show all", "give me all", "show me all"]
    list2 = ["instances", "individuals", "existing instances", "system instances", "individuals in the system", "system individuals"]
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?individual\nWHERE {{\n ?individual rdf:type ?class .\nFILTER(?class != owl:Class && ?class != owl:ObjectProperty && ?class != owl:DatatypeProperty && ?class != rdf:Property && ?class != owl:Ontology)\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

# 12a
def list_all_datatypes():
    list1 = ["List all", "Retrieve all", "Get all", "give me all", "show me all", "Show all", "Display all"]
    list2 = ["data types", "datatypes", "defined data types", "data types in the system", "available data types", "ontology data types"]
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT DISTINCT (datatype(?o) AS ?datatype)\nWHERE {{\n ?s ?p ?o .\n FILTER(isLiteral(?o))\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################

# 13a
def list_all_individuals_with_comments():

    list1 = ["List all", "list", "Retrieve all", "get", "Get all", "give me all", "show", "show me all", "Show all", "Display all"]
    list2 = ["instances", "individuals"]
    list3 = ["with", "having", "which have", "containing"]
    list4 = ["comments", "user comments"]
    
  
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for item4 in list4:
                    sentence = f"{item1} {item2} {item3} {item4}"
                    second_column = f"SELECT DISTINCT ?instance ?o\nWHERE {{\n ?instance a owl:NamedIndividual .\n ?instance rdfs:comment ?o .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################

# 14a
def get_data_type_of_individual(kg: str):  
    list1 = ["Retrieve", "Get", "give me", "show me", "Show"]
    list2 = ["data types of", "data types associated with"]
    list3 = kgr.list_all_individuals_with_prefix(kg)
    list4 = ["instance", "individual"]
    

    data = []
    for item1 in list1:
        for item2 in list2:
            for prefix, instance in list3:
                for item4 in list4:                  
                    sentence = f"{item1} {item2} {instance} {item4}"
                    second_column = f"SELECT DISTINCT ?property ?datatype WHERE {{ {prefix}:{instance} ?property ?o . FILTER(isLiteral(?o)) BIND(datatype(?o) AS ?datatype) }}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################

# 15a
def list_all_individuals_with_datatype(kg: str):

    list1 = ["List all", "list", "Retrieve all", "get", "Get all", "show", "give me all", "show me", "Show all", "Display all"]
    list2 = ["instances", "individuals"]
    list3 = ["with", "having", "which have", "containing"]
    list4 = kgr.list_all_datatypes_with_prefix(kg)  
    list5 = ["data type", "datatype" ]
  

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, datatype_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {datatype_name} {item5}"
                        second_column = f"SELECT DISTINCT ?individual\nWHERE {{\n ?individual ?p ?o .\n FILTER(datatype(?o) = {prefix}:{datatype_name})\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

########################################################################################################################

# 16a 
def get_class_subclass_mapping():               

    list1 = ["Retrieve", "Get", "get all", "give me", "show me", "show all", "Show", "Display"]
    list2 = ["class subclass", "class hierarchy", "class to subclass"]
    list3 = ["mappings", "mappings in the ontology", "relations", "relationships", "associations"]
    
  
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT ?subclass ?class\nWHERE {{\n ?subclass rdfs:subClassOf ?class .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################
#######################################################################################################################

# List of functions
a_functions_all = [describe_individual_1, describe_individual_2, list_instances_of_class_1, list_instances_of_class_2, list_all_classes_ontop, list_all_properties, list_all_object_properties, list_all_data_properties,
             list_all_insances_of_class_1, list_all_insances_of_class_2, list_instances_with_property, list_subclasses_of_class, list_all_subclasses_of_class, list_all_individuals_1,
               list_all_datatypes, get_data_type_of_individual, list_all_individuals_with_datatype, list_all_individuals_with_comments, get_class_subclass_mapping]

a_functions_instances = [describe_individual_1, describe_individual_2, list_instances_of_class_1, list_instances_of_class_2,
             list_all_insances_of_class_1, list_all_insances_of_class_2, list_instances_with_property, list_subclasses_of_class, list_all_subclasses_of_class,
               get_data_type_of_individual, list_all_individuals_with_datatype]

a_functions_no_instances = [list_all_classes_ontop, list_all_properties, list_all_object_properties, list_all_data_properties,
             list_all_individuals_1,
               list_all_datatypes, list_all_individuals_with_comments, get_class_subclass_mapping]

#################################################################
####################### Run all functions #######################

def finall():
    """
    Hybrid dataset creation:

    1. KG-dependent functions → split by KG (train/val)
       + 20% sampling per function for validation
    2. Non-KG functions → random 90/10 split
    """

    df_train = pd.DataFrame(columns=['Sentence', 'Query'])
    df_val   = pd.DataFrame(columns=['Sentence', 'Query'])

    # ===============================
    # 1. KG-DEPENDENT FUNCTIONS
    # ===============================
    for func in a_functions_instances:
        df_train_func = func("train")
        df_val_func   = func("val")

        # Full train data
        df_train = pd.concat([df_train, df_train_func], ignore_index=True)

        # 20% validation per function (at least 1 sample)
        if len(df_val_func) > 0:
            n = max(1, int(0.2 * len(df_val_func)))
            df_val_func = df_val_func.sample(n=n, random_state=42)

        df_val = pd.concat([df_val, df_val_func], ignore_index=True)

    # ===============================
    # 2. NON-KG FUNCTIONS
    # ===============================
    df_no_instances = pd.DataFrame(columns=['Sentence', 'Query'])

    for func in a_functions_no_instances:
        df_no_instances = pd.concat([df_no_instances, func()], ignore_index=True)

    # Shuffle + split
    if len(df_no_instances) > 1:
        train_split, val_split = train_test_split(
            df_no_instances,
            test_size=0.1,
            shuffle=True,
            random_state=42
        )

        df_train = pd.concat([df_train, train_split], ignore_index=True)
        df_val   = pd.concat([df_val, val_split], ignore_index=True)

    return df_train, df_val
