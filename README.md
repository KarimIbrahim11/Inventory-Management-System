# 📦 Inventory Management System

A Python-based Inventory Management System built with **Streamlit, Pandas, and Excel** to automate inventory operations, reduce manual errors, and create structured transaction data for business analysis.

---

## 📌 Project Overview

This project was built to solve common operational challenges caused by manually managing inventory through Excel.

The goal was not simply to replace Excel with a Python application, but to transform a manual inventory process into a more structured and data-driven workflow.

---

## 🔴 Business Problem

Before building the system, inventory management relied heavily on manual Excel updates.

This created several challenges:

- Manual stock updates after purchases and sales.
- Higher risk of data entry errors.
- No transaction history.
- Difficulty tracking why inventory increased or decreased.
- Manual product creation.
- Unstructured purchase and return processes.
- No clear separation between good and damaged returns.
- Difficulty tracking orders and packages related to transactions.
- Difficulty identifying low-stock products.
- Limited ability to analyze historical inventory movements.
- No centralized process connecting current inventory with historical transactions.

---

## 💡 Solution

I developed an **Inventory Management System** using:

- Python
- Streamlit
- Pandas
- Excel

The system centralizes inventory operations and automatically updates stock while maintaining structured transaction records.

---

# 🛠️ System Features

## 📥 Stock In

The system supports two different types of stock additions:

### 🛒 New Purchase

Used when new inventory is purchased from a supplier.

The system records:

- Supplier Name
- Purchase Price
- Quantity
- Notes
- Stock Before
- Stock After

The inventory quantity is automatically increased.

### ↩️ Good Return

Used when a previously sold product is returned in good condition and can be sold again.

The system records:

- Quantity
- Platform
- Order ID
- Package ID
- Notes
- Stock Before
- Stock After

The returned quantity is added back to the available inventory.

Separating **New Purchase** from **Good Return** makes it possible to identify the source of inventory increases and analyze them later.

---

## 📤 Stock Out

Used when products leave the inventory due to sales.

The system automatically:

- Deducts the sold quantity.
- Records the selling price.
- Records the sales platform.
- Records Order ID.
- Records Package ID.
- Records Notes.
- Calculates Stock Before.
- Calculates Stock After.

This provides better transaction traceability.

---

## ➕ New Product

The system allows users to create products that do not already exist in the inventory.

The user enters:

- Product ID
- Product Name
- Category
- Initial Quantity
- Minimum Quantity

The system then:

1. Creates the product in the **Products Sheet**.
2. Stores the initial stock.
3. Automatically records the first inventory transaction.

This eliminates the need to manually create the product in Excel.

---

## ↩️ Damaged Returns

Damaged returns are handled separately from inventory movements.

The system records:

- Return Date
- Product ID
- Product Name
- Quantity
- Platform
- Order ID
- Package ID
- Notes

Damaged products are **not added back to Available Stock**.

Damaged products are **not added back to Available Stock**.

This creates a clear distinction:

```text
Good Return → Stock +
Damaged Return → No Stock Change 
```
---

## 📜 Transaction History
Every inventory movement is stored in a structured transaction table. This creates a historical record of inventory movements instead of only maintaining the current stock quantity. 

**The transaction structure is:**
* Date
* Product ID
* Product Name
* Type
* Quantity
* Price
* Platform
* Order ID
* Package ID
* Stock Before
* Stock After
* Notes
* Quantity Type

---

## 🧠 Business Logic
The system follows clear inventory rules to ensure consistent operational transactions:

| Transaction Type | System Action | Description |
| :--- | :--- | :--- |
| 📥 **New Purchase** | `Stock +` | Increases available inventory |
| 🔄 **Good Return** | `Stock +` | Adds returned items back to sellable stock |
| 📤 **Stock Out** | `Stock -` | Deducts items upon sale or dispatch |
| ⚠️ **Damaged Return** | `No Change`| Logged for records, not added to sellable stock |

--- 
## 📊 Data & Analytics Opportunities
One of the main benefits of the system is that it produces structured business data that can be analyzed later. The data can later be connected to Power BI or Python to build an Inventory & Sales Analytics Dashboard.

**The data can be used for:**
- Sales trends.
- Top-selling products.
- Slow-moving products.
- Inventory Turnover.
- Low-stock analysis.
- Platform performance.
- Sales and revenue analysis.
- Supplier performance.
- New Purchases vs Good Returns.
- Good Returns vs Damaged Returns.
- Return analysis.
- Daily, weekly, and monthly performance.

---

## 🎯 Business Questions the Data Can Answer
The structured data can help answer questions such as:
* Which products are moving the fastest?
* Which products are slow-moving?
* Which platforms generate the highest sales?
* Which products require reordering?
* Is inventory growth coming from new purchases or good returns?
* Which products are consuming capital without enough movement?
* What is the return rate by product or platform?
* Which suppliers contribute most to inventory purchases?

---

## 🔄 Business Process
The project transforms the workflow from manual data entry to an automated, insights-driven process.

**Before (Manual):**
> Manual Data Entry ➔ Possible Errors ➔ Unstructured Data ➔ Difficult Analysis

**After (Automated):**
> User Transaction ➔ Automatic Stock Update ➔ Structured Transaction Data ➔ Business Analytics ➔ Better Decisions

---

## 🗂️ Data Structure

### 📦 Products Sheet
- Product ID
- Product Name
- Category
- Quantity
- Minimum Qty

### 📝 Transactions Sheet
- Date
- Product ID
- Product Name
- Type
- Quantity
- Price
- Platform
- Order ID
- Package ID
- Stock Before
- Stock After
- Notes
- Quantity Type

### ⚠️ Damaged Returns Sheet
- Return Date
- Product ID
- Product Name
- Quantity
- Platform
- Order ID
- Package ID
- Notes

---

## 🧰 Technology Stack
* **Programming:** Python
* **Application:** Streamlit
* **Data Processing:** Pandas
* **Data Storage:** Microsoft Excel
* **Analytics:** Python, Power BI

---

## 📸 Screenshots
*(Replace the links below with the actual paths to your images)*
- [Stock In](link-to-image)
- [Stock Out](link-to-image)
- [New Product](link-to-image)
- [Damaged Returns](link-to-image)
- [Transaction History](link-to-image)
- [Products](link-to-image)

---

## 🚀 Future Improvements
Possible future improvements include:
- [ ] Power BI Inventory Dashboard.
- [ ] Automated low-stock email alerts.
- [ ] Database integration instead of Excel.
- [ ] Sales forecasting.
- [ ] Reorder point prediction.
- [ ] Advanced inventory analytics.
- [ ] User authentication.
- [ ] Automated reporting.

---

## 🎯 Project Objective
The objective was not simply to replace Excel with Python. It was to transform a manual operational process into a **Data-Driven Process**:

`Manual Data Entry` ➔ `Automatic Stock Updates` ➔ `Structured Data` ➔ `Analytics` ➔ `Better Decisions`

This project combines: 
**Python + Streamlit + Pandas + Excel + Data Analysis + Automation + Business Process Understanding**

**The main approach behind the project is:**
> Understand the Business Problem ➔ Build a Practical Solution ➔ Structure the Data ➔ Generate Insights ➔ Support Better Decisions

