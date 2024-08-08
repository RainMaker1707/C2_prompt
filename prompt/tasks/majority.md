# Majority vote and final output
A majority vote is a process where you will compare answers in a certain way to decide which is the most represented.
You must firstly compare if the answer is infected or safe. Then if a majority of answers (4) represent infected then the final output will be infected. If the majority of answers (4) represent safe then the final output will be safe.
In the case of infected only, You must do a second majority vote between protocols to choose the final one. 
The final probability is the average of all probability of this answer represented in the forst majority vote (infected or safe).
Let's say you have 7 objects like these one to compare.
```md
# Device seems infected
- **Suspected Framework** Sliver
- **Suspected Protocol** HTTP
- **Probability** 66.4%
```
```md
# Device seems infected
- **Suspected Framework** Sliver
- **Suspected Protocol** HTTP
- **Probability** 89.7%
```
```md
# Device seems safe
- **Probability** 78.1%
```
```md
# Device seems safe
- **Probability** 82.4%
```
```md
# Device seems infected
- **Suspected Framework** Sliver
- **Suspected Protocol** MTLS
- **Probability** 71.7%
```
```md
# Device seems infected
- **Suspected Framework** Sliver
- **Suspected Protocol** HTTP
- **Probability** 79.3%
```
```md
# Device seems safe
- **Probability** 67%
```
The majority say it is infected as there is 4 answers that say it is infected. The 4 answers have different protocols. 3 of them are HTTP one is MTLS. The final probability is (79.3% + 71.7% + 89.7% + 66.4%)/4 = 76.8%
From the constraints described above the final output will be:
```md
# Device seems infected
- **Suspected Framework** Sliver
- **Suspected Protocol** HTTP
- **Probability** 76.8%
```
