from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@router.post("/subcategories/", response_model=schemas.SubCategory)
def create_subcategory(subcategory: schemas.SubCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_subcategory(db=db, subcategory=subcategory)

@router.post("/goods/", response_model=schemas.Good)
def create_good(good: schemas.GoodCreate, db: Session = Depends(get_db)):
    return crud.create_good(db=db, good=good)

@router.post("/sizes/", response_model=schemas.Size)
def create_size(size: schemas.SizeCreate, db: Session = Depends(get_db)):
    return crud.create_size(db=db, size=size)

@router.post("/stocks/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    return crud.create_stock(db=db, stock=stock)

@router.post("/incomes/", response_model=schemas.Income)
def create_income(income: schemas.IncomeCreate, db: Session = Depends(get_db)):
    return crud.create_income(db=db, income=income)

@router.post("/supplier_stocks/", response_model=schemas.SupplierStock)
def create_supplier_stock(supplier_stock: schemas.SupplierStockCreate, db: Session = Depends(get_db)):
    return crud.create_supplier_stock(db=db, supplier_stock=supplier_stock)

@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@router.post("/sales/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db=db, sale=sale)

@router.post("/report_details/", response_model=schemas.ReportDetail)
def create_report_detail(report_detail: schemas.ReportDetailCreate, db: Session = Depends(get_db)):
    return crud.create_report_detail(db=db, report_detail=report_detail)
