from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKey
from fastapi.params import Security
from app.middleware.auth import get_api_key
from app.services.service_database import DatabaseService

router = APIRouter(
    prefix="/database",
    tags=["DATABASE"],
    responses={404: {"message": "Not found"}},
    dependencies=[Security(get_api_key)]
)

@router.get("/create")
async def create():
    db = DatabaseService()
    db.create_table()
    return True

@router.put("/insert")
async def insert():
    db = DatabaseService()
    db.insert_employee('John Doe', 30, 5000.0)
    db.insert_employee('Jane Smith', 35, 6000.0)
    return True

@router.get("/select")
async def select():
    db = DatabaseService()
    employees = db.get_employees()
    return employees

@router.patch("/update")
async def update():
    db = DatabaseService()
    db.update_employee(1, 'John Doe', 31, 5500.0)
    return True

@router.delete("/delete")
async def delete():
    db = DatabaseService()
    db.delete_employee(2)
    return True