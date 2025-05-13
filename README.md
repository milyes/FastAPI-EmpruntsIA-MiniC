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
#include <stdio.h>
struct Emprunt {
    char nom[20];
    char emprunteur[20];
};

int main() {
    struct Emprunt e = {"IA", "Zoubirou"};
    printf("Nom: %s, Emprunteur: %s\n", e.nom, e.emprunteur);
    return 0;
}
