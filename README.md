# Detect and Defence (D2) Framework
### Introduction
It is designed to detect Command and Control (C2) frameworks infection from prompt engineering on chatGPT4.\
This framework aims to give a simple interactive tool where users can send extracted CSV file from wireshark PCAP file.\
It uses several prompt engineering techniques as few-shot prompting, self-consistency and so on.
The prompts are fully available [here](https://github.com/RainMaker1707/C2_prompt/tree/main/prompt/).\
The GPTchat is available [here](https://chatgpt.com/g/g-KAUp0QJSs-d2-from-doc).

### Extractor
The extractor used to have the CSV file at the right format is available [here](https://github.com/RainMaker1707/C2_prompt/blob/main/data/extractor.py).\
It automatically extract all .pcap files stored under `data/raw/` in `data/csv/` keeping the same path and file name.\
The extractor extract all packet, 
Usage: move on directory `cd C2_prompt/data` and then run `python3 extractor.py`.\
Options: optional `-t`, `--test` to limited extraction (1100 packets).

CSV has the following columns:
```json
{
    "Unnamed: 0" 
    "time" 
    "source"
    "destination"
    "protocol" 
    "length"
    "source_port"
    "destination_port"
    "request_method"
    "response_code"
    "request_uri"
    "data"
    "user_agent"
    "response_phrase"
    "content_type"
    "content_length"
}
```
The 8 last columns (from `request_method` to `content_length`) are `None` or absent if the protocol used is not HTTP. If the highest protocol is HTTP it is noted HTTP for any port.
HTTPS is only present when the TCP protocol is used on the port 443 (src or dst).
For the other protocol only the 

### How it works
The prompt use documentation files that are wrote in markdown. These files clearly explains the behavior of the C2 framework with example.
For now only a fictional C2, named Slimper and using HTTP, is used to test the process and make a proof of concept of the possible detection of active implants by an LLM.

