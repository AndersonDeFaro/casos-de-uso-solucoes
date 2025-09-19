from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_products():
    return [{"product": "Laptop"}, {"product": "Mouse"}]

@router.get("/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id, "product": "Laptop"}