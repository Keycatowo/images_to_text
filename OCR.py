#!/usr/bin/env python
# coding: utf-8

# 

# In[6]:


from PIL import Image
import pytesseract
import glob # to get file path



# In[13]:


filepath=glob.glob('./images/*')



# In[22]:


text = ""

for file in filepath:
    #開啟檔案
    print(file)
    img = Image.open(file)
    line = pytesseract.image_to_string(img, lang='chi_tra')
    print(line)
    text += file + "\n"
    text += line + "\n\n"


# In[26]:


f = open('./text/output.txt',"w")
print(text)
f.write(text)
f.close()


# In[ ]:




