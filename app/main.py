import fastapi as fa

from app.rest import api

# Infrastructure level
app = fa.FastAPI()

app.include_router(api.router)
