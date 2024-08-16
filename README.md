# Detect and Defence (D2) Framework
### Introduction
It is designed to detect Command and Control (C2) frameworks infection from prompt engineering on chatGPT4.\
This framework aims to give a simple interactive tool where users can send extracted CSV file from wireshark PCAP file.\
It uses several prompt engineering techniques as few-shot prompting, self-consitency and so on.
The prompt is fully available [here](https://github.com/RainMaker1707/blob/main/prompt/prompt.md)

### Extractor
The extractor used to have the CSV file at the right format is available [here](https://github.com/RainMaker1707/C2_prompt/blob/main/data/extractor.py).\
*TODO write an extractor or modify the actual extractor to simplify user extraction*

### How it works
### Usage
There is two ways to use the D2 framework.
- Use the customized chatGPT available [here](https://chatgpt.com/g/g-LXj2lXggp-d2-a-c2-framework-detector)
- You can create you own prompt following the steps explained in the section [Installation](#installation)

Once you are in the prompt, just send the CSV file with the appropriate columns and let the LLM works for you.

### Installation
*TODO*

### Advancements
For now the D2 frameworks is able to detect HTTP sessions and beacons of Sliver C2 framework using default configuration.

### Future works
- Work on a fictional C2 framework (Simple) to check if the prompt is able to work only with small documentation files.
- Work on secure communication (as HTTPS, mTLS, etc.).