from fastapi import FastAPI

app = FastAPI()

# Query Parameters are used to filter the data from the database.

@app.get("/products")
def get_products(
    category:str ="Electronics Items" , min_price : int = 0, max_price : int = 10000):
    return {
        "categoy": category,
        "min_price": min_price,
        "max_price": max_price          
    }