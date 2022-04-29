import fastapi as fa

from app.users import registry
from app import deps

router: fa.APIRouter = fa.APIRouter()

# Primary adapter level
@router.get("/")
def register_new_user(
    user_registry: registry.Users = fa.Depends(deps.user_registry_dep),
    name: str = fa.Query(...),
    email: str = fa.Query(...),
):
    user_registry.new(name, email)
    return {name: email}
