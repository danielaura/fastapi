from fastapi import FastAPI, Body 
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi app con FasAPI"
app.version = "0.0.1"

movies = [
    {
        'id':1,
        'title': 'avatar',
        'overview': "En un exuberante planeta llamado pandora viven los Na'vi",
        'year': "2009",
        'rating': 7.8,
        'category': "Accion"
    },
    {
        'id':2,
        'title': 'avatar2',
        'overview': "En un exuberante planeta llamado pandora viven los Na'vi",
        'year': "2023",
        'rating': 7.8,
        'category': "Comedia"
    }
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#Parametro de ruta Ej. {id}
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: str):
    for item in movies:
        if item['category'] == category:
            return item
        elif item['year'] == year:
            return item
    return []

@app.post('/movies', tags=['movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        'id':id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies          