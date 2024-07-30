# C2_prompt
This repository contains documents, scripts and textual prompt to make a GPT4 prompt able to detect C2 frameworks infection and provide appropriate defense rules against this threat


It is a current work that can be updated any time. This README will provide information about the state of the project.\
Versions will be labelled in github to keep traces of the different versions and compare results difference.

The precedent version of this README was more a Trello that will be soon available here too.\
To keep the README simple only explanations on versions and how it works will be here.\
The old README is still available in this repository `oldREADME.md`.

Feel free to open an issue or contact me in GitHub for more informations.




# V0
- No analyze explanation
- Give good results on example data (several HTTP sessions) and test data (one HTTP session)
- No help menu

This first usable version uses `Custom GPT4 assistant` and is available [here](https://chatgpt.com/g/g-LXj2lXggp-d2-a-c2-framework-detector).\
This assistant uses verbosity features that can be specified with V= in your first message.\
It uses also an FSM like described in `prompt/tasks/FSM.md`.\

As there is no analyze specified the LLM choose the most appropriate on its own to compute the result. This will be corrected soon.\
Verbosity value may be ignored by the LLM, I don't know why for now.

This version as been tested on HTTP session and it is the first version that detect an infection in not seen data.\
This version seems to provide good results and consistency on Sliver HTTP session detection.


# V1 
The next version will use 4 layers.
1. **Machine Learning classifier:** Detect if the file represent safe or infected device.
2. **Machine Learning classifier:** Detect the protocol used in case of infection.
3. **Machine Learning classifier:** Provide efficient rulesto protect against the threat detected.
4. **ChatGPT 4 answers:** Provide a human readable answer where it say the infection result and if needed the appropriate defense rules.

For now I will work on the point 1, and eventually make a release where there will be only 2 layer (1 and 4).\
This will be the v0.2.0-alpha.

When this is working, I will make the layer 2 and add it in the release v0.2.1-alpha.

Finally I will make the layer 3 that create defense rules for ONE framework as yara or snort (to define at the moment).
Then the final release of this part will be the v1.0.0-prod

For the next iteration (the V2), I will add other defense framework on the third layer to extend the defense possibility of this tools.


# Currently
- V1 layer 1: ML classifier for infection detection.

