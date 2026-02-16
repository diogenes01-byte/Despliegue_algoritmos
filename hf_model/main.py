from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI(title="API de Traducción Funcional")

class TranslationRequest(BaseModel):
    texto: str
    source_lang: str = "en"
    target_lang: str = "es"

# Modelo T5 
MODEL_NAME = "t5-small"  
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

@app.post("/traducir")
def traducir(request: TranslationRequest):
    try:
        # Preparar texto para T5: "translate {source} to {target}: texto"
        input_text = f"translate {request.source_lang} to {request.target_lang}: {request.texto}"
        inputs = tokenizer(input_text, return_tensors="pt")

        translated_tokens = model.generate(**inputs)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return {"traduccion": translated_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




