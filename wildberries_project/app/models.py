from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    api_key = Column(String)
    subscription_level = Column(String, default="no_subscription")

    # Relationships
    expenses = relationship("Expense", back_populates="seller")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    item_name = Column(String)
    ad_cost = Column(Float)
    photo_cost = Column(Float)
    salary_cost = Column(Float)
    other_cost = Column(Float)

    # Relationships
    seller = relationship("Seller", back_populates="expenses")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_visible = Column(Boolean)


class SubCategory(Base):
    __tablename__ = "subcategories"

    subject_id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer)
    subject_name = Column(String)
    parent_name = Column(String)


class Good(Base):
    __tablename__ = "goods"

    nm_id = Column(Integer, primary_key=True, index=True)
    vendor_code = Column(String)
    currency_iso_code = Column(String)
    discount = Column(Integer)
    date_received = Column(String)


class Size(Base):
    __tablename__ = "sizes"

    id = Column(Integer, primary_key=True, index=True)
    good_nm_id = Column(Integer, ForeignKey('goods.nm_id'))
    size_id = Column(Integer)
    price = Column(Integer)
    discounted_price = Column(Float)
    tech_size_name = Column(String)


class Stock(Base):
    __tablename__ = "stocks"

    sku = Column(String, primary_key=True, index=True)
    amount = Column(Integer)


class Income(Base):
    __tablename__ = "incomes"

    income_id = Column(Integer, primary_key=True, index=True)
    number = Column(String)
    date = Column(String)
    last_change_date = Column(String)
    supplier_article = Column(String)
    tech_size = Column(String)
    barcode = Column(String)
    quantity = Column(Integer)
    total_price = Column(Float)
    date_close = Column(String)
    warehouse_name = Column(String)
    nm_id = Column(Integer)
    status = Column(String)


class SupplierStock(Base):
    __tablename__ = "supplier_stocks"

    last_change_date = Column(String)
    warehouse_name = Column(String)
    supplier_article = Column(String)
    nm_id = Column(Integer, primary_key=True)
    barcode = Column(String)
    quantity = Column(Integer)
    in_way_to_client = Column(Integer)
    in_way_from_client = Column(Integer)
    quantity_full = Column(Integer)
    category = Column(String)
    subject = Column(String)
    brand = Column(String)
    tech_size = Column(String)
    price = Column(Float)
    discount = Column(Float)
    is_supply = Column(Boolean)
    is_realization = Column(Boolean)
    sc_code = Column(String)


class Order(Base):
    __tablename__ = "orders"

    date = Column(String)
    last_change_date = Column(String)
    warehouse_name = Column(String)
    country_name = Column(String)
    oblast_okrug_name = Column(String)
    region_name = Column(String)
    supplier_article = Column(String)
    nm_id = Column(Integer, primary_key=True)
    barcode = Column(String)
    category = Column(String)
    subject = Column(String)
    brand = Column(String)
    tech_size = Column(String)
    income_id = Column(Integer)
    is_supply = Column(Boolean)
    is_realization = Column(Boolean)
    total_price = Column(Float)
    discount_percent = Column(Integer)
    spp = Column(Float)
    finished_price = Column(Float)
    price_with_disc = Column(Float)
    is_cancel = Column(Boolean)
    cancel_date = Column(String)
    order_type = Column(String)
    sticker = Column(String)
    g_number = Column(String)
    srid = Column(String)


class Sale(Base):
    __tablename__ = "sales"

    date = Column(String)
    last_change_date = Column(String)
    warehouse_name = Column(String)
    country_name = Column(String)
    oblast_okrug_name = Column(String)
    region_name = Column(String)
    supplier_article = Column(String)
    nm_id = Column(Integer, primary_key=True)
    barcode = Column(String)
    category = Column(String)
    subject = Column(String)
    brand = Column(String)
    tech_size = Column(String)
    income_id = Column(Integer)
    is_supply = Column(Boolean)
    is_realization = Column(Boolean)
    total_price = Column(Float)
    discount_percent = Column(Integer)
    spp = Column(Float)
    payment_sale_amount = Column(Integer)
    for_pay = Column(Float)
    finished_price = Column(Float)
    price_with_disc = Column(Float)
    sale_id = Column(String, primary_key=True, index=True)
    order_type = Column(String)
    sticker = Column(String)
    g_number = Column(String)
    srid = Column(String)


class ReportDetail(Base):
    __tablename__ = "report_details"

    realizationreport_id = Column(Integer, primary_key=True, index=True)
    date_from = Column(String)
    date_to = Column(String)
    create_dt = Column(String)
    currency_name = Column(String)
    suppliercontract_code = Column(String)
    rrd_id = Column(Integer)
    gi_id = Column(Integer)
    subject_name = Column(String)
    nm_id = Column(Integer)
    brand_name = Column(String)
    sa_name = Column(String)
    ts_name = Column(String)
    barcode = Column(String)
    doc_type_name = Column(String)
    quantity = Column(Integer)
    retail_price = Column(Float)
    retail_amount = Column(Float)
    sale_percent = Column(Float)
    commission_percent = Column(Float)
    office_name = Column(String)
    supplier_oper_name = Column(String)
    order_dt = Column(String)
    sale_dt = Column(String)
    rr_dt = Column(String)
    shk_id = Column(Integer)
    retail_price_withdisc_rub = Column(Float)
    delivery_amount = Column(Integer)
    return_amount = Column(Integer)
    delivery_rub = Column(Float)
    gi_box_type_name = Column(String)
    product_discount_for_report = Column(Float)
    supplier_promo = Column(Float)
    rid = Column(Integer)
    ppvz_spp_prc = Column(Float)
    ppvz_kvw_prc_base = Column(Float)
    ppvz_kvw_prc = Column(Float)
    ppvz_office_id = Column(Integer)
    ppvz_office_name = Column(String)
    ppvz_supplier_id = Column(Integer)
    ppvz_supplier_name = Column(String)
    ppvz_inn = Column(String)
    declaration_number = Column(String)
    sticker_id = Column(String)
    site_country = Column(String)
    penalty = Column(Float)
    additional_payment = Column(Float)
    kiz = Column(String)
    srid = Column(String)
