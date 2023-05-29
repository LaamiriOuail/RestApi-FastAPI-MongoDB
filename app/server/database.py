import motor.motor_asyncio
from bson.objectid import ObjectId
from fastapi import File, UploadFile
import shutil
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.fiveer

freelancer = database.get_collection("freelancer")
# helpers


def freelancer_helper(freelancer) -> dict:
    return {
        "id": str(freelancer["_id"]),
        "username": freelancer["username"],
        "email": freelancer["email"],
        "password": freelancer["password"],
        "country": freelancer["country"],
        "phone": freelancer["phone"],
        "description": freelancer["description"],
        "avatar_path": freelancer["avatar_path"],
    }
    
# Retrieve all freelancers present in the database
async def retrieve_freelancers():
    freelancers = []
    async for freelanceri in freelancer.find():
        freelancers.append(freelancer_helper(freelanceri))
    return freelancers


# Add a new freelancer into to the database
async def add_freelancer(freelancer_data: dict) -> dict:
    freelanceri = await freelancer.insert_one(freelancer_data)
    new_freelancer = await freelancer.find_one({"_id": freelanceri.inserted_id})
    return freelancer_helper(new_freelancer)


# Retrieve a freelancer with a matching ID
async def retrieve_freelancer(id: str) -> dict:
    freelanceri = await freelancer.find_one({"_id": ObjectId(id)})
    if freelanceri:
        return freelancer_helper(freelanceri)


# Update a freelancer with a matching ID
async def update_freelancer(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    freelanceri = await freelancer.find_one({"_id": ObjectId(id)})
    if freelanceri:
        updated_freelancer = await freelancer.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_freelancer.modified_count > 0:
            return True
    return False


# Delete a freelancer from the database
async def delete_freelancer(id: str):
    freelanceri = await freelancer.find_one({"_id": ObjectId(id)})
    if freelanceri:
        await freelancer.delete_one({"_id": ObjectId(id)})
        return True
    
async def upload_avatar_image(file: UploadFile) -> str:
    # Generate a unique filename for the uploaded image (e.g., using UUID)
    filename = f"avatar_{file.filename}"
    # Save the uploaded image to the desired location
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return filename