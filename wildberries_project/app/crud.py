from sqlalchemy.orm import Session
import models, schemas

# CRUD операции для новых моделей
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_subcategory(db: Session, subcategory_id: int):
    return db.query(models.SubCategory).filter(models.SubCategory.id == subcategory_id).first()

def create_subcategory(db: Session, subcategory: schemas.SubCategoryCreate):
    db_subcategory = models.SubCategory(**subcategory.dict())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def get_good(db: Session, good_id: int):
    return db.query(models.Good).filter(models.Good.id == good_id).first()

def create_good(db: Session, good: schemas.GoodCreate):
    db_good = models.Good(**good.dict())
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good

def get_size(db: Session, size_id: int):
    return db.query(models.Size).filter(models.Size.id == size_id).first()

def create_size(db: Session, size: schemas.SizeCreate):
    db_size = models.Size(**size.dict())
    db.add(db_size)
    db.commit()
    db.refresh(db_size)
    return db_size

def get_stock(db: Session, sku: str):
    return db.query(models.Stock).filter(models.Stock.sku == sku).first()

def create_stock(db: Session, stock: schemas.StockCreate):
    db_stock = models.Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def get_income(db: Session, income_id: int):
    return db.query(models.Income).filter(models.Income.id == income_id).first()

def create_income(db: Session, income: schemas.IncomeCreate):
    db_income = models.Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def get_supplier_stock(db: Session, stock_id: int):
    return db.query(models.SupplierStock).filter(models.SupplierStock.id == stock_id).first()

def create_supplier_stock(db: Session, stock: schemas.SupplierStockCreate):
    db_supplier_stock = models.SupplierStock(**stock.dict())
    db.add(db_supplier_stock)
    db.commit()
    db.refresh(db_supplier_stock)
    return db_supplier_stock

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_sale(db: Session, sale_id: str):
    return db.query(models.Sale).filter(models.Sale.sale_id == sale_id).first()

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_report_detail(db: Session, report_id: int):
    return db.query(models.ReportDetail).filter(models.ReportDetail.id == report_id).first()

def create_report_detail(db: Session, report_detail: schemas.ReportDetailCreate):
    db_report_detail = models.ReportDetail(**report_detail.dict())
    db.add(db_report_detail)
    db.commit()
    db.refresh(db_report_detail)
    return db_report_detail
