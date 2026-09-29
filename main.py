from fastapi import FastAPI

from exceptions import (
    PinCodeNotFoundError,
    pin_code_not_found_handler,
    InvalidPinCodeError,
    invalid_pincode_handler
)

from models import LocationResponse, BulkResponse, BulkRequest
from data import pincode_db


app = FastAPI(
    title="Pincode Lookup API",
    description="Autocode district and state name from pincode during checkout"
)


app.add_exception_handler(
    PinCodeNotFoundError,
    pin_code_not_found_handler
)

app.add_exception_handler(
    InvalidPinCodeError,
    invalid_pincode_handler
)


@app.get("/")
def root():
    return {
        "Message": "Welcome to our API"
    }


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):

    result = []
    missing = []

    for code in request.pincodes:

        if code in pincode_db:
            result.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(result),
        not_found=len(missing),
        results=result,
        missing=missing
    )


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code: str):

    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(
            code,
            "Must be exactly 6 digits"
        )

    if code not in pincode_db:
        raise PinCodeNotFoundError(code)

    return pincode_db[code]
    