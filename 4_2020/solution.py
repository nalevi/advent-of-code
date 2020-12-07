import re

class Passport:

    byr = 0
    iyr = 0
    eyr = 0
    hgt = ""
    hcl = ""
    ecl = ""
    pid = 0
    cid = ""

    def valid(self):
        isValid = True
        if int(self.byr) not in range(1920,2003):
            isValid = False
        if int(self.iyr) not in range(2010,2021):
            isValid = False
        if int(self.eyr) not in range(2020,2031):
            isValid = False

        if re.search('cm',str(self.hgt)) != None:
            if (re.fullmatch('[0-9]{3}cm',str(self.hgt)) == None) or int(self.hgt[:-2]) not in range(150,194):
                isValid = False
        elif re.search('in',str(self.hgt)) != None:
            if (re.fullmatch('[0-9]{2}in',str(self.hgt)) == None) or int(self.hgt[:-2]) not in range(59,77):
                isValid = False
        else:
           isValid = False 


        if re.fullmatch('#[0-9a-f]{6}',str(self.hcl)) == None:
            isValid = False

        if self.ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
            isValid = False
        
        if re.fullmatch('[0-9]{9}',str(self.pid)) == None:
            isValid = False

        return isValid

    def __str__(self):
        out = ""
        out += "byr: " + str(self.byr) + " "
        out += "iyr: " + str(self.iyr) + " "
        out += "eyr: " + str(self.eyr) + " "
        out += "hgt: " + str(self.hgt) + " "
        out += "hcl: " + str(self.hcl) + " "
        out += "ecl: " + str(self.ecl) + " "
        out += "pid: " + str(self.pid) + " "
        out += "cid: " + str(self.cid) + " "

        return out

validPassport = 0

with open("input.txt","r") as file:
    content = file.read().splitlines()

    i = 0
    while i < len(content):
        passp = Passport()

        while content[i] != '':
            
            datas = content[i].split(' ')

            for d in datas:
                if d.split(':')[0] == 'byr':
                    passp.byr = d.split(':')[1]
                if d.split(':')[0] == 'iyr':
                    passp.iyr = d.split(':')[1]
                if d.split(':')[0] == 'eyr':
                    passp.eyr = d.split(':')[1]
                if d.split(':')[0] == 'hgt':
                    passp.hgt = d.split(':')[1]
                if d.split(':')[0] == 'hcl':
                    passp.hcl = d.split(':')[1]
                if d.split(':')[0] == 'ecl':
                    passp.ecl = d.split(':')[1]
                if d.split(':')[0] == 'pid':
                    passp.pid = d.split(':')[1]
                if d.split(':')[0] == 'cid':
                    passp.cid = d.split(':')[1]

            i += 1
            if i >= len(content):
                break
        if passp.valid():
            validPassport += 1
        i += 1

print("Valid: "+ str(validPassport))
    

    
    


