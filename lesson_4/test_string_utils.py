import pytest
from string_utils import StringUtils

stringUtils = StringUtils()


# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Пример: `capitilize("skypro") -> "Skypro"`
# Ниже представлены позитивные сценарии
# @pytest.mark.capitilize
@pytest.mark.xfail
@pytest.mark.parametrize('word1, result', [
    ("word", "Word"),
    ("s", "S"),
    ("Привет, Дима, как дела?", "Привет, Дима, как дела?"),
    # Баг. Код всегда заглавные буквы делает строчными. Баг оформлен
    ("hello Dima", "Hello dima"),
    ("сегодня 24 число", "Сегодня 24 число")
    ])
def test_positiv_capitilize(word1, result):
    word = StringUtils()
    res = word.capitilize(word1)
    assert res == result

# Ниже представлены негативные сценарии
@pytest.mark.parametrize('word1, result', [
    ("Word", "Word"),
    ("S", "S"),
    ("", ""),
    (" ", " "),
    ("01", "01"),
    ("24 negativ", "24 negativ")
    ])
def test_negativ_capitilize(word1, result):
    word = StringUtils()
    res = word.capitilize(word1)
    assert res == result


# Принимает на вход текст и удаляет пробелы в начале, если они есть
# Пример: `trim("   skypro") -> "skypro"`

# @pytest.mark.trip
@pytest.mark.parametrize('prob1, result', [
    (" Word", "Word"),
    ("  S", "S"),
    (" ", ""),
    ("   01", "01"),
    ("  24 negativ", "24 negativ"),
    ("            Hello     Dima", "Hello     Dima")
    ])
def test_positiv_trim(prob1, result):
    prob = StringUtils()
    res = prob.trim(prob1)
    assert res == result

# ниже представлены негативные кейсы
@pytest.mark.parametrize('prob1, result', [
    ("Word", "Word"),
    ("01", "01"),
    ("", ""),
    ])
def test_negativ_trim(prob1, result):
    prob = StringUtils()
    res = prob.trim(prob1)
    assert res == result


# Принимает на вход текст с разделителем и возвращает список строк. \n
# Параметры: \n
#  `string` - строка для обработки \n
# `delimeter` - разделитель строк. По умолчанию запятая (",") \n
# Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
# Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
# Ниже представлены положительные кейсы
@pytest.mark.parametrize('string, result', [
    ("Hello, are you", ['Hello', ' are you']),
    ("Было много дел, помыть посуду, убраться", ['Было много дел', ' помыть посуду', ' убраться']),
    ("1,2,3", ["1", "2", "3"])
    ])
def test_positiv_to_list(string, result):
    prob = StringUtils()
    res = prob.to_list(string)
    assert res == result


@pytest.mark.parametrize('string, delil, result', [
    ("1:2:3", ":", ['1', '2', '3']),
    ("Список дел: купить яйца", ":", ["Список дел", " купить яйца"]),
    ("Hello;world", ";", ["Hello", "world"])
    ])
def test_s_kov_to_list(string, delil, result):
    prob = StringUtils()
    res = prob.to_list(string, delil)
    assert res == result


@pytest.mark.parametrize('string, delil, result', [
    ("Список дел: купить яйца, овощи", ":", ["Список дел", " купить яйца, овощи"]),
    ("", "", []),
    (" ", "", []),
    ("   ", ",", [])
    ])
def test_negativ1_to_list(string, delil, result):
    prob = StringUtils()
    res = prob.to_list(string, delil)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("Список дел: купить яйца, овощи", ["Список дел: купить яйца", " овощи"]),
    ("", []),
    (" ", []),
    ("Hello", ["Hello"])
    ])
def test_negativ2_to_list(string, result):
    prob = StringUtils()
    res = prob.to_list(string)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Hi Alex", "i", True),
    ("Hello, Alex", "l", True),
    ("123456", "4", True),
    ("Phone 25", "25", True)
    ])
def test_positiv_conteins(string, symbol, result):
    prob = StringUtils()
    res = prob.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("", "", True),
    ("   ", "", True),
    ("12345", "8", False),
    ("Alex", "X", False)      # Стоит уточнить у заказчика. Возможно должно быть - True
    ])
def test_negativ_conteins(string, symbol, result):
    prob = StringUtils()
    res = prob.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Hi Alex", "i", "H Alex"),
    ("Hello, Alex", "l", "Heo, Aex"),
    ("123456", "4", "12356"),
    ("Phone 25", "25", "Phone ")
    ])
def test_positiv_delete_symbol(string, symbol, result):
    prob = StringUtils()
    res = prob.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Hi Alex", "", "Hi Alex"),
    ("1234567 number", "8", "1234567 number"),
    ("Alex", "  f", "Alex"),
    ("", "", ""),
    (" ", " ", ""),
    ])
def test_negativ_delete_symbol(string, symbol, result):
    prob = StringUtils()
    res = prob.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Hi Alex", "i", False),
    ("Hello, Alex", "h", False),    # Стоит уточнить у заказчика. Возможно должно быть - True
    ("123456", "1", True),
    ("123456 hi", "2", False),
    ("Phone 25", "Pho", True)
    ])
def test_positiv_starts_with(string, symbol, result):
    prob = StringUtils()
    res = prob.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("", "", True),
    ("Phone 25", "", True),  # Стоит уточнить у заказчика. Возможно должно быть - False
    (" ", " ", True)
    ])
def test_negativ_starts_with(string, symbol, result):
    prob = StringUtils()
    res = prob.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Hi Alex", "i", False),
    ("Hello, Alex", "O", False),             # Стоит уточнить у заказчика. Возможно должно быть - True
    ("123456", "6", True),
    ("123456", "65", False),
    ("123456 hi", "h", False),
    ("Phone 25", "25", True),
    ("Hello23, world23", "world23", True)
    ])
def test_positiv_end_with(string, symbol, result):
    prob = StringUtils()
    res = prob.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("", "", True),
    (" ", " ", True),
    ("123456 hi", "", True),  # Стоит уточнить у заказчика. Возможно должно быть - False
    ])
def test_negativ_end_with(string, symbol, result):
    prob = StringUtils()
    res = prob.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("Hi Alex", False),
    ("123456", False),
    ("123456 hi", False),
    ("", True),
    ("     ", True),
    ])
def test_positiv_is_empty(string, result):
    prob = StringUtils()
    res = prob.is_empty(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ("     hi", False),
    ])
def test_negativ_is_empty(string, result):
    prob = StringUtils()
    res = prob.is_empty(string)
    assert res == result


@pytest.mark.parametrize('string, djoner, result', [
    ([1,2,3], ",", "1,2,3"),
    ([1,2,3,4], ";", "1;2;3;4"),
    (["Hel", "lo"], ",", "Hel,lo"),
    ([1,2,3, "Hel", "lo"], ",", "1,2,3,Hel,lo")
    ])
def test_positiv1_list_to_string(string, djoner, result):
    prob = StringUtils()
    res = prob.list_to_string(string, djoner)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ([1,2,3], "1, 2, 3"),
    (["Hel", "lo"], "Hel, lo"),
    ([1,2,3, "Hel", "lo"], "1, 2, 3, Hel, lo")
    ])
def test_positiv2_list_to_string(string, result):
    prob = StringUtils()
    res = prob.list_to_string(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
    ([], ""),
    (["", ""], ", "),       # Стоит уточнить у заказчика
    ([" ", " "], " ,  ")    # Стоит уточнить у заказчика
    ])
def test_negativ_list_to_string(string, result):
    prob = StringUtils()
    res = prob.list_to_string(string)
    assert res == result
