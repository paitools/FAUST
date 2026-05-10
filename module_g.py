import pandas as pd
from sklearn.model_selection import train_test_split


####################################################################################################################################

# 1g
def get_all_signals():
    list1 = ["List all", "list", "Retrieve all", "Get all", "get", "show me all", "Show all", "Display all"]
    list2 = ["signals", "available signals", "encoded CAN signals", "DBC signals", "CAN signals", "CAN bus signals", "encoded signals"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?signal\nWHERE {{\n ?signal a dbc:Signal .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

####################################################################################################################################

# 2g
def get_all_messages():
    list1 = ["List all", "list", "Retrieve all", "Get all", "get", "show me all", "Show all", "Display all"]
    list2 = ["messages", "DBC messages", "CAN messages", "CAN bus messages", "observable messages", "messages in the system"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?message\nWHERE {{\n ?message a dbc:Message .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

######################################################################################################################################

# 3g
def get_signal_message_mapping():               

    list1 = ["List", "Retrieve", "Get", "give me", "show me", "Fetch", "Show", "Display"]
    list2 = ["signal message", "DBC signal to message", "signal to message"]
    list3 = ["mapping", "relation", "connection"]
    
  
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?signal ?message\nWHERE {{\n ?signal a dbc:Signal .\n ?message dbc:hasSignal ?signal .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 4g
def list_all_message_properties():
    list1 = ["List all", "list", "Retrieve all", "Get all", "get", "show", "show me", "show me all", "Show all"]
    list2 = ["message properties", "DBC message properties", "CAN message properties", "properties of messages", "message fields"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?message a dbc:Message ;\n  ?property ?o .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 5g
def list_all_units():
    list1 = ["List all", "Retrieve all", "Get all", "get", "show me all", "Show all", "Display all"]
    list2 = ["units", "DBC units", "defined units", "available units", "QUDT units", "units in the system", "signal units"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT DISTINCT ?unit\nWHERE {{\n ?signal qudt:hasUnit ?unit .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

########################################################################################################################################

# 6g
def list_all_encodings():
    list1 = ["List all", "Retrieve all", "Get all", "get", "show me", "show me all", "Show all"]
    list2 = ["encodings", "defined encoding schemas", "message encoding schemas", "message encodings", "encoding schemas", "DBC encoding schemas", "encodings in the system", "encoding schemas in the system"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?encoding\nWHERE {{\n ?message dbc:encodedVia ?encoding .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##########################################################################################################################################

# 7g
def list_message_with_most_signals():                

    list1 = ["List", "Retrieve", "Get", "give me", "show me", "Show", "Display"]
    list2 = ["message", "DBC message", "CAN message", "CAN bus message"]
    list3 = ["with", "having", "which have", "containing"]
    list4 = ["the highest number of signals", "the most signals", "the largest number of signals", "the highest signal count", "the greatest number of signals"]
    
  
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for item4 in list4:
                    sentence = f"{item1} {item2} {item3} {item4}"
                    second_column = f"SELECT ?message (COUNT(?signal) AS ?count)\nWHERE {{\n ?message a dbc:Message .\n ?signal dbc:isPartOf ?message .\n}}\nGROUP BY ?message\nORDER BY DESC(?count)\nLIMIT 1"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##########################################################################################################################################

# 8g
def get_encoding_of_message_with_most_signals():

    list1 = ["List", "Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["encoding of", "encoding shema of"]
    list3 = ["message", "CAN message", "CAN bus message", "DBC message"]
    list4 = ["containing", "which has", "having"]
    list5 = ["the highest number of siganls", "the largest number of signals"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for item4 in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {item4} {item5}"
                        second_column = f"SELECT ?message ?encoding\nWHERE {{\n {{ SELECT ?message (COUNT(?signal) AS ?count)\n  WHERE {{ ?signal dbc:isPartOf ?message . }}\n  GROUP BY ?message\n  ORDER BY DESC(?count)\n  LIMIT 1\n }}\n ?signal dbc:isPartOf ?message ;\n  dbc:decodedVia ?encoding .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################
############### SENSORS & PLATFORMS ###################################################################################################

# 9g
def get_sensor_node_mapping():               

    list1 = ["Retrieve", "Get", "give me", "show me", "Fetch", "Show", "Display"]
    list2 = ["sensor to node", "sensor node", "sensor transmitter node", "sensor to ECU", "sensor to transmitter node", "sensor to ECU node", "sniffing sensor to transmitter node"]
    list3 = ["mapping", "relationship", "connection"]
    
  
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?sensor ?node\nWHERE {{\n ?message a dbc:Message ;\n  dbc:hasTransmitter ?node .\n ?sensor sosa:observes ?message .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################################################################

# 10g
def get_platforms_hosting_sensors():                

    list1 = ["List", "list all", "Retrieve", "Get", "give me", "show me", "Show all", "get all"]
    list2 = ["platforms", "DBC platforms", "CAN buses", "CAN bus platforms"]
    list3 = ["hosting", "which host"]
    list4 = ["sensors", "sniffing sensors"]
     
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for item4 in list4:
                    sentence = f"{item1} {item2} {item3} {item4}"
                    second_column = f"SELECT DISTINCT ?platform ?sensor\nWHERE {{\n ?platform sosa:hosts ?sensor .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################################################

# 11g
def get_message_platform_mapping():               

    list1 = ["Retrieve", "Get", "give me", "show me", "Fetch", "Show", "Display"]
    list2 = ["message platform", "message to CAN bus", "message to platform", "message to CAN bus platform"]
    list3 = ["mapping", "relation", "connection", "association"]
      
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT ?message ?platform\nWHERE {{\n ?message a dbc:Message ;\n  sosa:isObservedBy ?sensor .\n ?sensor sosa:isHostedBy ?platform .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

#12g
def get_all_platforms():
    list1 = ["List all", "list", "Retrieve all", "Get all", "get", "show", "show me all", "Show all", "Display all"]
    list2 = ["platforms", "existing platforms", "CAN busses", "available platforms", "DBC platforms", "platforms in the system", "CAN bus platforms", "CAN bus platforms in the system"] 
    

    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?platform\nWHERE {{\n ?platform a sosa:Platform .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################
############### OBSERVATIONS ###################################################################################################################

# 13g
def get_observation_types():
    list1 = ["List", "Retrieve", "Get", "get all", "Fetch", "Show", "show all", "give me", "show me", "show me all"]
    list2 = ["observation classes", "observation types", "types of observation in the system", "present types of observation", "classes of observation", "observation types represented in the system"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            sentence = f"{item1} {item2}"
            second_column = f"SELECT ?observation\nWHERE {{\n ?observation rdfs:subClassOf sosa:Observation .\n}}"
            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

# 14g.1
def list_message_log_properties_1():               

    list1 = ["List", "list all", "Get", "get all", "give me", "give me all", "show me", "Fetch", "Show", "show all", "Display"]
    list2 = ["properties", "core components", "fields"]
    list3 = ["of a message log", "of a CAN message log", "of message logs", "of DBC message logs"]
      
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?messagelog a dbc:MessageLog ;\n  ?property ?o .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 14g.2
def list_message_log_properties_2():               

    list1 = ["List", "list all", "Get", "get all", "give me", "show me", "Fetch", "Show", "Display"]
    list2 = ["message log", "CAN message log", "messagelog", "DBC message log"]
    list3 = ["properties", "core components", "fields"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?messagelog a dbc:MessageLog ;\n  ?property ?o .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################

# 15g.1
def list_signal_log_properties_1():               

    list1 = ["List", "list all", "Get", "get all", "give me", "show me", "show me all", "Fetch", "Show", "show all", "Display"]
    list2 = ["properties", "core components", "fields"]
    list3 = ["of a signal log", "of a CAN signal log", "of signal logs", "of DBC signal logs"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  ?property ?o .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 15g.2
def list_signal_log_properties_2():               

    list1 = ["List", "Get", "give me", "show me", "Fetch", "Show", "Display"]
    list2 = ["signal log", "CAN signal log", "DBC signal log", "signallog"]
    list3 = ["properties", "core components", "fields"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?property\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  ?property ?o .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################

# 16g.1
def get_message_log_platforms_1():               

    list1 = ["List", "list all", "Get", "get all", "give me", "show me", "Fetch", "Show", "show all", "Display"]
    list2 = ["platforms", "CAN busses", "CAN bus platforms"]
    list3 = ["of a message log", "of DBC message logs", "of message logs", "carring message logs"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?platform\nWHERE {{\n ?messagelog dbc:observedOn ?platform .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 16g.2
def get_message_log_platforms_2():               

    list1 = ["List", "list all", "Get", "get all", "give me", "show me", "Fetch", "Show", "show all", "Display"]
    list2 = ["message log", "messagelog"]
    list3 = ["platforms", "CAN buses", "buses", "CAN bus platforms"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                    sentence = f"{item1} {item2} {item3}"
                    second_column = f"SELECT DISTINCT ?platform\nWHERE {{\n ?messagelog dbc:observedOn ?platform .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################

# 17g
def get_units_of_signal_logs():                

    list1 = ["List all", "list", "Retrieve", "Get", "give me", "show me", "show me all", "Show all", "get all"]
    list2 = ["units", "measurement units", "QUDT units"]
    list3 = ["of", "associated to", "assigned to"]
    list4 = ["signal log results", "signal logs", "signal log observations"]
    
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for item4 in list4:
                    sentence = f"{item1} {item2} {item3} {item4}"
                    second_column = f"SELECT DISTINCT ?unit\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  sosa:observedProperty ?signal .\n ?signal qudt:hasUnit ?unit .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

########################################################################################################################
########################################################################################################################

# List of functions
g_functions = [get_all_signals, get_all_messages, get_signal_message_mapping, list_all_message_properties, list_all_units, list_all_encodings, list_message_with_most_signals,
            get_sensor_node_mapping, get_platforms_hosting_sensors, get_message_platform_mapping, get_all_platforms, get_observation_types, list_message_log_properties_1, list_message_log_properties_2,
            list_signal_log_properties_1, list_signal_log_properties_2, get_message_log_platforms_1, get_message_log_platforms_2, get_units_of_signal_logs]

g_functions_no_instances = [get_all_signals, get_all_messages, get_signal_message_mapping, list_all_message_properties, list_all_units, list_all_encodings, list_message_with_most_signals, get_encoding_of_message_with_most_signals,
            get_sensor_node_mapping, get_platforms_hosting_sensors, get_message_platform_mapping, get_all_platforms, get_observation_types, list_message_log_properties_1, list_message_log_properties_2,
            list_signal_log_properties_1, list_signal_log_properties_2, get_message_log_platforms_1, get_message_log_platforms_2, get_units_of_signal_logs]

#################################################################
####################### Run all functions #######################

def finall():
    """
    Hybrid dataset creation:

    Non-KG functions → each function is split 90/10 independently
    """

    df_train = pd.DataFrame(columns=['Sentence', 'Query'])
    df_val   = pd.DataFrame(columns=['Sentence', 'Query'])

    # ===============================
    # NON-KG FUNCTIONS (per-function split)
    # ===============================
    for func in g_functions_no_instances:
        df_func = func()

        if len(df_func) > 1:
            train_split, val_split = train_test_split(
                df_func,
                test_size=0.1,
                shuffle=True,
                random_state=42
            )

            df_train = pd.concat([df_train, train_split], ignore_index=True)
            df_val   = pd.concat([df_val, val_split], ignore_index=True)

        else:
            # fallback: if too small, just put into train
            df_train = pd.concat([df_train, df_func], ignore_index=True)

    return df_train, df_val
