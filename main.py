from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import pages.router
from pages.router import router as router_pages

app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def welcome() -> str:
    return 'Главная страница'

#print(pages.router.get_input_page)


app.include_router(router_pages)

