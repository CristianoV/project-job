from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "word") == 382
    assert count_ocurrences("data/jobs.csv", "WORD") == 382
    assert count_ocurrences("data/jobs.csv", "word") != 381
    assert count_ocurrences("data/jobs.csv", "WORD") != 381
