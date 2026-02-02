from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="HR Data API - Combined")

# Database setup for Employee Data
EMPLOYEE_DB_URL = "sqlite:///./employee_data.db"
employee_engine = create_engine(EMPLOYEE_DB_URL)
EmployeeSessionLocal = sessionmaker(bind=employee_engine)

# Database setup for Manager Reviews
REVIEW_DB_URL = "sqlite:///./manager_reviews.db"
review_engine = create_engine(REVIEW_DB_URL)
ReviewSessionLocal = sessionmaker(bind=review_engine)

Base = declarative_base()


# ==================== EMPLOYEE MODELS ====================

class Employee(Base):
    __tablename__ = "user_data_test_admin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)
    user_unique_id = Column(String)
    company_email_id = Column(String)
    permission_role = Column(String)
    employee_status = Column(String)
    employee_type = Column(String)
    date_of_joining = Column(String)
    date_of_exit = Column(String)
    tenure = Column(String)
    experience = Column(Integer)
    last_login = Column(String)
    latest_office_effective_from = Column(String)
    confirmation_status = Column(String)
    date_of_confirmation = Column(String)
    probation_period = Column(String)
    probation_start_date = Column(String)
    role = Column(String)
    role_name = Column(String)
    role_code = Column(String)
    team = Column(String)
    team_name = Column(String)
    team_code = Column(String)
    top_department = Column(String)
    departments_hierarchy = Column(String)
    group_company = Column(String)
    designation_title = Column(String)
    department = Column(String)
    department_code = Column(String)
    cost_center = Column(String)
    cost_center_name = Column(String)
    direct_manager = Column(String)
    direct_manager_email = Column(String)
    direct_manager_employee_id = Column(String)
    l2_manager = Column(String)
    l2_manager_email = Column(String)
    l2_manager_employee_id = Column(String)
    direct_reportees = Column(Integer)
    reportees = Column(Integer)
    reporting_manager = Column(String)
    primary_manager = Column(String)
    hod = Column(String)
    hod_email_id = Column(String)
    hod_employee_id = Column(String)
    hrbp_name = Column(String)
    hrbp_email_id = Column(String)
    hrbp_employee_id = Column(String)
    hrbp_role = Column(String)
    dotted_line_manager = Column(String)
    dotted_line_manager_email = Column(String)
    dotted_line_manager_employee_id = Column(String)
    dotted_reportees = Column(Integer)
    dotted_line_reportees = Column(String)
    attendance_policy = Column(String)
    shifts = Column(String)
    weeklyoff = Column(String)
    current_shifts = Column(String)
    shift_name = Column(String)
    attendance_pattern = Column(String)
    office_location = Column(String)
    office_city = Column(String)
    office_state = Column(String)
    office_country = Column(String)
    office_pincode = Column(String)
    office_region = Column(String)
    location_type = Column(String)
    work_location = Column(String)
    region = Column(String)
    geography = Column(String)
    current_fixed_annual_ctc = Column(Integer)
    joining_bonus = Column(Integer)
    relocation_bonus = Column(Integer)
    previous_company = Column(String)
    previous_compensation = Column(Integer)
    job_category = Column(String)
    band = Column(String)
    grade = Column(String)


