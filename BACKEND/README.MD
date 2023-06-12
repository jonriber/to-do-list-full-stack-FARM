### INSTALL REQUIREMENTS

## COMMAND TO INSTALL VIRTAL ENVIRONMENT
 - python -m venv backend
## ACTIVATE/DESACTIVATE

.\backend\Scripts\activate

## INSTALL PACKAGES INSIDE REQUIREMENT.TXT

RUN: pip install -r requirements.txt

## INITIALIZE API SERVICE
- using uvicorn ---> run: uvicorn main:app --reload
- Access it through http://127.0.0.1:8000 in your brownser
- Access API docs: http://127.0.0.1:8000/docs


