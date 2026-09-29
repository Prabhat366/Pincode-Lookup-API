A FastAPI-based REST API for validating and looking up Indian pincode location details such as city, district, and state.

## Features

- Single pincode lookup
- Bulk pincode lookup
- Pincode validation
- Custom exception handling
- Handles invalid pincodes
- Handles pincodes that are not available
- Pydantic request and response validation
- Interactive API documentation with Swagger UI

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- REST API
- Postman

## Project Structure

```text
pincode-lookup-api/
│
├── main.py
├── models.py
├── exceptions.py
├── data.py
├── requirements.txt
├── .gitignore
└── README.md
