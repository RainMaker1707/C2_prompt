You will use all the example files provided. All infected and all safe examples.
You have to detect pattern in the structure of the netflow and identify the labelled protocol associated to the most likely pattern you recognized.
The pattern recognized should be evaluated against all safe example pattern to ensure shared pattern exclusion.



You must compute the safe probability against the infected probability. You will then transfer this probability to the output task.

To check pattern you must check HTTP request URL and then use pyton to match any request that match these pattern:
- `((.+)?(\/)([a-zA-Z0-9]+)(\.woff|\.js|\.html|\.php|\.png))`

The following pattern want to match any HTTP query that use a extension used by Sliver by default.

Also use the number of requests for each protocol to determine the infection pattern.
For this you must count for each protocol the number of requests for each sequences.
A sequences has the same tuple (Source, Destination) or (Destination, Source).
For exemple if a packet rely to (Source=10.101.10.10, Destination=8.8.8.8) and another rely to (Source 8.8.8.8, Destination=10.101.10.10), they are part of the same sequence.

You have to compare sequences patterns between infected example and safe example to determine if the file provided by the user seems infected or not.