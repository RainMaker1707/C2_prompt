from pyshark import FileCapture 
from os import listdir
import pandas as pd
from argparse import ArgumentParser


path_to_raw = "raw/"
path_to_csv = "csv/"


test = False

def extract(path):
    capture = FileCapture(path, keep_packets=False)
    features = list()
    counter = 0
    for packet in capture:
        feature = {
            "time": packet.sniff_timestamp,
            "source": 0,
            "destination": 0,
            "protocol": packet.transport_layer,
            "length": packet.length,
            "source_port": 0,
            "destination_port": 0,
            "request_method": None,
            "response_code": None,
            "request_uri": None,
            "data": None,
            "user_agent": None,
        }
        if hasattr(packet, "ip"):
            feature["source"] = packet.ip.src
            feature["destination"] = packet.ip.dst
        elif hasattr(packet, "ipv6"):
            feature["source"] = packet.ipv6.src
            feature["destination"] = packet.ipv6.dst
        if hasattr(packet, 'tcp'):
            feature["source_port"] = packet.tcp.srcport
            feature["destination_port"] = packet.tcp.dstport
        elif hasattr(packet, 'udp'):
            feature["source_port"] = packet.udp.srcport
            feature["destination_port"] = packet.udp.dstport
        if hasattr(packet, 'http'):
            feature["protocol"] = "HTTP"
            """
            '', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattr__', '__getattribute__',
            '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
            '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
            '__slots__', '__str__', '__subclasshook__', '_all_fields', '_field_prefix',
            '_get_all_field_lines', '_get_all_fields_with_alternates', '_get_field_or_layer_repr',
            '_get_field_repr', '_layer_name', '_pretty_print_layer_fields', '_sanitize_field_name',
            '_ws_expert', '_ws_expert_group', '_ws_expert_message', '_ws_expert_severity',
            'accept_encoding', 'chat', 'content_length', 'content_length_header', 'data',
            'data_data', 'data_len', 'field_names', 'file_data', 'get', 'get_field',
            'get_field_by_showname', 'get_field_value', 'has_field', 'host', 'layer_name',
            'pretty_print', 'raw_mode', 'request', 'request_full_uri', 'request_line',
            'request_method', 'request_number', 'request_uri', 'request_uri_path',
            'request_uri_query', 'request_uri_query_parameter', 'request_version', 'user_agent']
            """
            feature["request_method"] = packet.http.request_method if hasattr(packet.http, 'request_method') else None
            feature["request_uri"] = packet.http.request_uri if hasattr(packet.http, 'request_uri') else None
            feature["user_agent"] = packet.http.user_agent if hasattr(packet.http, 'user_agent') else None
            # The following line don't work correct it to get the data content in UTF8
            feature["response_code"] = packet.http.response_code if hasattr(packet.http, "response_code") else None
            feature["response_phrase"] = packet.http.response_phrase if hasattr(packet.http, "response_type") else None
            feature["content_type"] = packet.http.content_type if hasattr(packet.http, "content_type") else None
            feature["content_length"] = int(packet.http.content_length) if hasattr(packet.http, "content_length") else None
            if feature["content_length"] is None or feature["content_length"] < 1000:
                feature["data"] = packet.http.file_data.replace("\n", "").replace("+", "") if hasattr(packet.http, "file_data") else None

        if hasattr(packet, 'tcp') and (packet.tcp.srcport == "443" or packet.tcp.dstport == "443"):
            feature["protocol"] = "HTTPS"
        features.append(feature)
        if test and counter > 1100: break
        counter += 1
    capture.close()
    return pd.DataFrame(features)


def process(path):
    if path[-1] != '/': path += '/'
    for file in listdir(path):
        df = extract(path+file)
        df.to_csv(path_to_csv+path[4:]+file[:-5]+".csv")
        print("Written " + path_to_csv+path[4:]+file[:-5]+".csv")


def loop():
    for dr in listdir(path_to_raw):
        if dr == "safe":
            process(path_to_raw+dr)
        else:
            for subdir in listdir(path_to_raw+dr+"/"):
                process(path_to_raw+dr+"/"+subdir)

if __name__ == "__main__":
    from time import sleep
    parser = ArgumentParser()
    parser.add_argument("-t", "--test", action='store_true')
    parser.add_argument("-d", "--dir", type=str)
    

    args = parser.parse_args()
    if args.test: 
        test = True
    if args.dir:
        if args.dir[-1] != "/":
            args.dir += "/"
        process(path_to_raw+args.dir)
    else:
        loop()