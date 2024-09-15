from fastapi import FastAPI
import src.config.config as config
from fastapi.middleware.cors import CORSMiddleware
from src.api.system.routes import router as system_router

app = FastAPI(
  title= config.PROJECT_NAME,
  description= "{{ cookiecutter.project_description }}" }}",
  summary="This is a FastAPI project template.",
  version= config.VERSION,
  terms_of_service="",
  contact={
      "name": "",
      "url": "",
      "email": "",
  },
  license_info={
      "name": "Apache 2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
  },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-Requested-With", "Content-Type"],
)



app.include_router(system_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
