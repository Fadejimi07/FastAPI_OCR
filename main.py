from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

app = FastAPI()


@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    filepath = "txtfile"
    with open(filepath, "w+b") as f:
        shutil.copyfileobj(image.file, f)
    return pytesseract.image_to_string(filepath, lang="eng")
