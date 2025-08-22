import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_book_appears_in_dictionary_after_adding(collector):
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()

def test_book_not_added_if_name_longer_than_40_characters(collector):
    long_name = "Очень длинное название книги, которое точно больше сорока символов"
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()

def test_book_not_added_twice(collector):
    collector.add_new_book("Дюна")
    collector.add_new_book("Дюна")
    assert list(collector.get_books_genre().keys()).count("Дюна") == 1

@pytest.mark.parametrize("genre", ['Фантастика', 'Мультфильмы'])
def test_genre_is_set_if_allowed(collector, genre):
    collector.add_new_book("Книга")
    collector.set_book_genre("Книга", genre)
    assert collector.get_book_genre("Книга") == genre

def test_books_with_specific_genre_are_returned(collector):
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга2", "Фантастика")
    assert set(collector.get_books_with_specific_genre("Фантастика")) == {"Книга1", "Книга2"}

def test_books_with_age_restriction_not_in_children_list(collector):
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Детективы")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга2", "Фантастика")
    assert collector.get_books_for_children() == ["Книга2"]

def test_book_added_to_favorites(collector):
    collector.add_new_book("Книга")
    collector.add_book_in_favorites("Книга")
    assert "Книга" in collector.get_list_of_favorites_books()

def test_book_not_duplicated_in_favorites(collector):
    collector.add_new_book("Книга")
    collector.add_book_in_favorites("Книга")
    collector.add_book_in_favorites("Книга")
    assert collector.get_list_of_favorites_books().count("Книга") == 1

def test_book_removed_from_favorites(collector):
    collector.add_new_book("Книга")
    collector.add_book_in_favorites("Книга")
    collector.delete_book_from_favorites("Книга")
    assert "Книга" not in collector.get_list_of_favorites_books()