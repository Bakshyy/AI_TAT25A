from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import Body
from pydantic import BaseModel  # Import Pydantic's BaseModel
import os


# Initialize the FastAPI app
app = FastAPI()

# Load environment variables
load_dotenv()

# Fetch the OpenAI API key from .env
api_key = os.getenv("OPENAI_KEY")

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=api_key,
)

# CORS configuration for FlutterFlow
origins = [
    "http://localhost",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model to validate and structure the prompt request
class PromptRequest(BaseModel):
    prompt: str  # Define the expected prompt structure

# Root endpoint for the homepage
@app.get("/")
async def HomeScreen():
    return {"message": "Welcome to my bullshit"}

# Generate endpoint to handle POST requests with structured data
@app.post("/generate")
async def generate(prompt_request: PromptRequest):  # Use Pydantic model
    prompt = prompt_request.prompt  # Access the prompt directly
    
    try:
        # Making a request to the OpenAI API for generating a completion
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        # Returning the generated content as a response
        return {"response": response.choices[0].message.content}
    
    except Exception as e:
        # Handle API or other errors
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/NewPage")
async def NewPage():
    return {"message": "New Page"}




