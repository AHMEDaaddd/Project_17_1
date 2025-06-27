"""Модуль models.py.

Содержит классы для работы с продуктами и категориями.
"""


class Product:
    """Класс для представления товара."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализация экземпляра товара."""
        if quantity == 0:
            raise (ValueError("Товар с нулевым количеством не может быть добавлен"))
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name} ({self.quantity} шт.) - {self.price} руб."


class ZeroQuantityError(Exception):
    """Исключение: попытка добавить товар с нулевым количеством."""

    def __init__(
        self, message: str = "Товар с нулевым количеством не может быть добавлен"
    ) -> None:
        """Инициализация исключения с сообщением."""
        self.message = message
        super().__init__(self.message)


class Category:
    """Категория товаров магазина."""

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Создаёт категорию с названием, описанием и списком продуктов."""
        self.name = name
        self.description = description
        self.products = products

    def add_product(self, product: Product) -> bool:
        """Добавляет продукт в категорию с обработкой исключений."""
        try:
            if product.quantity == 0:
                raise ZeroQuantityError()
        except ZeroQuantityError as e:
            print(e)
            return False
        else:
            self.products.append(product)
            print("Продукт успешно добавлен")
            return True
        finally:
            print("Обработка добавления продукта завершена")

    def middle_price(self) -> float:
        """Возвращает среднюю цену товаров в категории (или 0 при отсутствии товаров)."""
        try:
            if not self.products:
                raise ZeroDivisionError
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0
