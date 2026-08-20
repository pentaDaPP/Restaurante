import cloudinary
from dotenv import load_dotenv
import os

load_dotenv()

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_API_SECRET")
)
print("cloud_name" , os.getenv("CLOUDINARY_CLOUD_NAME"))
print("api_key" , os.getenv("CLOUDINARY_API_KEY"))
print("secret_key" , os.getenv("CLOUDINARY_API_SECRET"))