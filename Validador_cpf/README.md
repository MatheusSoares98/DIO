# CPF Validator API

This project is an Azure Function HTTP trigger that validates a Brazilian CPF (Cadastro de Pessoa Física). It receives a CPF, verifies its validity using standard validation rules, and returns a response indicating whether the CPF is valid or not.

## Features

- **Validation Rules**:
  - Ensures the CPF has 11 digits.
  - Rejects CPFs with all digits repeated (e.g., `11111111111`).
  - Calculates and validates the check digits using the CPF algorithm.
- **Flexible Input**:
  - Accepts the CPF via query string or JSON in the request body.
- **Response**:
  - Returns a message stating whether the CPF is valid or invalid.
  - Provides an error message if the CPF is not provided.

## Endpoints

### HTTP Method: `POST`

#### Query String Parameter:
- `cpf`: The CPF to validate.

#### Request Body (optional):
```json
{
  "cpf": "12345678909"
}
