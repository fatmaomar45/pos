from fastapi import FastAPI
from app.database import Base, engine

from app.routers.user import router as user
from app.routers.suppliers import router as suppliers
from app.routers.categories import router as categories
from app.routers.sales import router as sales
from app.routers.salesitems import router as salesitems
from app.routers.receipts import router as receipts
from app.routers.product import router as products
from app.routers.payments import router as payments
from app.routers.customers import router as customers


Base.metadata.create_all(bind=engine)


app = FastAPI(title="pos API", version="1.0")



app.include_router(user)
app.include_router(suppliers)
app.include_router(categories)
app.include_router(sales)
app.include_router(salesitems)
app.include_router(receipts)
app.include_router(products)
app.include_router(payments)
app.include_router(customers)
