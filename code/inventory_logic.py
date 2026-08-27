"""
Selected inventory business logic from the
Inventory Management System.

The complete application contains 1,900+ lines of Python code.
Only selected core logic is included here.
"""


def calculate_stock_after(
    stock_before,
    quantity,
    transaction_type
):
    """
    Calculate the resulting stock based on
    the business transaction type.

    Business Rules:

    New Purchase  -> Stock +
    Good Return   -> Stock +
    Stock Out     -> Stock -
    Damaged Return -> No Stock Change
    """

    if transaction_type == "New Purchase":
        return stock_before + quantity

    elif transaction_type == "Good Return":
        return stock_before + quantity

    elif transaction_type == "Stock Out":
        return stock_before - quantity

    elif transaction_type == "Damaged Return":
        return stock_before

    return stock_before


def validate_stock_out(
    available_stock,
    requested_quantity
):
    """
    Prevent Stock Out transactions from
    exceeding the available inventory.
    """

    if requested_quantity <= 0:
        return False, "Quantity must be greater than zero."

    if requested_quantity > available_stock:
        return (
            False,
            "Requested quantity exceeds available stock."
        )

    return True, "Stock Out is valid."


def validate_new_product(
    products_df,
    product_id
):
    """
    Validate that a new Product ID does not
    already exist in the Products sheet.
    """

    product_id = str(product_id).strip()

    existing_ids = (
        products_df["Product ID"]
        .astype(str)
        .str.strip()
    )

    if product_id in existing_ids.values:
        return False, "Product ID already exists."

    return True, "Product ID is available."


def get_stock_status(
    quantity,
    minimum_quantity
):
    """
    Determine the current stock status.
    """

    if quantity <= 0:
        return "Out of Stock"

    elif quantity <= minimum_quantity:
        return "Low Stock"

    return "Available"
