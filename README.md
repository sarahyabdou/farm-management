Farm Management System - DRF Assessment



A Django REST Framework-based API to manage users, farms, crops, and animals — built for the Bortoqala DRF Developer Assessment.



---




## 🚀 Features




\- ✅ JWT Authentication (register, login, refresh, profile)

\- ✅ Custom user model with phone number and address

\- ✅ CRUD for Farms, Crops, and Animals

\- ✅ Permissions: Users can only manage their own farms and related data

\- ✅ Postman collection included for easy testing



---



## 🛠️ Setup Instructions



1- Clone the repo



```bash

git clone https://github.com/sarahyabdou/farm-management.git

cd farm-management



2\. Create virtual environment and install dependencies

python -m venv venv

source venv/bin/activate     # on Windows use: venv\\Scripts\\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver



Authentication


| Action   | Endpoint                  | Method |

| -------- | ------------------------- | ------ |

| Register | `/api/user/register/` | POST   |

| Login    | `/api/token/`             | POST   |

| Refresh  | `/api/token/refresh/`     | POST   |

| Profile  | `/api/user/profile/`  | GET    |

GET



🌿 API Endpoints

Model	Endpoint Base	Description

Farms	/api/farm/farms/	Create / Read / Update / Delete

Crops	/api/farm/crops/	Create / Read / Update / Delete

Animals	/api/farm/animals/	Create / Read / Update / Delete



All endpoints require JWT Authorization: Bearer <access\_token>
 Permissions

Only the user who owns a farm can view, edit, or delete it. Users are not allowed to create crops or animals for farms they do not own. If a user attempts to access or modify resources they don’t have permission for, the API will return a 404 Notfound response.
A complete Postman collection is included for testing:


### Postman Collection
1. Located in `docs/postman/farm-api.postman_collection.json`
2. Includes:
   - All authentication flows
   - Farm management endpoints
   - Sample requests/responses



