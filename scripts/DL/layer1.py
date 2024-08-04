import argparse as arg
from os import listdir
import json
import pandas as pd
import ipaddress
import numpy as np
from random import randrange

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Masking
from sklearn.model_selection import train_test_split



# Global variable only for easier change
mode = "random_normal"
activ_fun = "softmax"
losses = "categorical_crossentropy"
protocols = {"HTTP": 1, "HTTPS":2, "DNS": 3, "MTLS": 4, "TCP": 5, "TLS": 6, "TLSv1.3": 7, "MDNS": 8}
next_int = 8
max_len = 0
safe_example = None
model_save_path = "/home/rainmaker/Desktop/C2_prompt/model/layer1.h5"


# It is obviously an ugly converted that need to be changed
def ip_to_int(col):
    ip_list = list()
    for ip in col:
        if ip is None: ip_list.append(-1)
        else:
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
            protocols[protocol] = len(protocols)+1
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
    global safe_example
    for dic in labels:
        infected = dic.get("frameworkName") in ["Sliver", "Mythic"]
        for inner_data in dic.get("data"):
            # TODO: drop title columns here
            # data.get(inner_data.get("filename")).drop()
            y.append(infected)
            if data.get(inner_data.get("filename")) is None:
                print(inner_data.get("filename"))
            x.append(data.get(inner_data.get("filename")))
            if infected == 0 and safe_example is None:
                safe_example = data.get(inner_data.get("filename"))
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
    try:
        max_len = max(len(seq) for seq in x)
    except Exception as e:
        print("ERROR: ", e)
        exit(1)
    padded_x = pad_sequences(x, maxlen=max_len, padding='post', dtype='float32')
    return train_test_split(padded_x, y, test_size=0.2, random_state=randrange(1, 100))


# source https://stackoverflow.com/questions/59339531/balanced-accuracy-score-in-tensorflow
def balanced_accuracy(y_true, y_pred):
    C = tf.math.confusion_matrix(y_true, y_pred)
    diag = tf.linalg.diag_part(C)
    true_num = tf.reduce_sum(C, axis=1)
    per_class = tf.math.divide_no_nan(tf.cast(diag, tf.float32), tf.cast(true_num, tf.float32))
    return tf.math.reduce_mean(per_class)


def config():
    tf.config.set_visible_devices([], "GPU") # No GPU in my laptop
    model = Sequential()
    model.add(Masking(mask_value=0.0, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[balanced_accuracy])
    return model




if __name__ == "__main__":
    parser = arg.ArgumentParser(prog="Layer1", description="Detect if the wireshark csv is infected or safe")
    parser.add_argument('path')
    parser.add_argument('labels')
    parser.add_argument('-o', '--output', required=False, type=str, default=model_save_path)
    parser.add_argument('-l', '--load', required=False, default=False, action='store_true')
    parser.add_argument('-rt', '--retrain', required=False, default=False, action='store_true')
    args = parser.parse_args()
    if(args.path[-1] != "/"): args.path += "/"
    if(args.labels[-1] != "/"): args.labels += "/"

    x_train, x_test, y_train, y_test  = preprocess(args)

    x_train = np.array(x_train)
    x_test = np.array(x_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    if args.load:
        model = tf.keras.models.load_model(args.output)
    elif args.retrain:
        model = tf.keras.models.load_model(args.output)
        model.fit(x_train, y_train, epochs=17, batch_size=16)
    else:
        model = config()
        model.fit(x_train, y_train, epochs=17, batch_size=16)
        loss, acc = model.evaluate(x_test, y_test)
        print(f'Accuracy: {acc},  Loss: {loss}')
    print("Predictions: ", np.array([True if e > .5 else False for e in model.predict(x_test)]))
    print("Test set:    ", y_test)
    model.save(args.output)
    
    exit(0)