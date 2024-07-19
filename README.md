# C2_prompt
This repository contains documents, scripts and textual prompt to make a GPT4 prompt able to detect C2 frameworks infection and provide appropriate defense rules against this threat



## Today
- Improve user file analyzes.
- Works on prompt V3 which will use csv packets dissection from wireshark.


## Delayed
- Maybe V3 work with sklearn script to help the LLM to decide.
- PromptV3.1 using plain text packets dissection from wireshark.
- Gather and forge more data.


## TODO
- Compare the prompt V3 and V3.1 to understand how data format affect the prompt result.
- Reverse engineer some detection prompt already made to understand the prompt logic implemented.
- Implement analyze script in python.




## Introduction

This project aims to develop a GPT4 prompt able to detect automatically from pcap files the infection of a C2 framework.
The three first parts focus on the SLiver C2 framework.

- [x] The first part is to develop a basic prompt that can use raw data in pcap file by generating data and use only RTF and self-consistency
    - Update which is not possible, only binary comparisons are possible and it is not really what we want here
- [ ] The second part will be to develop a feature extractor and extract these data from all data files generated
- [ ] The third part will be to apply more prompt techniques to the actual prompt
- [ ] The last part will be to add data for more C2 frmeworks

After this prompt about detection I will made a prompt that can generate efficient defense rules against the infection the user faces.
- [ ] ...


Secondly, this project aims to provide efficient defense rules for framework as Yara or Snort.
Update for this part will come soon.


## Repository organisation
- **converted-data** contains all the converted data used by the prompt. Different versions of the prompt may use different data format.
- **data** contains raw data as pcap file containing safe and infected netflow.\ It has been sniffed from VM on host only conenction with static IP.
- **labels** contains json files that labellizes the netflo from converted-data. It will help the LLM to understand on what rley each examples it is fed with. 
- **prompt** contains all files related to the instructions given to the LLM for the tasking. Tasks directory contains others part of the part that are split from the main one to improve readability, maintanibility and modularity.
- **scripts** contains the scripts that may be used by some versions of the prompt. Different version may use different scripts or none of them.
- **test-data** contains data in different format (as the converted-data directory) to test the prompt efficency.
- **versions** *available soon* contains all the prompt versions file needed to make your prompt at this state. For example prompt V1 used data.zip and labels.zip + its instructions stored in prompt.md.

## Iterations
- __*I0*__ Prompt that uses raw pcap data to detect one or two types of sliver implant use 
    (NOT POSSIBLE as the env cannot install pyshark, only binary comparisons are possible)
- __*I1*__ Prompt that uses raw pcap data to detect all types of basic connections with sliver implant
    (As the I0 using raw data is too limitating, you only can do binary comparison which is not what we want here)
- __*I2*__ Prompt that uses pcap data transformation to detect all types of basic connections with sliver implant
    We are here and now the prompt use packet dissection as plain text or csv depending on version used. (V3 use csv, V3.1 use plain text)
- **I3** Add detection of custom sliver implant (stagers for example)
- **I4** Add defense rules creation 
    Will need new knowledge, new sub task, improved prompt ...
- **I5** Add basic connection of others C2 frameworks (as mythic for example)
- ...


## Current work
- Data transformation
    - [x] basic extractor
    - [x] wireshark converter to csv
    - [ ] wireshark converter to plain text
    - advanced techniques
        - [ ] ...
- Prompt
    - techniques used
        - [x] RTFC
        - [x] Self-consistency
        - [x] Prompt Chaining
        - [x] Splitted prompt file
        - [ ] RAG
        - [ ] ...
    - C2 f  ramework detection
        - [x] Sliver
        - [ ] Mythic
        - [ ] ...
    - Defense rules
        - [ ] Snort
        - [ ] Yara
        - [ ] ...
    - Versions
        - [x] 1: Raw data  ❌
        - [x] 2: Use pyshark pcap to txt packet extractor ❌
        - [x] 3: Using csv dissection 🦾
        - [ ] 3.1: Using plain text dissection

## Work done
- Gather data for basic connection
    - sessions
        - [x] http
        - [x] https
        - [x] mtls
        - [ ] dns
    - beacons 
        - [x] http
        - [x] https
        - [x] mtls
        - [ ] dns
- Data transformation
    - [x] basic extractor
    - [x] wireshark converter to csv
    - [ ] wireshark converter to plain text
    - advanced techniques
        - [ ] ...
