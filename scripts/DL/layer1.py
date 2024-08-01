import argparse as arg
from os import listdir
import json
import pandas as pd
import ipaddress
import numpy as np


import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Masking
from sklearn.model_selection import train_test_split



# Global variable only for easier change
mode = "random_normal"
activ_fun = "softmax"
losses = "categorical_crossentropy"
protocols = {"HTTP": 0, "HTTPS":1, "DNS": 2, "MTLS": 3, "TCP": 4, "TLS": 5, "TLSv1.3": 6, "MDNS": 7}
next_int = 8
max_len = 0


# It is obviously an ugly converted that need to be changed
def ip_to_int(col):
    ip_list = list()
    for ip in col:
        try:
            ip_list.append(int(ipaddress.IPv4Address(ip)))
        except:
            try:
                ip_list.append(int(ipaddress.IPv6Address(ip)))
            except:
                ip_list.append(0)    
    return pd.Series(data=ip_list)


def protocol_to_int(col):
    protocol_list = list()
    for protocol in col:
        if protocol not in protocols:
            protocols[protocol] = len(protocols)
        protocol_list.append(protocols.get(protocol))
    return pd.Series(data=protocol_list)



def load_data(data_path):
    files_dict = dict() # will contains a list of all files in the data directory without the parents directories
    # key = filepath, value = csv read with pandas
    dirs = listdir(data_path)
    for directory in dirs:
        directory += "/"
        files = listdir(data_path+directory)
        for file in files:
            if "." in file: 
                files_dict[data_path+directory+file] = pd.read_csv(data_path+directory+file)
                files_dict.get(data_path+directory+file)["Source"] = ip_to_int(files_dict.get(data_path+directory+file)["Source"])
                files_dict.get(data_path+directory+file)["Destination"] = ip_to_int(files_dict.get(data_path+directory+file)["Destination"])
                files_dict.get(data_path+directory+file)["Protocol"] = protocol_to_int(files_dict.get(data_path+directory+file)["Protocol"])    
            else:
                file += "/"
                for subfile in listdir(data_path+directory+file):
                    files_dict[data_path+directory+file+subfile] = pd.read_csv(data_path+directory+file+subfile)
                    files_dict.get(data_path+directory+file+subfile)["Source"] = ip_to_int(files_dict.get(data_path+directory+file+subfile)["Source"])
                    files_dict.get(data_path+directory+file+subfile)["Destination"] = ip_to_int(files_dict.get(data_path+directory+file+subfile)["Destination"])
                    files_dict.get(data_path+directory+file+subfile)["Protocol"] = protocol_to_int(files_dict.get(data_path+directory+file+subfile)["Protocol"])
    return files_dict


def load_label(labels_path, data_path):
    labels = list() # will contains a list of all label files with corrected filename field.
    dirs = listdir(labels_path)
    for file_path in dirs:
        with open(labels_path + file_path, 'r') as file:
            temp = json.loads(file.read())
            for o in temp.get("data"):
                # Checker to replace the label filename with the appropriate one
                if "/mnt/data/data/" == o.get("filename")[0:15]:
                    o["filename"] = data_path + o.get("filename")[15:]
            labels.append(temp)
    return labels


def labelize_data(data, labels):
    labellized_data = dict() # key = filename, value = infected or safe
    x = list()
    y = list()
    for dic in labels:
        infected = dic.get("frameworkName") in ["Sliver", "Mythic"]
        for inner_data in dic.get("data"):
            y.append(infected)
            x.append(data.get(inner_data.get("filename")))
    return x, y


def split_data(x, y):
    x_train, y_train, x_test, y_test = [], [], [], []
    return x_train, y_train, x_test, y_test


def preprocess(args):
    data = load_data(args.path)
    for key in data.keys():
        data.get(key).drop(["No.", "Time", "Info"], axis='columns', inplace=True) # Info temporarily dropped, need tokenisation to be used
    labels = load_label(args.labels, args.path)
    x, y = labelize_data(data, labels)
    max_len = max(len(seq) for seq in x)
    padded_x = pad_sequences(x, maxlen=max_len, padding='post', dtype='float32')
    return train_test_split(padded_x, y, test_size=0.2, random_state=42)


def config():
    tf.config.set_visible_devices([], "GPU") # No GPU in my laptop
    model = Sequential()
    model.add(Masking(mask_value=0.0, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


if __name__ == "__main__":
    parser = arg.ArgumentParser(prog="Layer1", description="Detect if the wireshark csv is infected or safe")
    parser.add_argument('path')
    parser.add_argument('labels')
    args = parser.parse_args()
    if(args.path[-1] != "/"): args.path += "/"
    if(args.labels[-1] != "/"): args.labels += "/"

    # from here both paths are needed otherwise the program throw an error.
    x_train, x_test, y_train, y_test  = preprocess(args)
    x_train = np.array(x_train)
    x_test = np.array(x_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    
    model = config()
    model.fit(x_train, y_train, epochs=100, batch_size=32)    
    
    loss, acc = model.evaluate(x_test, y_test)

    model.save_weights("/home/rainmaker/Desktop/C2_prompt/model/layer1.weights.h5")
    print(f'Accuracy: {acc},  Loss: {loss}')
    exit(0)