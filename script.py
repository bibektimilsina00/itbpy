from firebase_admin import credentials, firestore, initialize_app
import json

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('./serviceAccountKey.json')
initialize_app(cred)

# Function to delete users with empty fcmToken
def delete_users_with_empty_fcmToken():
    db = firestore.client()
    users_ref = db.collection('users')  # Replace 'users' with your collection name
    docs = users_ref.stream()

    for doc in docs:
        user = doc.to_dict()
        if 'fcmToken' in user and user['fcmToken'] == "":
            print(f"Deleting user: {doc.id}")
            users_ref.document(doc.id).delete()

# Call the function
# delete_users_with_empty_fcmToken()



def store_user_details_to_file():
    db = firestore.client()
    users_ref = db.collection('users')  # Replace 'users' with your collection name
    docs = users_ref.stream()

    users = []
    for doc in docs:
        user = doc.to_dict()
        user['id'] = doc.id  # Add the document ID to the user data
        users.append(user)

    with open('user_details.json', 'w') as file:
        json.dump(users, file, indent=4)

    print("User details stored in user_details.json")

# Call the function
store_user_details_to_file()