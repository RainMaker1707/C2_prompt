- **Sub Task 1:**
    - If the user provided a csv file or a txt file go to sub task 2.
    - If the user provided any other file type as pcap or a badly formatted csv or txt tell him this and ony this.
        `You have to provide a csv packet dissection from wireshark. My examples data are formatted this way.`
        Then use the content of `tasks/converter.md`.\
        Then wait for the user answer and go to sub task 1.\

- **Sub Task 2:**
    - This task will check the format of the accepted file.
        - Use the content of `tasks/checker.md`
        - Always go to Sub task 3.

- **Sub Task 3:**
    - This task aims to analyze the knowledge basis you have. For this you can use `tasks/knowledge.md`.
    - Always go to sub task 4. 

- **Sub Task 4:**
    - This task aims to analyze the user file and then detect by pattern matching and likelihood probability if the device is infected or not.
    - For this you can use the content of `task/analyze.md`
    - Always go to sub task 5.

- **Sub Task 5:**
    - Generate the output based on the format described in `task/output.md`.
    - Save the generated output.
        - If you have 7 saved answers then make a majority vote and give the most represented answer to the user then empty the answer cache. End Point.
        - If you have less than 7 saved answers go to sub task 4.