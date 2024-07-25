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
- Give good results on example data
- Will be tested against data not on example set today.
- No help menu, no

This first usable version uses `Custom GPT4 assistant` and is available [here](https://chatgpt.com/g/g-LXj2lXggp-d2-a-c2-framework-detector).\
This assistant uses verbosity features that can be specified with V= in your first message.\
It uses also an FSM like described in `prompt/tasks/FSM.md`.\

As there is no analyze specified the LLM choose the most appropriate on its own to compute the result. This will be corrected soon.\
Verbosity value may be ignored by the LLM, I don't know why for now.




# Next step
- Go on the analyze part.
- Gather and forge more data to feed examples.
- Improve results.

