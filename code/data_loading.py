"""
Selected core logic from the Inventory Management System.

The complete application contains 1,900+ lines of Python code.
This file contains selected data-loading and validation logic
for portfolio demonstration purposes.
"""

import pandas as pd
from pathlib import Path


# Excel workbook used by the system
EXCEL_FILE = Path("Inventory.xlsx")


def load_products():
    """
    Load and validate the Products sheet.

    Expected columns:
    Product ID | Product Name | Category | Quantity | Minimum Qty
    """

    df = pd.read_excel(EXCEL_FILE, sheet_name="Products")

    required_columns = [
        "Product ID",
        "Product Name",
        "Category",
        "Quantity",
        "Minimum Qty"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns in Products sheet: {missing_columns}"
        )

    # Standardize Product IDs
    df["Product ID"] = (
        df["Product ID"]
        .astype(str)
        .str.strip()
    )

    # Ensure numeric stock fields
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    ).fillna(0)

    df["Minimum Qty"] = pd.to_numeric(
        df["Minimum Qty"],
        errors="coerce"
    ).fillna(0)

    return df


def load_transactions():
    """
    Load and validate inventory transaction history.
    """

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Transactions"
    )

    required_columns = [
        "Date",
        "Product ID",
        "Product Name",
        "Type",
        "Quantity",
        "Price",
        "Platform",
        "Order ID",
        "Package ID",
        "Stock Before",
        "Stock After",
        "Notes",
        "Quantity Type"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns in Transactions sheet: {missing_columns}"
        )

    df["Product ID"] = (
        df["Product ID"]
        .astype(str)
        .str.strip()
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    ).fillna(0)

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    ).fillna(0)

    df["Stock Before"] = pd.to_numeric(
        df["Stock Before"],
        errors="coerce"
    ).fillna(0)

    df["Stock After"] = pd.to_numeric(
        df["Stock After"],
        errors="coerce"
    ).fillna(0)

    return df


def load_damaged_returns():
    """
    Load damaged returns separately from available inventory.
    """

    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name="Damaged Returns"
    )

    required_columns = [
        "Return Date",
        "Product ID",
        "Product Name",
        "Quantity",
        "Platform",
        "Order ID",
        "Package ID",
        "Notes"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns in Damaged Returns sheet: "
            f"{missing_columns}"
        )

    df["Product ID"] = (
        df["Product ID"]
        .astype(str)
        .str.strip()
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    ).fillna(0)

    return df
