# C2_prompt
This repository contains documents, scripts and textual prompt to make a GPT4 prompt able to detect C2 frameworks infection and provide appropriate defense rules against this threat


## Introduction

This project aims to develop a GPT4 prompt able to detect automatically from pcap files the infection of a C2 framework.
The three first parts focus on the SLiver C2 framework.

- [x] The first part is to develop a basic prompt that can use raw data in pcap file by generating data and use only RTF and self-consistency
    - Update which is not possible, only binary comparisons are possible and it is not really what we want here
- [ ] The second part will be to develop a feature extractor and extract these data from all data files generated
- [ ] The third part will be to apply more prompt techniques to the actual prompt
- [ ] The last part will be to add data for more C2 frmeworks


Secondly, this project aims to provide efficient defense rules for framework as Yara or Snort.
Update for this part will come soon.


## Repository organisation

## Iterations
- **I0** Prompt that uses raw pcap data to detect one or two types of sliver implant use (NOT POSSIBLE as the env cannot install pyshark, only binary comparisons are possible)
- **I1** Prompt that uses raw pcap data to detect all types of basic connections with sliver implant
- **I2** Prompt that uses pcap data transformation to detect all types of basic connections with sliver implant
- **I3** Add detection of custom sliver implant (stagers for example)
- **I4** Add basic connection of others C2 frameworks (as mythic for example)
- ...


## Current work
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
    - advanced techniques
        - [ ] ...
- Prompt
    - techniques used
        - [x] RTFC
        - [x] Self-consistency
        - [x] ReACT
        - [ ] RAG
        - [ ] ...
    - C2 framework detection
        - [x] Sliver
        - [ ] Mythic
        - [ ] ...
    - Defense rules
        - [ ] Snort
        - [ ] Yara
        - [ ] ...

## Work done
- Gather data for basic connection
    - sessions
        - [x] http
        - [x] https
        - [x] mtls
        - [ ] dns
    - beacons 
        - [ ] http
        - [ ] https
        - [ ] mtls
        - [ ] dns
- Data transformation
    - [x] basic extractor
    - advanced techniques
        - [ ] ...
- Prompt
    - techniques used
        - [x] RTFC
        - [x] Self-consistency
        - [ ] ReACT
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

    ## Explanation
        TODO

    ## Label template
        Each framework has its json file(s) labelling the examples related.
        json files format:
        ```json
        {
            "frameworkName": "Sliver",
            "data": [
                {
                    "ID": random id,
                    "filename": filepath
                    "connectionType": <connection used> (session or beacon for sliver) 
                    "protocol": <protocol used>
                    "stager": <0 false 1 true (true if stager used)>
                    "custom": <0 false 1 true (true if custom used)>
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
    First problem encountered: the environement where run my prompt cannot install or use pyshark. So it cannot analyse pcap files directly.
    I have to change a bit my approach to use relevant information directly with pyshark and not directly pcap send to the prompt by users.
    It would make the prompt able to answer question.

    As prompt environement has no internet connection it cannot directly install the pyshark module required.
    So I will probably try to directly embed the pyshark files in the prompt knowledge to let users send pcap files directly.

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




    ## Remarks to note
    - For now only non noisy data are available. Noisy data (low, medium and high noise) will be available soon.
    - For the first part example data focus on sessions. Beacons data will be available soon.
    - DNS seems to not connect in sessions mode.
    - The port 31337 (Elite) is only open when a multiplayer job is requested
    - Port used to handle job as DNS or HTTP are the official one (43, 80, ...)
    - When an idle HTTP or HTTPS connection is active, much TCP packet are exchanged.

