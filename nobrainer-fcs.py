import readfcs

class File:
    def __init__(self, filename):
        self.filename = filename
        self.filepath = f"./{filename}"

    def present (self):
        stuff= readfcs.read(self.filepath)
        return print(stuff)

#    def inspectvar (self):
 #       varobject = readfcs.read(self.filepath)
  #      outputvar = varobject.var
   #     return print(outputvar)
    
    def inspectuns (self):
        unsobject = readfcs.read(self.filepath)
        outputuns = unsobject.uns["meta"]
        for k, v in outputuns.items():
            print(f"{k} : {v}")
        return print()

print("***************************")
print("***************************")
print("***************************")
print("Welcome to Artur´s No-Brainer .fcs Metadata Inspector. Please put the files you wish to work on in the same folder as this script.")

while True:
    workfile = File(input("Please specify file name: "))
    print("***************************")
    print("Here are the .fcs file properties, presented as an Object: ")
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    File.present(workfile)
    print("***************************")
    #print("Here are variables involved: ")
    #print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    #File.inspectvar(workfile)
    print("***************************")
    print("Here is the metadata: ")
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    File.inspectuns(workfile)
    print("***************************")
    check = input("Do you wish to analyze another file? Y to continue, any other key for exit.")
    if check.upper() == "Y":
        continue
    print("All done, have a nice day!")
    break
