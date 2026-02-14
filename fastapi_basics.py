from fastapi import FastAPI, Query  # импорт FastAPI и Query для описания параметров

app = FastAPI(title="basics")

# GET /api/v1/basics?name=...
@app.get("/api/v1/basics")
async def get_basics(
    name: str = Query(               # объявляем query-параметр name
        default="Alise",             # значение по умолчанию
        description="Имя пользователя"  # описание в Swagger UI
    )
):
    # возвращаем персонализированное сообщение
    return {"message": f"Hello, {name}!"}

