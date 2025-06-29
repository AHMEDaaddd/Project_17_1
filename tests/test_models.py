import pytest

from src.models import Category, Product, ZeroQuantityError


def test_product_zero_quantity() -> None:
    with pytest.raises(ValueError) as exc_info:
        Product("Товар", "Описание", 100.0, 0)
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)


def test_middle_price_non_empty_category() -> None:
    p1 = Product("Продукт1", "Описание", 100, 5)
    p2 = Product("Продукт2", "Описание", 200, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.middle_price() == 150


def test_middle_price_empty_category() -> None:
    category = Category("Пустая", "Описание", [])
    assert category.middle_price() == 0


def test_middle_price_empty():
    c = Category("Test", "Desc", [])
    assert c.middle_price() == 0


def test_middle_price_correct():
    p1 = Product("A", "D", 100, 1)
    p2 = Product("B", "D", 200, 1)
    c = Category("Test", "Desc", [p1, p2])
    assert c.middle_price() == 150


def test_add_product_success(capsys) -> None:
    category = Category("Категория", "Описание", [])
    product = Product("Продукт", "Описание", 100, 5)
    result = category.add_product(product)
    captured = capsys.readouterr().out
    assert result is True
    assert "Продукт успешно добавлен" in captured
    assert "Обработка добавления продукта завершена" in captured


def test_add_product_failure(capsys) -> None:
    category = Category("Категория", "Описание", [])

    class FakeProduct(Product):
        def __init__(self):
            self.quantity = 0
            self.name = "Фейк"
            self.description = "Описание"
            self.price = 0

    result = category.add_product(FakeProduct())
    captured = capsys.readouterr().out
    assert result is False
    assert "Товар с нулевым количеством не может быть добавлен" in captured
    assert "Обработка добавления продукта завершена" in captured
