from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from pages.router import router as router_pages
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def get_html(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})



app.include_router(router_pages)

