import requests as req
from hashlib import md5

#Function defined to do the calculation of the checksum
def md5sum(fname):
    hash = md5()
    with open(fname, "rb") as file:
        for block in iter(lambda: file.read(128 * hash.block_size), b""):
            hash.update(block)
    return hash.hexdigest()

#Ask for input on what website you would like the request to be.
#Specify DOMAIN. https:// or http:// will cause errors.
website = input("What domain are you wanting to make the HTTP request to?: ")
filename = website #Setting filename for the http requests as the input given.
print("You've entered: " + website)
httpget = req.request(method='GET', url="http://"+website) #Forced http://
file = open(filename, "w+") #New file with new file name
file.write(httpget.text) #Writes the request we sent out to the file.

#Call the function previously defined, passing our exact file created
checksum = md5sum(filename)
print("Checksum of the file: " + checksum) 
print("Printing the checksum of the file to a file named checksum.txt")
#Confirmation.
file = open("checksum.txt", "w+") #New file, again.
file.write(checksum) #Writing the checksum to a new file.
print("Finished!")