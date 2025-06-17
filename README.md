# 🛒 Django Product Listing API

A beginner-friendly Django REST Framework project for listing products with:

- 🔍 Search by name (`?search=shirt`)
- 📂 Filter by category (`?category=Clothing`)
- 💰 Filter by price range (`?min_price=100&max_price=1000`)
- 📄 Pagination with page number and page size (`?page=2&page_size=5`)

---

## 🚀 How to Run the Project

1. Clone the repo:

2. Install dependencies:

3. Run migrations:

5. Run the server:

6. Open in browser:
- Admin: `http://127.0.0.1:8000/admin/`
- API: `http://127.0.0.1:8000/api/products/`

---

## 🔍 Example API URLs

| Action | URL |
|--------|-----|
| All products | `/api/products/` |
| Search by name | `/api/products/?search=shirt` |
| Filter by category | `/api/products/?category=Clothing` |
| Filter by price | `/api/products/?min_price=300&max_price=1000` |
| Page 2 | `/api/products/?page=2` |
| Custom page size | `/api/products/?page_size=3` |

---

## ✅ Features Included

- Django REST Framework setup
- Product model (name, category, price)
- Admin panel to manage products
- API to list products
- Filter by category
- Search by product name
- Filter by price range
- Pagination with page number & page size

---
.
