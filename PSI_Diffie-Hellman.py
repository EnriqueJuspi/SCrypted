import hashlib

def main():
    #Private Keys for client and server:
    client_key = 5      #client_key set to 3 for testing
    #client_key = int(input("Client key: "))
    while client_key <= 1:
        #Error message
        print("Key must be greater than 1! Try again")
        #Ask for input again
        client_key = int(input("Client key: "))

    server_key = 7      #server_key set to 3 for testing
    #server_key = int(input("Server key: "))
    while server_key <= 1:
        #Error message
        print("Key must be greater than 1! Try again")
        #Ask for input again
        server_key = int(input("Server key: "))
    print("Client key :", client_key)
    print("Server key :", server_key, "\n")

    #Client and Server set
    print("Loading Client and Server Set")
    client_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    client_set1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    server_set = [1, 2, 3, 4, 5, 10, 11, 12, 13]
    print("Client set: ", client_set)
    print("Server set: ", server_set, "\n")

    #Hashing Client and Server set
    print("Hashing Client and Server Set")
    hashed_client_set = client_set
    hashed_server_set = server_set
    md5_mod_p(hashed_client_set) 
    md5_mod_p(hashed_server_set)
    print("Hashed client set: ",hashed_client_set)
    print("Hashed server set: ",hashed_server_set,"\n")

    #Public Client and Server Key
    print("Create and Sending Public key")
    public_client_key = hashed_client_set
    public_server_key = hashed_server_set
    public_key(client_key, public_client_key)
    public_key(server_key, public_server_key)
    print("Public client key: ",public_client_key)
    print("Public server key: ",public_server_key,"\n")

    #Server's Secret Value
    print("Sending Server Secret Value to Client for Intersection")
    client_secret_value = public_server_key
    server_secret_value = public_client_key
    public_key(client_key, client_secret_value)
    public_key(server_key, server_secret_value)
    print("Client Secret Value :", client_secret_value)
    print("Server Secret Value :", server_secret_value, "\n")

    #Secret Key Intersection and Result
    secret_key_intersection = intersection(client_secret_value,server_secret_value)
    result_intersection = secret_key_intersection
    print("Secret Key Intersection :",secret_key_intersection)
    for j in range(0,len(secret_key_intersection)):
        for k in range(0,len(server_secret_value)):
            if secret_key_intersection[j] == server_secret_value[k]:
                result_intersection[k] = client_set1[k]
    print("Result Intersection :", result_intersection)

def prime_check(num):
    #Check if number is Prime
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

def intersection(lst1, lst2):
    #Get intersection of two list
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def md5_mod_p(set):
    #hash md5 the set of numbers and mod p
    for i in range(0,len(set)):
        result = hashlib.md5(str(set[i]).encode())
        digest = result.hexdigest()
        number = int(digest, 16)
        set[i] = number % prime

def public_key(private_key,set):
    #Get public key of set using private key
    for i in range(0,len(set)):
        set[i] = (set[i]**private_key) % prime

if __name__ == "__main__":
    #Ask for Prime Number for client and server and check input
    #p needs to be a large prime number
    print("Prime need to be a large prime number (ex: 199,211,223,227,...) ")
    prime = 199     #prime set to large prime number 199 for testing
    #prime = int(input("Prime number: "))
    p_prime = prime_check(prime)
    while p_prime == False :
        #Error message
        if p_prime == False:
            print(str(prime) +" is not a Prime number! Try again")
        #Ask for input again
        prime = int(input("Prime number: "))
        p_prime = prime_check(prime)
    print("Client and Server agree on a large prime number :", prime,"\n")
    main()