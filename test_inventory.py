import pytest

from inventory import Inventory
from product import Product

@pytest.fixture
def inventory():  #fresh new empty inventory for each test
    return Inventory()

@pytest.fixture
def make_product():
    def make(
            product_id="1", product_name="indomie", 
            price=25.99, quantity=10, 
            category="snacks", brand="Noodles",
              size="M", supplier="Allan ojuka", 
              entry_date=None, expiry_date=None
              ):
        return Product(
            product_id, product_name, 
            price, quantity, 
            category, brand,
            size, supplier, 
            entry_date=None, expiry_date=None
        )
    return make

def test_product_creation(make_product):
    product = make_product(category="snacks", brand="noodles")
    assert product.category.lower() == "snacks"
    assert product.brand.lower() == "noodles"

def test_inventory_quantity_helpers(inventory, make_product):
    inventory.add_product(make_product(product_id="1", quantity =10))

    assert inventory.check_stock("1",5) is True
    assert inventory.reduce_stock("1",5).quantity == 5
    assert inventory.update_quantity("1",99).quantity == 99


@pytest.fixture

def loaded_inventory(inventory, make_product):
    inventory.add_product(make_product(
        "1","Hammer",
        "Tools", "ACME",
        "John Cena",10
    ))
    inventory.add_product(make_product(
        "1","Hammer",
        "Tools", "ACME",
        "John Cena",10
    ))
    inventory.add_product(make_product(
        "2","omena",
        "food", "ALLAN OJUKA FRIEND",
        "Johnny ",134
    ))
    inventory.add_product(make_product(
        "10","FLUGONE",
        "medice", "MEDACTIVE",
        "MLAFI ",1340
    ))
    return inventory

def test_add_product(inventory,make_product):
    product = make_product(product_id="1")
    results = inventory.add_product(product)

    assert results is product
    assert len(inventory) == 1
    assert inventory.find_product("1") is product


def test_add_product_dublicate_id(inventory,make_product):
    inventory.add_product(make_product(product_id="2"))

    with pytest.raises(ValueError,match="already exists"):
        inventory.add_product(make_product(product_id ="2"))

def test_add_product_wrong_type_raises(inventory):
    with pytest.raises(TypeError):
        inventory.add_product({"product_id":"2"})

