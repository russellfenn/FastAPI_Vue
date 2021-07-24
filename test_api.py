from starlette.testclient import TestClient
from api import app, MathQuestion, MathResult
import pytest


@pytest.fixture
def math_question():
    return MathQuestion(arg1=5.2, arg2=2.3, operation="add")


def test_math_add(math_question: MathQuestion):
    client = TestClient(app)
    response = client.post("/math", data=math_question.json())
    print(response.json())
    assert response.status_code == 200
    result: MathResult = MathResult(**response.json())

    assert result.result == 7.5


def test_math_subtract(math_question: MathQuestion):
    math_question.operation = "subtract"
    client = TestClient(app)
    response = client.post("/math", data=math_question.json())
    print(response.json())
    assert response.status_code == 200
    result: MathResult = MathResult(**response.json())

    assert result.result == 2.9
    assert float(result.question.arg1) == 5.2
    assert result.question.operation == "subtract"
