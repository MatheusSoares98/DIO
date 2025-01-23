import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Receiving request to verify CPF.')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    if cpf:
        is_valid = verify_cpf(cpf)
        return func.HttpResponse(f"The CPF {cpf} is {'valid' if is_valid else 'invalid'}.")
    else:
        return func.HttpResponse(
            "Please provide the CPF in the query string or request body.",
            status_code=400
        )


def verify_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(cpf_segment, weight):
        total = sum(int(digit) * factor for digit, factor in zip(cpf_segment, range(weight, 1, -1)))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf[:9], 10)
    second_digit = calculate_digit(cpf[:10], 11)

    return cpf[9] == str(first_digit) and cpf[10] == str(second_digit)
