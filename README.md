
# Homomorphic-based Voting System

a privacy preserving voting system, in 
which each voter could vote without disclosing which candidate is voted for. The protocol 
which is proposed will work with unlimited voters and candidates. Our protocol will make use 
of the partially homomorphic encryption RSA system since it is multiplicative homomorphic 
encryption scheme. In addition to prime integer factorization property to count the votes.
## Working Principle :

![alt text](https://github.com/Uzax/Homomorphic_Voting_System/blob/main/images/Steps.png)

## Protocol : 
![alt text](https://github.com/Uzax/Homomorphic_Voting_System/blob/main/images/Protocol.png)

## How to run the program:

```bash
1. Add RSA_enc.py in both UntrustedS.py, DeclarationS.py, and Client.py directories
2. Download pycryptodome library using
	pip install pycryptodome
3. Run UntrustedS.py and DeclarationS.py first
4. while UntrustedS.py and DeclarationS.py both are running run client.py 3 times each run add a vote.
	Each vote should be a number representing the candidate as prompted
5.Observe the output in DeclarationS.py

```
  
