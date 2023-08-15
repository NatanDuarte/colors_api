import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from colors_api.color_extractor import ColorExtractor


app = FastAPI()

@app.get('/healthcheck')
def healthcheck():
    return { "status": "ok" }

@app.post('/colors')
def extract_colors(n_colors: int, file: UploadFile = File(...)):
    try:
        if file.content_type.startswith('image/'):
            temp_file = f'./temp/{file.filename}'
            with open(temp_file, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            colorExtractor = ColorExtractor()

            palette_json = colorExtractor.load(temp_file).extract(n_colors)

            return JSONResponse(content=palette_json, status_code=200)
        else:
            return JSONResponse(content={
                "message": "no image provided"
            }, status_code=400)
    except Exception as e:
        return JSONResponse(content={
            "message": f"Erro ao processar a imagem: {str(e)}"
        }, status_code=500)
