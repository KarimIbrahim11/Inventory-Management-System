"""
Selected transaction-management logic from the
Inventory Management System.

The complete application contains 1,900+ lines of Python code.
This file contains selected logic for creating structured
inventory transactions.
"""


def create_transaction(
    date,
    product_id,
    product_name,
    transaction_type,
    quantity,
    price,
    platform,
    order_id,
    package_id,
    stock_before,
    stock_after,
    notes,
    quantity_type
):
    """
    Create a structured inventory transaction.

    This standardizes all inventory movements into
    a consistent transaction record.
    """

    transaction = {
        "Date": date,
        "Product ID": product_id,
        "Product Name": product_name,
        "Type": transaction_type,
        "Quantity": quantity,
        "Price": price,
        "Platform": platform,
        "Order ID": order_id,
        "Package ID": package_id,
        "Stock Before": stock_before,
        "Stock After": stock_after,
        "Notes": notes,
        "Quantity Type": quantity_type
    }

    return transaction


def create_damaged_return(
    return_date,
    product_id,
    product_name,
    quantity,
    platform,
    order_id,
    package_id,
    notes
):
    """
    Create a damaged-return record.

    Damaged returns are stored separately and do not
    increase available inventory.
    """

    damaged_return = {
        "Return Date": return_date,
        "Product ID": product_id,
        "Product Name": product_name,
        "Quantity": quantity,
        "Platform": platform,
        "Order ID": order_id,
        "Package ID": package_id,
        "Notes": notes
    }

    return damaged_return


def prepare_new_product(
    product_id,
    product_name,
    category,
    initial_quantity,
    minimum_quantity
):
    """
    Prepare a new product record for the Products sheet.
    """

    product = {
        "Product ID": product_id,
        "Product Name": product_name,
        "Category": category,
        "Quantity": initial_quantity,
        "Minimum Qty": minimum_quantity
    }

    return product


def prepare_initial_transaction(
    date,
    product_id,
    product_name,
    quantity,
    price,
    supplier,
    stock_after,
    notes
):
    """
    Create the initial transaction for a newly created product.

    The initial quantity is treated as the product's
    starting inventory.
    """

    transaction = {
        "Date": date,
        "Product ID": product_id,
        "Product Name": product_name,
        "Type": "New Purchase",
        "Quantity": quantity,
        "Price": price,
        "Platform": "",
        "Order ID": "",
        "Package ID": "",
        "Stock Before": 0,
        "Stock After": stock_after,
        "Notes": notes,
        "Quantity Type": "New Purchase",
        "Supplier": supplier
    }

    return transaction
