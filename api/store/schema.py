import uuid
from pydantic import BaseModel, Field

class Address(BaseModel):     
    street: str
    city: str
    state: str
    zip: str

class Person(BaseModel):
    id: str = Field(default=str(uuid.uuid4()))
    first_name: str
    last_name: str
    age: int = Field(gt=0)
    email: str
    address: Address
    def __init__(self, id, first_name, last_name, email,  age, address) -> None:
        super().__init__(id=id, first_name=first_name, last_name=last_name, email=email,  age=age, address=address)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address

    def to_dict(self):
        dest = {"last_name": self.last_name, 
                "first_name": self.first_name, 
                "email": self.email, 
                "id": self.id, 
                "age": self.age,
                "address": self.address}

        if self.id:
            dest["id"] = self.id

        if self.age:
            dest["age"] = self.age

        if self.address:
            dest["address"] = self.address

        if self.last_name:
            dest["last_name"] = self.last_name

        if self.first_name:
            dest["first_name"] = self.first_name

        return dest

    def __repr__(self):
        return f"Person(\
                first_name={self.first_name}, \
                last_name={self.last_name}, \
                email={self.email}, \
                age={self.age}, \
                id={self.id}, \
                address={self.address}\
            )"


