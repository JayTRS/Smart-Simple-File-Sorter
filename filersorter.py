import os
import shutil
from dotenv import find_dotenv, load_dotenv
from groq import Groq
load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)



path = input("Enter the path location of the files you want to move: ")
files = os.listdir(path)
newpath = input("Enter the path where the files will move to: ")
newfiles = [f for f in os.listdir(newpath) if os.path.isdir(os.path.join(newpath, f))]
print(newfiles)

for file in files:
    filename,extention = os.path.splitext(file)
    extention = extention[1:]

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""Your task is to organize files by determine their extenions and move them to their respective folders that you deem suited for them. 
            Extension = {extention} 
            All folders avaliable for u to organize= {newfiles} (Ignore all text with extension) 
            Response Structure: 'name of the folder' 
            Response Conditon: Follow the response structure strictly and only, never use any of ur own words no matter what even if you are unclear about which folder to move the file into. Follow the instruction strictly.
            Conditions: if the file end with .mp3, the responding folder is Music else if its another form of sound file, move to Sounds """ 
        }
    ],
    model="llama-3.3-70b-specdec",
    )
    response = chat_completion.choices[0].message.content
    print(path + "\\" + file + " ---> " + newpath + "\\" + response)
    shutil.move(path + "\\" + file, newpath + "\\" + response)




