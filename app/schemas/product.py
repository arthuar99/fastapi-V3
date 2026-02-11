from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass
