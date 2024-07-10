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


## Work done
- Gather data for basic connection
    - sessions
        - [ ] http
        - [ ] https
        - [x] mtls
        - [ ] dns
    - beacons 
        - [ ] http
        - [ ] https
        - [ ] mtls
        - [ ] dns
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


    ## Explanation
        TODO