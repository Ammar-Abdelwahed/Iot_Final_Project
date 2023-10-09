import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from time import sleep
# Initialize Firebase
cred = credentials.Certificate("C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add Data

def system_processes(log_file, collec, fruit_type, id):
    date = datetime.now().strftime("%Y-%m-%d")
    #get the data continuously
    t = datetime.now().strftime("%H:%M:%S")
    #format log_info
    data_json = {id: fruit_type}
    data = f"{date} {t}: {data_json[id]}\n"
    append_log_file(log_file, data)
    doc_ref = db.collection(collec).document(fruit_type)
    doc_ref.set(data_json)
    print("Data added.")
        

def create_log_file(log_file):
    with open(log_file,'w') as file:
        file.write("")

def append_log_file(log_file, log_info):
    with open(log_file,'a') as file:
        file.write(log_info)


if __name__ == '__main__':
    #take input from camera
    date = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{date}-pub.log" 
    #create file
    create_log_file(log_file)
    while True:
        fruit_type = input("Enter fruit type: ")
        id = input("enter the id: ")
        system_processes(log_file, "grad2", fruit_type, id)
    