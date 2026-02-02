# HR Data API - Combined

Single API with both Employee Data and Manager Review endpoints.

## 🚀 Start the API

```bash
cd hr_data_api
source ../venv/bin/activate
uvicorn main:app --reload --port 8000
```

Or run directly:
```bash
python main.py
```

## 📍 Endpoints

### Root
```
GET http://localhost:8000/
```

### Employee Data (489 records)
```
GET http://localhost:8000/employees/
GET http://localhost:8000/employees/?limit=500
```

### Manager Reviews (488 records)
```
GET http://localhost:8000/reviews/
GET http://localhost:8000/reviews/?limit=500
```

### Interactive Documentation
```
http://localhost:8000/docs
```

## 📊 Data Sources

- **employee_data.db** - 489 employees with 76 fields
- **manager_reviews.db** - 488 performance reviews with 16 fields

## 🧪 Test

```bash
# Get all employees
curl http://localhost:8000/employees/

# Get all reviews
curl http://localhost:8000/reviews/

# Check API status
curl http://localhost:8000/
```
