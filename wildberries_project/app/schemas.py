from typing import List, Optional
from pydantic import BaseModel

# Схемы Pydantic
class CategoryBase(BaseModel):
    name: str
    is_visible: bool

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class SubCategoryBase(BaseModel):
    subject_id: int
    parent_id: int
    subject_name: str
    parent_name: str

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategory(SubCategoryBase):
    id: int

    class Config:
        orm_mode = True

class GoodBase(BaseModel):
    nm_id: int
    vendor_code: str
    currency_iso_code: str
    discount: int
    date_received: str

class GoodCreate(GoodBase):
    pass

class Good(GoodBase):
    id: int

    class Config:
        orm_mode = True

class SizeBase(BaseModel):
    id: int
    good_nm_id: int
    size_id: int
    price: int
    discounted_price: float
    tech_size_name: str

class SizeCreate(SizeBase):
    pass

class Size(SizeBase):
    id: int

    class Config:
        orm_mode = True

class StockBase(BaseModel):
    sku: str
    amount: int

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    sku: str

    class Config:
        orm_mode = True

class IncomeBase(BaseModel):
    income_id: int
    number: str
    date: str
    last_change_date: str
    supplier_article: str
    tech_size: str
    barcode: str
    quantity: int
    total_price: float
    date_close: str
    warehouse_name: str
    nm_id: int
    status: str

class IncomeCreate(IncomeBase):
    pass

class Income(IncomeBase):
    id: int

    class Config:
        orm_mode = True

class SupplierStockBase(BaseModel):
    last_change_date: str
    warehouse_name: str
    supplier_article: str
    nm_id: int
    barcode: str
    quantity: int
    in_way_to_client: int
    in_way_from_client: int
    quantity_full: int
    category: str
    subject: str
    brand: str
    tech_size: str
    price: float
    discount: float
    is_supply: bool
    is_realization: bool
    sc_code: str

class SupplierStockCreate(SupplierStockBase):
    pass

class SupplierStock(SupplierStockBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    date: str
    last_change_date: str
    warehouse_name: str
    country_name: str
    oblast_okrug_name: str
    region_name: str
    supplier_article: str
    nm_id: int
    barcode: str
    category: str
    subject: str
    brand: str
    tech_size: str
    income_id: int
    is_supply: bool
    is_realization: bool
    total_price: float
    discount_percent: int
    spp: float
    finished_price: float
    price_with_disc: float
    is_cancel: bool
    cancel_date: str
    order_type: str
    sticker: str
    g_number: str
    srid: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    date: str
    last_change_date: str
    warehouse_name: str
    country_name: str
    oblast_okrug_name: str
    region_name: str
    supplier_article: str
    nm_id: int
    barcode: str
    category: str
    subject: str
    brand: str
    tech_size: str
    income_id: int
    is_supply: bool
    is_realization: bool
    total_price: float
    discount_percent: int
    spp: float
    payment_sale_amount: int
    for_pay: float
    finished_price: float
    price_with_disc: float
    sale_id: str
    order_type: str
    sticker: str
    g_number: str
    srid: str

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True

class ReportDetailBase(BaseModel):
    realizationreport_id: int
    date_from: str
    date_to: str
    create_dt: str
    currency_name: str
    suppliercontract_code: str
    rrd_id: int
    gi_id: int
    subject_name: str
    nm_id: int
    brand_name: str
    sa_name: str
    ts_name: str
    barcode: str
    doc_type_name: str
    quantity: int
    retail_price: float
    retail_amount: float
    sale_percent: float
    commission_percent: float
    office_name: str
    supplier_oper_name: str
    order_dt: str
    sale_dt: str
    rr_dt: str
    shk_id: int
    retail_price_withdisc_rub: float
    delivery_amount: int
    return_amount: int
    delivery_rub: float
    gi_box_type_name: str
    product_discount_for_report: float
    supplier_promo: float
    rid: int
    ppvz_spp_prc: float
    ppvz_kvw_prc_base: float
    ppvz_kvw_prc: float
    ppvz_office_id: int
    ppvz_office_name: str
    ppvz_supplier_id: int
    ppvz_supplier_name: str
    ppvz_inn: str
    declaration_number: str
    sticker_id: str
    site_country: str
    penalty: float
    additional_payment: float
    kiz: str
    srid: str

class ReportDetailCreate(ReportDetailBase):
    pass

class ReportDetail(ReportDetailBase):
    id: int

    class Config:
        orm_mode = True
