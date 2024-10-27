# from additionals import omni_key
omni_key=omni_key="|!@#$%^&*(omni_key_absolute)*&^%$#@!|"

import os
from database.db import get_all_keywords

def qwerty(cpath, keywords):
    try:
        # Specify 'utf-8' encoding to read the file
        with open(cpath, "r", encoding="utf-8") as file:
            content = file.read()
        
        cdir = os.path.dirname(cpath)
        lines = content.split("\n")
        res = []
        for line in lines[:-1]:
            words = line.split(omni_key)
            for keyword in keywords:
                if keyword["keyword"] in words[2] and line not in res:
                    res.append(line)

        nfpath = os.path.join(cdir, "new_file.txt")
        print(len(res))
        with open(nfpath, 'w', encoding='utf-8') as new_file:
            for i in res:
                line = i.split(omni_key)
                new_file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                new_file.write(line[1] + "\n")
                new_file.write(line[2] + "\n")
                new_file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                
        return nfpath
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


path=os.path.join("customer_panel","feed","5591086960","C--0G_0MtEo","comments.txt")
keywords=get_all_keywords()
print(keywords)

print(qwerty(keywords=keywords,cpath=path))