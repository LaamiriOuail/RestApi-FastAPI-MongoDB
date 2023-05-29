from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi import File, UploadFile
import datetime
import shutil
import os
from app.server.database import (
    add_freelancer,
    delete_freelancer,
    retrieve_freelancer,
    retrieve_freelancers,
    update_freelancer,
    upload_avatar_image
)
from app.server.models.freelancer import (
    ErrorResponseModel,
    ResponseModel,
    FreelanceSchema,
    UpdateFreelanceSchema,
)

router = APIRouter()

@router.post("/", response_description="freelancer data added into the database")
async def add_freelancer_data(freelancer: FreelanceSchema = Body(...)):
    freelancer = jsonable_encoder(freelancer)
    new_freelancer = await add_freelancer(freelancer)
    return ResponseModel(new_freelancer, "freelancer added successfully.")

@router.get("/", response_description="freelancer retrieved")
async def get_freelancer():
    freelancer = await retrieve_freelancers()
    if freelancer:
        return ResponseModel(freelancer, "freelancer data retrieved successfully")
    return ResponseModel(freelancer, "Empty list returned")


@router.get("/{id}", response_description="freelancer data retrieved")
async def get_freelancer_data(id):
    freelancer = await retrieve_freelancer(id)
    if freelancer:
        return ResponseModel(freelancer, "freelancer data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "freelancer doesn't exist.")

@router.put("/{id}")
async def update_student_data(id: str, req: UpdateFreelanceSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_freelancer(id, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )
    
@router.delete("/{id}", response_description="freelancer data deleted from the database")
async def delete_freelancer_data(id: str):
    deleted_freelancer = await delete_freelancer(id)
    if deleted_freelancer:
        return ResponseModel(
            "freelancer with ID: {} removed".format(id), "freelancer deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "freelancer with id {0} doesn't exist".format(id)
    )