- Prompt
    - techniques used
        - [x] RTFC
        - [x] Self-consistency
        - [x] Prompt Chaining
        - [ ] Splitted prompt file
        - [ ] RAG
        - [ ] ...
    - C2 framework detection
        - [ ] Sliver
        - [ ] Mythic
        - [ ] ...
    - Defense rules
        - [ ] Snort
        - [ ] Yara
        - [ ] ...
    - Versions
        - [x] 1: Raw data  ❌
        - [x] 2: Use pyshark pcap to txt packet extractor ❌
        - [ ] 3: Using csv dissection 🦾
        - [ ] 3.1: Using plain text dissection

## Explanation
- For now the prompt is able to detect take as input a plain text wireshark packets dissection netflow and analyze it with its own code creation which is not optimal.

## Label template
Each framework has its json file(s) labelling the examples related.
json files format:
```json
{
    "frameworkName": "Sliver",
    "data": [
        {
            "ID": "<random id>",
            "filename": "<filepath>"
            "connectionType": "<connection used> (session or beacon for sliver, None for safe)" 
            "protocol": "<protocol used> (None for safe)"
            "stager": "<0 false 1 true (true if stager used)>"
            "custom": "<0 false 1 true (true if custom used)>"
        },
        {
            "ID": 1,
            "filename": "converted-data/sessions/mtls/session_mtls_open-after_then_close.txt",
            "connectionType": "session",
            "protocol": "mtls",
            "stager": 0,
            "custom": 0
        },
        ...
    ]
}
```

Each file related has its data object in a json file.





## Problem
First problem encountered: the environement where run my prompt cannot install or use pyshark. So it cannot analyse pcap files directly.\
I have to change a bit my approach to use relevant information directly with pyshark and not directly pcap send to the prompt by users.\
It would make the prompt able to answer question.

As prompt environement has no internet connection it cannot directly install the pyshark module required.\
So I will probably try to directly embed the pyshark files in the prompt knowledge to let users send pcap files directly.\

**A basic extractor has been written in python but I struggle to use pyshark inside the environement of the GPT4 prompt.**
For now the prompt will provide a basic pcap to txt python extractor. User will have to run it locally and then provides the converted file to GPT.
```python
import pyshark

filepath = "file/to/your/file"

with open(filepath, "w") as f:
    for packet in pyshark.FileCapture(filepath[0:-5] + ".txt"):
        f.write(str(packet))
        f.write("-"*17+"\n"+"-"*17) # Packet separation (not really helps the LLM but improves human readability)
```

Secondly the prompt give to much informations about how it proceeds to give the answer. I'll see to fix this later.
Thirdly the prompt keep to generate code to analyze text converted file instead of doing it by text only.




## Remarks to note
- For now only non noisy data are available. Noisy data (low, medium and high noise) will be available soon.
- For the first part example data focus on sessions. Beacons data will be available soon.
- DNS seems to not connect in sessions mode. __*Update:*__ on beacon mode it doesn't seem to work too.
- The port 31337 (Elite) is only open when a multiplayer job is requested
- Port used to handle job as DNS or HTTP are the official one (53, 80, 443, ...)
- When an idle HTTP or HTTPS connection is active, much TCP packet are exchanged.
- The LLM build a code to assess if the provided file represent an infected pattern or not. I then think it will probably be better to create a micro sklearn algorithm that can detect that before. As we will have more control on parameters used.





# V1
Use raw pcap data.\
As GPT4 can't read these data it simply doesn't work.\
You may ask to do binary comparison but it will not really help.
The actual prompt stored in V1 is more like a V1.5 hybrid between the V1 and its evolution.
It will not be available in the versions directory as it don't work and the prompt was changed.

# V2
Use pcap with handmade custom basic pcap to txt converter python script `scripts/converter.py`
Results were too inconsistent to be used.

## FSM inside tasking

```
0 ----> 1 ----> 2 ----> 3 ----> 4
 \_____/                 \_____/    
```

- **Task 0** check the input when the input is converted it goes to the task 1.
- **Task 1** check the format of the txt file if well formatted go to step 2, else goto step 0.
- **Task 2** performs examples analyzes. and then go to task 3.
- **Task 3** performs an analyzes on the user converted file. Then goto task 4.
- **Task 4** Generate an answer and save it.
    - Then check if it has 7 answers. 
        - If yes make majority vote and generate the final answer.
        - If no go to task 3.

## Why left this idea
The idea was to use basic packet extractor which only write to text files the packet extraction from pyshark.\
This was not really suitable as it is done mannually and can be time consumming to do it for several data.\


# V3
TODO

