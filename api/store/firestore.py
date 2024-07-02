import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
# from dotenv import load_dotenv
# load_dotenv()

# Initialize the app with a service account
try:
    # cred = credentials.ApplicationDefault()
    print(">>>>>>>>>Firebase SDK initializing...")
    service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')  
    print(">>>>>>",service_account_path)
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)
    print("Firebase SDK initialized successfully.")
except Exception as e:
    print(f"Error initializing Firebase SDK: {e}")


project_id = os.getenv('PROJECT_ID')
database_id = os.getenv('DATABASE_ID')

db = firestore.Client(
        project=project_id, 
        database=database_id
)

collection_name = 'persons'


def add_person(person):
    doc_ref = db.collection(collection_name)
    doc_ref.document(person['id']).set(person)
    return person['id']


def read_all_docs(collection_name):
    docs = db.collection(collection_name).stream()
    documents = [doc.to_dict() for doc in docs]

    return documents

# Function to get a document by ID
def get_document_by_id(collection_name, document_id):
    doc_ref = db.collection(collection_name).document(document_id)
    try:
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise Exception(f'No such document with ID: {document_id}')
    except Exception as e:
        print(f'Error getting document: {e}')
        return None
if __name__== '__init__':
    print("App running...")

