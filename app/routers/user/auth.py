from fastapi import APIRouter, Query
from app.dto.common import (BaseResponse, BaseResponseData)
from app.dto.user_dto import (UserRegisterRequest, UserLoginRequest)
from app.services.user_service import UserService
from app.helpers.jwt_helpers import generate_token
from app.models.user import UserData

route = APIRouter(tags=['Auth'], prefix="/auth")


@route.post("/register")
async def register(register_input: UserRegisterRequest):
    user_id = await UserService().register(register_input)
    
    return BaseResponseData(
        message="Tạo tài khoản thành công",
        data=user_id
    )


@route.post("/login")
async def login(login_input: UserLoginRequest):
    user_data = await UserService().login(login_input)
    
    token = generate_token({"user_id": str(user_data['id'])})
    return {
        "message": "Đăng nhập thành công",
        "data": user_data,
        "token": token
    }
    
@route.get("/overview")
async def overview_ktx():
    overview = await UserService().overview()
    
    return overview


@route.get("/gen")
async def gen_ktx():
    for i in range(0, 30):
        user_dict = {
            "email": f"example{i}@gmail.com",
            "full_name": f"Nguyen Van A {i}",
            "mssv": f"2019011{i}",
            "password": "12345678",
            "user_type": 1,
            "is_valid": True,
            "is_more_info": True,
            "major": "14",
            "gender": 1,
            "batch": "64",
            "phonenumber": f"{i}12345{i}003",
            "birth": "2001-01-01"
        }
        model = UserData(**user_dict)
        await model.save()
    
    return {
        "message": "Thanh cong"
    }