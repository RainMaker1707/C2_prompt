# C2_prompt
This repository contains documents, scripts and textual prompt to make a GPT4 prompt able to detect C2 frameworks infection and provide appropriate defense rules against this threat


## Introduction

## Repository organisation

## Iterations
- **I0** Prompt that uses raw pcap data to detect one or two types of sliver implant use
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
        - [ ] RAG
        - [ ] ...
    - raw data detection
        - [ ] http
        - [ ] https
        - [x] mtls
        - [ ] dns
    - transformed data detection
        - [ ] http
        - [ ] https
        - [ ] mtls
        - [ ] dns
    - C2 framework detection
        - [ ] Sliver
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
        - [ ] RTFC
        - [x] Self-consistency
        - [ ] RAG
        - [ ] ...
    - raw data detection
        - [ ] http
        - [ ] https
        - [ ] mtls
        - [ ] dns
    - transformed data detection
        - [ ] http
        - [ ] https
        - [ ] mtls
        - [ ] dns
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

    ## Problem
    First problem encountered: the environement where run my prompt cannot install or use pyshark. So it cannot analyse pcap files directly.
    I have to change a bit my approach to use relevant information directly with pyshark and not directly pcap send to the prompt by users.
    It would make the prompt able to answer question.

    As prompt environement has no internet connection it cannot directly install the pyshark module required.
    So I will probably try to directly embed the pyshark files in the prompt knowledge to let users send pcap files directly.
