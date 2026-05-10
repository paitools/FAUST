import pandas as pd
from sklearn.model_selection import train_test_split
import kg_reader as kgr


#####################################################################################################################################

# 1d
def list_signal_measuring_kind():               

    list1 = ["List", "Retrieve", "Get", "give me", "show me", "Show", "Display"]
    list2 = ["signals", "DBC signals", "CAN signals", "CAN bus signals", "encoded signals"]
    list3 = ["that measure", "observing", "carrying", "measuring"]
    list4 = kgr.list_all_units()  
      
    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for prefix, kind, unit in list4:
                    sentence = f"{item1} {item2} {item3} {kind}"
                    second_column = f"SELECT DISTINCT ?signal\nWHERE {{\n ?signal qudt:hasUnit {prefix}:{unit} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

####################################################################################################################################

# 2d.1
def list_signals_of_message_1(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["signals", "DBC signals", "CAN signals", "CAN bus signals"]
    list3 = ["of", "which are part of", "part of"]
    list4 = kgr.list_random_messages(kg, 10)
    list5 = ["message"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for msg_prefix, msg_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {msg_name} {item5}"
                        second_column = f"SELECT DISTINCT ?signal\nWHERE {{\n ?signal dbc:isPartOf {msg_prefix}:{msg_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 2d.2
def list_signals_of_message_2(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["signals", "DBC signals", "CAN signals", "CAN bus signals"]
    list3 = ["of", "which are part of", "part of"]
    list4 = kgr.list_random_messages(kg, 10)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for msg_prefix, msg_name in list4:
                    sentence = f"{item1} {item2} {item3} {msg_prefix}:{msg_name}"
                    second_column = f"SELECT DISTINCT ?signal\nWHERE {{\n ?signal dbc:isPartOf {msg_prefix}:{msg_name} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

######################################################################################################################################

# 3d.1
def get_message_of_signal_1(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["message", "DBC message", "CAN message", "CAN bus message"]
    list3 = ["of", "encoding", "which encodes"]
    list4 = kgr.list_random_signals(kg, 15)
    list5 = ["signal"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {sig_name} {item5}"
                        second_column = f"SELECT DISTINCT ?message\nWHERE {{\n ?message dbc:hasSignal {sig_prefix}:{sig_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 3d.2
def get_message_of_signal_2(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["message", "DBC message", "CAN message", "CAN bus message"]
    list3 = ["of", "encoding", "which encodes", "which has signal"]
    list4 = kgr.list_random_signals(kg, 10)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    sentence = f"{item1} {item2} {item3} {sig_prefix}:{sig_name}"
                    second_column = f"SELECT DISTINCT ?message\nWHERE {{\n ?message dbc:hasSignal {sig_prefix}:{sig_name} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 4g.1
def get_encoding_of_signal_1(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["encoding schema", "DBC encoding schema", "encodings"]
    list3 = ["of", "from", "corresponding to", "assigned to"]
    list4 = kgr.list_random_signals(kg, 12)
    list5 = ["signal"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {sig_name} {item5}"
                        second_column = f"SELECT DISTINCT ?encoding ?property ?value\nWHERE {{\n {sig_prefix}:{sig_name} dbc:decodedVia ?encoding .\n ?encoding ?property ?value .\n}}" 
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 4d.2
def get_encoding_of_signal_2(kg: str):

    list1 = ["Retrieve", "Get", "give me", "Show", "show me", "Display"]
    list2 = ["encoding schema", "DBC encoding schema", "encodings"]
    list3 = ["of", "from", "corresponding to", "assigned to"]
    list4 = kgr.list_random_signals(kg, 10)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    sentence = f"{item1} {item2} {item3} {sig_prefix}:{sig_name}"
                    second_column = f"SELECT DISTINCT ?encoding ?property ?value\nWHERE {{\n {sig_prefix}:{sig_name} dbc:decodedVia ?encoding .\n ?encoding ?property ?value .\n}}" #todo proveri
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 5d.1
def get_signals_targeting_ECU_1(kg: str):  

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["signals", "DBC signals", "CAN signals", "CAN bus signals"]
    list3 = ["targeting", "having"]
    list4 = kgr.list_random_nodes(kg, 4)   #done
    list5 = ["node", "ECU", "receiver node"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for node_prefix, ecu in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {ecu} {item5}"
                        second_column = f"SELECT DISTINCT ?signal\nWHERE {{\n ?signal dbc:hasReceiver {node_prefix}:{ecu} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 5d.2
def get_signals_targeting_ECU_2(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["signals", "DBC signals", "CAN signals", "CAN bus signals"]
    list3 = ["having receiver node", "targeting ECU node", "with receiver node"]
    list4 = kgr.list_random_nodes(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for node_prefix, ecu in list4:
                    sentence = f"{item1} {item2} {item3} {node_prefix}:{ecu}"
                    second_column = f"SELECT DISTINCT ?signal\nWHERE {{\n ?signal dbc:hasReceiver {node_prefix}:{ecu} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

########################################################################################################################################

# 6g.1
def get_decid_of_signal_1(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["decimal id", "decID", "decimal identifier"]
    list3 = ["of", "associated with", "linked to"]
    list4 = kgr.list_random_signals(kg, 8)
    list5 = ["signal", "DBC signal", "CAN signal"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {sig_name} {item5}"
                        second_column = f"SELECT DISTINCT ?decID\nWHERE {{\n {sig_prefix}:{sig_name} dbc:isPartOf ?message .\n ?message dbc:hasDecID ?decID .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 6d.2
def get_decid_of_signal_2(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["decimal id", "dec Id", "decID", "decimal identifier"]
    list3 = ["of", "associated with", "linked to"]
    list4 = kgr.list_random_signals(kg, 8)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sig_prefix, sig_name in list4:
                    sentence = f"{item1} {item2} {item3} {sig_prefix}:{sig_name}"
                    second_column = f"SELECT DISTINCT ?decID\nWHERE {{\n {sig_prefix}:{sig_name} dbc:isPartOf ?message .\n ?message dbc:hasDecID ?decID .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##########################################################################################################################################
############### SENSORS & PLATFORMS ######################################################################################################

# 7d.1
def get_platform_of_sensor_1(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["the platform", "the CAN bus platform", "the CAN bus"]
    list3 = ["of", "associated with", "linked to", "hosting", "which hosts"]
    list4 = kgr.list_random_sensors(kg, 4)
    list5 = ["sensor", "sniffing sensor", "CAN bus sniffing sensor"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sen_prefix, sensor_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {sensor_name} {item5}"
                        second_column = f"SELECT DISTINCT ?platform\nWHERE {{\n ?platform sosa:hosts {sen_prefix}:{sensor_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 7d.2
def get_platform_of_sensor_2(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["the platform", "the CAN bus platform", "the CAN bus"]
    list3 = ["of", "associated with", "linked to"]
    list4 = kgr.list_random_sensors(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sen_prefix, sensor_name in list4:
                    sentence = f"{item1} {item2} {item3} {sen_prefix}:{sensor_name}"
                    second_column = f"SELECT DISTINCT ?platform\nWHERE {{\n ?platform sosa:hosts {sen_prefix}:{sensor_name} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#######################################################################################################################################

# 8d.1
def get_hexids_on_platfrom_1(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "give me", "Show", "show me", "Display"]
    list2 = ["hexadecimal id's", "hex IDs", "hexIDs", "message IDs", "hexadecimal identifiers"]
    list3 = ["on", "associated with", "linked to"]
    list4 = kgr.list_random_platforms(kg, 4)
    list5 = ["platform", "CAN bus", "CAN bus platform"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for plat_prefix, platfrom_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {platfrom_name} {item5}"
                        second_column = f"SELECT DISTINCT ?hexid\nWHERE {{\n ?messagelog dbc:observedOn {plat_prefix}:{platfrom_name} ;\n  dbc:hasHexID ?hexid .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 8d.2
def get_hexids_on_platfrom_2(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "give me", "Show", "show me", "Display"]
    list2 = ["hexadecimal id's", "hexIDs", "message IDs", "hexadecimal identifiers"]
    list3 = ["on", "associated with", "linked to"]
    list4 = kgr.list_random_platforms(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for plat_prefix, platfrom_name in list4:
                    sentence = f"{item1} {item2} {item3} {plat_prefix}:{platfrom_name}"
                    second_column = f"SELECT DISTINCT ?hexid\nWHERE {{\n ?messagelog dbc:observedOn {plat_prefix}:{platfrom_name} ;\n  dbc:hasHexID ?hexid .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################################################################

# 9d.1
def get_rxnodes_of_sensor_1(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "give me", "Show", "show me", "Display"]
    list2 = ["transmitter nodes", "transmitter ECUs", "Tx nodes"]
    list3 = ["on", "associated with", "linked to"]
    list4 = kgr.list_random_sensors(kg, 4)
    list5 = ["sensor", "sniffing sensor"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sen_prefix, sensor_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {sensor_name} {item5}"
                        second_column = f"SELECT DISTINCT ?transmitter\nWHERE {{\n ?message dbc:hasTransmitter ?transmitter ;\n  sosa:isObservedBy {sen_prefix}:{sensor_name} .\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 9d.2
def get_rxnodes_of_sensor_2(kg: str):

    list1 = ["List", "list all", "Retrieve", "Get", "get all", "give me", "Show", "show me", "Display"]
    list2 = ["transmitter nodes", "transmitter ECUs", "Tx ECUs", "Tx nodes"]
    list3 = ["on", "associated with", "linked to"]
    list4 = kgr.list_random_sensors(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for sen_prefix, sensor_name in list4:
                    sentence = f"{item1} {item2} {item3} {sen_prefix}:{sensor_name}"
                    second_column = f"SELECT DISTINCT ?transmitter\nWHERE {{\n ?message dbc:hasTransmitter ?transmitter ;\n  sosa:isObservedBy {sen_prefix}:{sensor_name} .\n}}"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################################################
############### OBSERVATIONS ##################################################################################################################

# 10d.1
def get_current_temp_of_signal_1(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["the current temperature", "the latest temperature", "current temperature"]
    list3 = ["of", "from"]
    list4 = kgr.list_random_temp_signals(kg, 4)
    list5 = ["signal", "DBC signal", "", "CAN signal"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for tsig_prefix, temp_signals in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {temp_signals} {item5}"
                        second_column = f"SELECT ?tempvalue (MAX(?timestamp) AS ?latestTime)\nWHERE {{\n ?templog a dbc:SignalLog ;\n  sosa:observedProperty {tsig_prefix}:{temp_signals} ;\n  sosa:hasSimpleResult ?tempvalue ;\n  sosa:resultTime ?timestamp .\n}}\nGROUP BY ?tempvalue\nORDER BY DESC(?latestTime)\nLIMIT 1"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 10d.2
def get_current_temp_of_signal_2(kg: str):

    list1 = ["Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["the current temperature", "the latest temperature", "current temperature"]
    list3 = ["of", "from"]
    list4 = kgr.list_random_temp_signals(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for tsig_prefix, temp_signals in list4:
                    sentence = f"{item1} {item2} {item3} {tsig_prefix}:{temp_signals}"
                    second_column = f"SELECT ?tempvalue (MAX(?timestamp) AS ?latestTime)\nWHERE {{\n ?templog a dbc:SignalLog ;\n  sosa:observedProperty {tsig_prefix}:{temp_signals} ;\n  sosa:hasSimpleResult ?tempvalue ;\n  sosa:resultTime ?timestamp .\n}}\nGROUP BY ?tempvalue\nORDER BY DESC(?latestTime)\nLIMIT 1"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

# 11d.1
def get_latest_messagelogs_on_platfrom_1(kg: str):

    list1 = ["List", "Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["most recent", "recent"]
    list3 = ["message logs on", "message logs observed on", "message logs from"]
    list4 = kgr.list_random_platforms(kg, 4)
    list5 = ["platform", "bus", "", "CAN bus", "CAN bus platform"]

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for plat_prefix, platfrom_name in list4:
                    for item5 in list5:
                        sentence = f"{item1} {item2} {item3} {platfrom_name} {item5}"
                        second_column = f"SELECT ?timestamp ?value\nWHERE {{\n ?log a dbc:MessageLog ; dbc:observedOn {plat_prefix}:{platfrom_name} ;\n  sosa:hasSimpleResult ?value ;\n  sosa:resultTime ?timestamp .\n}}\nORDER BY DESC(?timestamp)\nLIMIT 300"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 11d.2
def get_latest_messagelogs_on_platfrom_2(kg: str):

    list1 = ["List", "Retrieve", "Get", "Fetch", "give me", "Show", "show me", "Display"]
    list2 = ["most recent", "recent"]
    list3 = ["message logs on", "message logs observed on"]
    list4 = kgr.list_random_platforms(kg, 4)

    data = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                for plat_prefix, platfrom_name in list4:
                    sentence = f"{item1} {item2} {item3} {plat_prefix}:{platfrom_name}"
                    second_column = f"SELECT ?timestamp ?data\nWHERE {{\n ?log a dbc:MessageLog ; dbc:observedOn {plat_prefix}:{platfrom_name} ;\n  sosa:hasSimpleResult ?data ;\n  sosa:resultTime ?timestamp .\n}}\nORDER BY DESC(?timestamp)\nLIMIT 300"
                    data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

################################################################################################################################################

# 12d
def get_the_average_of_signal_on_date(kg: str):

    list1 = ["Calculate", "Get", "give me", "Show", "show me"]
    list2 = ["the average value of", "the mean value of", "the average of", "the mean of"]
    list3 = kgr.list_random_signals(kg, 6)
    list4 = ["on", "signal on"]
    list5 = kgr.list_random_dates(5)

    data = []
    for item1 in list1:
        for item2 in list2:
            for sig_prefix, sig_name in list3:
                for item4 in list4:
                    for input_date, query_date in list5:
                        sentence = f"{item1} {item2} {sig_name} {item4} {input_date}"
                        second_column = f"SELECT (AVG(?value) AS ?meanValue)\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  sosa:hasSimpleResult ?value ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), \"{query_date}\"))\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###############################################################################################################

# 13d
def get_the_max_of_signal_on_date(kg: str):

    list1 = ["Calculate", "Get", "give me", "Show", "show me"]
    list2 = ["the maximum value of", "the max of", "the maximum of"]
    list3 = kgr.list_random_signals(kg, 6)
    list4 = ["on", "signal on", "observed on", "signal observed on"]
    list5 = kgr.list_random_dates(5)

    data = []
    for item1 in list1:
        for item2 in list2:
            for sig_prefix, sig_name in list3:
                for item4 in list4:
                    for input_date, query_date in list5:
                        sentence = f"{item1} {item2} {sig_name} {item4} {input_date}"
                        second_column = f"SELECT (MAX(?value) AS ?maxValue)\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  sosa:hasSimpleResult ?value ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), \"{query_date}\"))\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

#################################################################################################################################

# 14g
def get_the_mean_of_signal_from_date(kg: str):

    list1 = ["Calculate", "Get", "give me", "show me"]
    list2 = ["the average value of", "the mean value of", "the average of", "the mean of"]
    list3 = kgr.list_random_signals(kg, 5)
    list4 = ["from", "signal from", "starting from", "signal after", "as of"]
    list5 = kgr.list_random_dates(5)

    data = []
    for item1 in list1:
        for item2 in list2:
            for sig_prefix, sig_name in list3:
                for item4 in list4:
                    for input_date, query_date in list5:
                        sentence = f"{item1} {item2} {sig_name} {item4} {input_date}"
                        second_column = f"SELECT (AVG(?value) AS ?meanValue)\nWHERE {{\n ?signallog a dbc:SignalLog ;\n  sosa:hasSimpleResult ?value ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:resultTime ?timestamp .\n FILTER(?timestamp >= \"{query_date}T00:00:00\"^^xsd:dateTime)\n}}"
                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

##################################################################################################################################
############# Advanced Modeling ##################################################################################################

# 15d 
def get_sig_value_on_date_with_condition(kg: str):                

    list1 = ["List all", "Retrieve", "Get", "show me", "get all"]
    list2 = kgr.list_random_signals(kg, 4)
    list3 = ["values on", "measurements on"]
    list4 = kgr.list_random_dates(4)
    list5 = ["when"]
    list6 = kgr.list_random_temp_signals(kg, 2)
    list7 = ["exceeded", "was greater than"]
    list8 = kgr.list_random_values(4)
    list9 = ["°C", "degrees"]   
    
    data = []
    for item1 in list1:
        for sig_prefix, sig_name in list2:
            for item3 in list3:
                for input_date, query_date in list4:
                    for item5 in list5:
                        for tsig_prefix, temp_signals in list6:
                            for item7 in list7:
                                for imput_num, query_num in list8:
                                    for item9 in list9:
                                        sentence = f"{item1} {sig_name} {item3} {input_date} {item5} {temp_signals} {item7} {imput_num} {item9}"
                                        second_column = f"SELECT ?timestamp ?tempValue ?signalValue\nWHERE {{\n ?templog a dbc:SignalLog ;\n  sosa:observedProperty {tsig_prefix}:{temp_signals} ;\n  sosa:hasSimpleResult ?tempValue ;\n  sosa:resultTime ?timestamp .\n FILTER(?tempValue > {query_num} && STRSTARTS(STR(?timestamp), \"{query_date}\"))\n OPTIONAL {{\n ?signallog a dbc:SignalLog ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:hasSimpleResult ?signalValue ;\n  sosa:resultTime ?signaltimestamp .\n FILTER(SUBSTR(STR(?timestamp),1,19)=SUBSTR(STR(?signaltimestamp),1,19)) }}\n }}\nORDER BY ?timestamp"
                                        data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###################################################################################################################################################################################

# 16d.1
def get_signal_value_higher_than_1(kg: str):

    list1 = ["List", "Retrieve", "Get", "Show", "show me"]
    list2 = kgr.list_random_signals(kg, 4)
    list3 = ["values greater than", "values higher than", "logs exceeding"]
    list4 = kgr.list_random_values(4)
    list5 = [", recorded on", ", observed on"]
    list6 = kgr.list_random_dates(4)


    data = []
    for item1 in list1:
        for sig_prefix, sig_name in list2:
            for item3 in list3:
                for input_num, query_num in list4:
                    for item5 in list5:
                        for input_date, query_date in list6:
                            sentence = f"{item1} {sig_name} {item3} {input_num}{item5} {input_date}"
                            second_column = f"SELECT ?timestamp ?signalValue\nWHERE {{\n ?log a dbc:SignalLog ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:hasSimpleResult ?signalValue ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), '{query_date}') && ?signalValue > {query_num})\n}}\nORDER BY ?timestamp"
                            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 16d.2
def get_signal_value_higher_than_2(kg: str):

    list1 = ["List", "Retrieve", "Get", "give me", "show me"]
    list2 = kgr.list_random_signals(kg, 4)
    list3 = ["values on"]
    list4 = kgr.list_random_dates(4)
    list5 = ["which are higher than", "that are larger than"]
    list6 = kgr.list_random_values(4)


    data = []
    for item1 in list1:
        for sig_prefix, sig_name in list2:
            for item3 in list3:
                for input_date, query_date in list4:
                    for item5 in list5:
                        for input_num, query_num in list6:
                            sentence = f"{item1} {sig_name} {item3} {input_date} {item5} {input_num}"
                            second_column = f"SELECT ?timestamp ?signalValue\nWHERE {{\n ?log a dbc:SignalLog ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:hasSimpleResult ?signalValue ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), '{query_date}') && ?signalValue > {query_num})\n}}\nORDER BY ?timestamp"
                            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

###################################################################################################################################################################################

# 17d.1
def get_signal_value_smaller_than_1(kg: str):

    list1 = ["List", "Retrieve", "Get", "Show", "show me"]
    list2 = kgr.list_random_signals(kg, 4)
    list3 = ["values smaller than", "values lower than", "logs below"]
    list4 = kgr.list_random_values(4)
    list5 = [", recorded on", ", observed on"]
    list6 = kgr.list_random_dates(4)

    data = []
    for item1 in list1:
        for sig_prefix, sig_name in list2:
            for item3 in list3:
                for imput_num, query_num in list4:
                    for item5 in list5:
                        for input_date, query_date in list6:
                            sentence = f"{item1} {sig_name} {item3} {imput_num}{item5} {input_date}"
                            second_column = f"SELECT ?timestamp ?signalValue\nWHERE {{\n ?log a dbc:SignalLog ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:hasSimpleResult ?signalValue ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), '{query_date}') && ?signalValue < {query_num})\n}}\nORDER BY ?timestamp"
                            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

# 17d.2
def get_signal_value_smaller_than_2(kg: str):

    list1 = ["List", "Retrieve", "Get", "Show"]
    list2 = kgr.list_random_signals(kg, 4)
    list3 = ["values on"]
    list4 = kgr.list_random_dates(4)
    list5 = ["which are lower than", "that are smaller than"]
    list6 = kgr.list_random_values(4)

    data = []
    for item1 in list1:
        for sig_prefix, sig_name in list2:
            for item3 in list3:
                for input_date, query_date in list4:
                    for item5 in list5:
                        for input_num, query_num in list6:
                            sentence = f"{item1} {sig_name} {item3} {input_date} {item5} {input_num}"
                            second_column = f"SELECT ?signalValue\nWHERE {{\n ?log a dbc:SignalLog ;\n  sosa:observedProperty {sig_prefix}:{sig_name} ;\n  sosa:hasSimpleResult ?signalValue ;\n  sosa:resultTime ?timestamp .\n FILTER(STRSTARTS(STR(?timestamp), '{query_date}') && ?signalValue < {query_num})\n}}\nORDER BY ?timestamp"
                            data.append([sentence, second_column])
    
    df = pd.DataFrame(data, columns=['Sentence', 'Query'])
    return df

####################################################################################################################################################################################
####################################################################################################################################################################################

# List of functions
d_functions = [list_signal_measuring_kind, list_signals_of_message_1, list_signals_of_message_2, get_message_of_signal_1, get_message_of_signal_2, get_encoding_of_signal_1, get_encoding_of_signal_2, get_signals_targeting_ECU_1, get_signals_targeting_ECU_2,
get_decid_of_signal_1, get_decid_of_signal_2, get_platform_of_sensor_1, get_platform_of_sensor_2, get_hexids_on_platfrom_1, get_hexids_on_platfrom_2, get_rxnodes_of_sensor_1, get_rxnodes_of_sensor_2,
get_current_temp_of_signal_1, get_current_temp_of_signal_2, get_latest_messagelogs_on_platfrom_1, get_latest_messagelogs_on_platfrom_2, get_the_average_of_signal_on_date, get_the_max_of_signal_on_date,
get_the_mean_of_signal_from_date, get_sig_value_on_date_with_condition, get_signal_value_higher_than_1, get_signal_value_higher_than_2, get_signal_value_smaller_than_1]

d_functions_instances = [list_signals_of_message_1, list_signals_of_message_2, get_message_of_signal_1, get_message_of_signal_2, get_encoding_of_signal_1, get_encoding_of_signal_2, get_signals_targeting_ECU_1, get_signals_targeting_ECU_2,
get_decid_of_signal_1, get_decid_of_signal_2, get_platform_of_sensor_1, get_platform_of_sensor_2, get_hexids_on_platfrom_1, get_hexids_on_platfrom_2, get_rxnodes_of_sensor_1, get_rxnodes_of_sensor_2,
get_current_temp_of_signal_1, get_current_temp_of_signal_2, get_latest_messagelogs_on_platfrom_1, get_latest_messagelogs_on_platfrom_2, get_the_average_of_signal_on_date, get_the_max_of_signal_on_date,
get_the_mean_of_signal_from_date, get_sig_value_on_date_with_condition, get_signal_value_higher_than_1, get_signal_value_higher_than_2, get_signal_value_smaller_than_1]

d_functions_no_instances = [list_signal_measuring_kind]

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
    for func in d_functions_instances:
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

    for func in d_functions_no_instances:
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
