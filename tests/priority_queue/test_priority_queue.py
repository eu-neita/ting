import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    with pytest.raises(IndexError) as excinfo:
        priority_queue.search(1)
    assert str(excinfo.value) == "Índice Inválido ou Inexistente"

    priority_queue.enqueue({'qtd_linhas': 20})
    assert len(priority_queue.regular_priority) == 1

    priority_queue.dequeue()
    assert len(priority_queue.regular_priority) == 0

    priority_queue.enqueue({'qtd_linhas': 10})
    priority_queue.enqueue({'qtd_linhas': 1})
    assert len(priority_queue.high_priority) == 1

    priority_queue.enqueue({'qtd_linhas': 2})
    assert priority_queue.search(1).get('qtd_linhas') == 2
