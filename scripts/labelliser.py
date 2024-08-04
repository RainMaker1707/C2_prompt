from os import listdir
import argparse as arg

counter= 0

class data_object():
    inner = dict()
    def __init__(self, filename, connectionType, protocol, custom, stager):
        global counter
        self.inner = {
            "ID": counter,
            "filename": filename,
            "connectionType": connectionType,
            "protocol": protocol,
            "custom" : custom,
            "stager": stager
        }
        counter += 1




def labelize(path):
    labels = list()
    for file in listdir(path):
        labels.append(data_object(path+file, "None", "None", 0, 0).inner)
    return labels


if __name__ == "__main__":
    parser = arg.ArgumentParser(prog="Layer1", description="Detect if the wireshark csv is infected or safe")
    parser.add_argument('path')
    args = parser.parse_args()
    if args.path[-1] != '/': args.path += '/'
    labels = labelize(args.path)
    print(labels)