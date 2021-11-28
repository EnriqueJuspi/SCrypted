# Private Set Intersection (PSI) with Diffie-Hellman

Implementing a Private Set Intersection protocol with Diffie-Hellman in Python.

The protocol consists of two parties, i.e., a Client and a Server. Both the client and the server have a set of numbers, where both the client and server can associate each number to a certain data. The set of datas used are not nessecarily need to be consist of numbers. In general, you can use any type of data sets as long as the hashing is done properly, the calculation and algorithm should able to take care of the rest.

In the implementation, the client wants to learn the intersection of the two sets without revealing any entries outside the intersection to the server. The server wants to inform the client about common entries without revealing to the client the rest of his entries. Both the client and the server will agreed to use a prime number to help with hashing and creating keys for encryption or decryption.


### Development
In terms of development and Implementation, Private Set Intersectoin in itself isn't very secure. It is possible to use pure-computational power to try all the combination of set of numbers available. Thus, making it a requirement to have another layer of encryption in a form of Diffie-Hellman key exchange, which guarantee a secure data exchange without having fear of middle man attack or other form of unsecure information being look into. 

In addition, since the set of numbers that are going to be used seems predictable, it is best to have another layer of security in a form of md5 hashing with addition of mod prime number to ensure it is one-way encryption, meaning you couldn't get the actual message through using the encrypted version.


### Requirements
---
* Any Python IDE of your choice (the code was developed and tested with Visual Studio Code with Python 3.9.2)

### Building and Testing the Project
1. Clone a copy of the main git repository or download the git repository on https://github.com/EnriqueJuspi/SCrypted.
      ```
	    git clone --recursive git://github.com/EnriqueJuspi/SCrypted
2. Open and Run PSI_Diffie-Hellman.py
Note : The inputs hard-coded to help with testing. You can edit the inputs by changing the variable value or uncomment remove "#" in Line 6, 14, and 98.
(Variables : prime, client_key, server_key, client_set, and server_set)


### How the Protocol Works ###
---
The client and server agrees on a large prime number (ex: 199,211,223,227,...) for hashing and processing sets. Both each get their own private key for encryption and decryption of sets. After that, the client and server computes the MD5 hash functions of each number in sets provided. Next, they both encrypts the hashed set of numbers using their own private key making a public key. The client and server then exchange these public key, which can be used to get secret sets of value.

The client and server both takes the other's public key and using their own key to make a secret sets of value which can either common or not, depending on the initial sets of number. The secret sets of value belonged to the server will then be send to the client, for the use of intersection. In the intersection, both secret sets of value are intersected and using the intersected value, the client will be able to get the intended set of results. This intended set of results is based on the initial set of numbers of the client.
