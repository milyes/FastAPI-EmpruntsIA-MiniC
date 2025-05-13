# FastAPI Emprunts IA + Mini C

Mini projet démonstratif combinant une API en Python (FastAPI) et un exemple en langage C structuré.

## 1. API FastAPI Emprunts

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Emprunt(BaseModel):
    nom: str
    emprunteur: str

@app.post("/as")
def lancer_emprunt(data: Emprunt):
    return {"message": f"Emprunt enregistré pour {data.emprunteur} par {data.nom}"}
