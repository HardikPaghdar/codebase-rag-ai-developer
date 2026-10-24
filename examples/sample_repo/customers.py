def validate_customer(name: str, email: str) -> None:
    if not name.strip():
        raise ValueError('Name is required')
    if '@' not in email:
        raise ValueError('Email must contain @')

def create_customer(name: str, email: str) -> dict:
    validate_customer(name, email)
    return {'name': name.strip(), 'email': email.lower().strip()}
