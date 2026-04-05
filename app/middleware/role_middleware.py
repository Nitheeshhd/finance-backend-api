from fastapi import Request, HTTPException

async def role_checker(request: Request, call_next):

    path = request.url.path

    if (
        path == "/" or
        path.startswith("/docs") or
        path.startswith("/openapi") or
        path.startswith("/favicon") or
        path.startswith("/users") or
        path.startswith("/records") or
        path.startswith("/dashboard")
    ):
        return await call_next(request)

    role = request.headers.get("role")

    if not role:
        raise HTTPException(status_code=400, detail="Role header missing")

    if role == "viewer" and request.method != "GET":
        raise HTTPException(status_code=403, detail="Viewer cannot perform this action")

    if role == "analyst" and request.method != "GET":
        raise HTTPException(status_code=403, detail="Analyst has limited access")

    return await call_next(request)