import os
class Config:
	   API_ID = int(os.environ.get("API_ID"))
	   API_HASH = os.environ.get("API_HASH")
	   STRING_SESSION = os.environ.get("SS")