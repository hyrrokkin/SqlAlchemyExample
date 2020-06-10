# -----------------------------------------------------------
# Пакет для хранения различных классов, реализующих каждую
# из связей SQLAlchemy
# -----------------------------------------------------------
from src.model import \
    one_to_many_bidirectional, \
    one_to_mane_unidirectional,\
    many_to_one_unidirectional, \
    many_to_one_bidirectional, \
    one_to_one_from_one_to_many, \
    one_to_many_from_many_to_one