class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    user_unique_id: Optional[str]
    company_email_id: Optional[str]
    permission_role: Optional[str]
    employee_status: Optional[str]
    employee_type: Optional[str]
    date_of_joining: Optional[str]
    date_of_exit: Optional[str]
    tenure: Optional[str]
    experience: Optional[int]
    last_login: Optional[str]
    latest_office_effective_from: Optional[str]
    confirmation_status: Optional[str]
    date_of_confirmation: Optional[str]
    probation_period: Optional[str]
    probation_start_date: Optional[str]
    role: Optional[str]
    role_name: Optional[str]
    role_code: Optional[str]
    team: Optional[str]
    team_name: Optional[str]
    team_code: Optional[str]
    top_department: Optional[str]
    departments_hierarchy: Optional[str]
    group_company: Optional[str]
    designation_title: Optional[str]
    department: Optional[str]
    department_code: Optional[str]
    cost_center: Optional[str]
    cost_center_name: Optional[str]
    direct_manager: Optional[str]
    direct_manager_email: Optional[str]
    direct_manager_employee_id: Optional[str]
    l2_manager: Optional[str]
    l2_manager_email: Optional[str]
    l2_manager_employee_id: Optional[str]
    direct_reportees: Optional[int]
    reportees: Optional[int]
    reporting_manager: Optional[str]
    primary_manager: Optional[str]
    hod: Optional[str]
    hod_email_id: Optional[str]
    hod_employee_id: Optional[str]
    hrbp_name: Optional[str]
    hrbp_email_id: Optional[str]
    hrbp_employee_id: Optional[str]
    hrbp_role: Optional[str]
    dotted_line_manager: Optional[str]
    dotted_line_manager_email: Optional[str]
    dotted_line_manager_employee_id: Optional[str]
    dotted_reportees: Optional[int]
    dotted_line_reportees: Optional[str]
    attendance_policy: Optional[str]
    shifts: Optional[str]
    weeklyoff: Optional[str]
    current_shifts: Optional[str]
    shift_name: Optional[str]
    attendance_pattern: Optional[str]
    office_location: Optional[str]
    office_city: Optional[str]
    office_state: Optional[str]
    office_country: Optional[str]
    office_pincode: Optional[str]
    office_region: Optional[str]
    location_type: Optional[str]
    work_location: Optional[str]
    region: Optional[str]
    geography: Optional[str]
    current_fixed_annual_ctc: Optional[int]
    joining_bonus: Optional[int]
    relocation_bonus: Optional[int]
    previous_company: Optional[str]
    previous_compensation: Optional[int]
    job_category: Optional[str]
    band: Optional[str]
    grade: Optional[str]

    class Config:
        from_attributes = True


# ==================== MANAGER REVIEW MODELS ====================

class ManagerReview(Base):
    __tablename__ = "manager_reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    manager_name = Column(String)
    manager_email = Column(String)
    manager_id = Column(String, index=True)
    employee_id = Column(String, index=True)
    employee_name = Column(String)
    employee_email = Column(String)
    department = Column(String, index=True)
    designation = Column(String)
    date_of_joining = Column(String)
    experience_years = Column(Integer)
    annual_ctc = Column(Integer)
    location = Column(String, index=True)
    review_date = Column(String, index=True)
    performance_score = Column(Integer)
    rating = Column(String, index=True)
    comments = Column(String)


class ManagerReviewResponse(BaseModel):
    id: int
    manager_name: str
    manager_email: str
    manager_id: str
    employee_id: str
    employee_name: str
    employee_email: str
    department: str
    designation: str
    date_of_joining: str
    experience_years: int
    annual_ctc: int
    location: str
    review_date: str
    performance_score: int
    rating: str
    comments: Optional[str]

    class Config:
        from_attributes = True


# ==================== DATABASE SESSIONS ====================

def get_employee_db():
    db = EmployeeSessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_review_db():
    db = ReviewSessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==================== API ENDPOINTS ====================

@app.get("/")
def root():
    return {
        "message": "HR Data API - Combined",
        "endpoints": {
            "employees": "/employees/ - Get all employee data (489 records)",
            "reviews": "/reviews/ - Get all manager reviews (488 records)"
        },
        "docs": "/docs"
    }


@app.get("/employees/", response_model=List[EmployeeResponse])
def get_all_employees(
    skip: int = 0,
    limit: int = 500,
    db: Session = Depends(get_employee_db)
):
    """Get all employee data"""
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees


@app.get("/reviews/", response_model=List[ManagerReviewResponse])
def get_all_reviews(
    skip: int = 0,
    limit: int = 500,
    db: Session = Depends(get_review_db)
):
    """Get all manager reviews"""
    reviews = db.query(ManagerReview).offset(skip).limit(limit).all()
    return reviews


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
