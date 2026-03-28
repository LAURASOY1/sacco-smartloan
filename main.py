from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

INTEREST_RATE = 0.12  # 12% annual
loan_records = []

def calculate_net_salary(salary):
    nhif = 1700  # simplified
    nssf = 200   # simplified
    return salary - nhif - nssf

def calculate_affordability(net_salary):
    return net_salary / 3  # must retain 1/3

def credit_score(salary, loan):
    ratio = loan / salary
    if ratio <= 2:
        return 80, "Low Risk ✅"
    elif ratio <= 3:
        return 60, "Medium Risk ⚠️"
    else:
        return 40, "High Risk ❌"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/loan", response_class=HTMLResponse)
def process_loan(
    request: Request,
    name: str = Form(...),
    salary: float = Form(...),
    loan_amount: float = Form(...),
    months: int = Form(...)
):
    net_salary = calculate_net_salary(salary)
    max_loan = net_salary * 4
    monthly_limit = calculate_affordability(net_salary)

    interest = loan_amount * INTEREST_RATE
    total = loan_amount + interest
    monthly_payment = total / months

    score, risk = credit_score(salary, loan_amount)

    if loan_amount > max_loan:
        result = {
            "status": "Rejected ❌",
            "reason": "Exceeds SACCO limit (4× net salary)",
        }
    elif monthly_payment > monthly_limit:
        result = {
            "status": "Rejected ❌",
            "reason": "Monthly repayment exceeds 1/3 salary rule",
        }
    else:
        result = {
            "status": "Approved ✅",
            "net_salary": round(net_salary, 2),
            "interest": round(interest, 2),
            "total": round(total, 2),
            "monthly": round(monthly_payment, 2),
            "score": score,
            "risk": risk
        }

    loan_records.append({
        "name": name,
        "loan": loan_amount,
        "status": result["status"]
    })

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "name": name,
        "history": loan_records
    })
