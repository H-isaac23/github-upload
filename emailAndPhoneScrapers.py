import re, pyperclip

telephoneRegex = re.compile(R"""(
(\(\d\d\d\)) # Area code 
(\s|-)      # Separator
\d\d\d      # Second part
-           # Separator
\d\d\d\d    # Third Part
)""", re.VERBOSE)

telephoneOneRegex = re.compile(R"""(
((\d{2,3})|\(\d{2,3}\))?# Area code 
(\s|-)?      # Separator
\d\d\d\d      # Second part
-           # Separator
\d\d\d\d    # Third Part
)""", re.VERBOSE)

phoneRegex = re.compile(r"""(
(\+)?
\d{4,5}  #Area Code
(\s|-)?    #Separator
\d\d\d    #First part
(\s|-)?    #Separator
\d\d\d\d    #Third part
)""", re.VERBOSE)

emailRegex = re.compile(r"""
[a-zA-Z0-9_.+-]+#username
@#@
[a-zA-Z0-9_.+-]+#domain
""", re.VERBOSE)

text = pyperclip.paste()

foundPhones = phoneRegex.findall(text)
foundTelephones = telephoneRegex.findall(text)
foundEmails = "\n".join(emailRegex.findall(text))
foundTelephoneOnes = telephoneOneRegex.findall(text)
telephones = []
phones = []
telephoneOnes = []
for x in foundTelephones:
    telephones.append(x[0])
for x in foundTelephoneOnes:
    telephoneOnes.append(x[0])
for x in foundPhones:
    phones.append(x[0])
print("\n".join(phones).lstrip())
print()
print("\n".join(telephones).lstrip())
print()
print("\n".join(telephoneOnes).lstrip())
print()
print(foundEmails)


