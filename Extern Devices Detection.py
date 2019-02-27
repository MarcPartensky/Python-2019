import os

def search():
    output=""
    for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(os.access(lettre + ":\\", os.R_OK))
        if os.access(lettre + ":\\", os.R_OK):
            if os.access(lettre + ":\\" + "289571048976325.txt", os.R_OK):
                output+="Ma clé USB: "+lettre+"\n"
    if len(output)==0:
        output="No devices found."
    return output

print(search())
