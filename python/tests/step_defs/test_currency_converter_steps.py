import pytest
from pytest_bdd import parsers, scenario, given, when, then


@scenario("../features/currency_converter.feature", "Add two numbers")
def test_add_two_numbers():
    pass


@given(parsers.parse("the first number is {number:d}"), target_fixture="first_number")
def first_number(number):
    return number


@given(parsers.parse("the second number is {number:d}"), target_fixture="second_number")
def second_number(number):
    return number


@when(parsers.parse("the two numbers are added"), target_fixture="add_result")
def adding_two_numbers(first_number, second_number):
    return first_number + second_number


@then(parsers.parse("the result should be {expected:d}"))
def add_result_should_be(add_result, expected):
    assert add_result == expected
