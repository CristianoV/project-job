from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0]
        == {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}
    )
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")[1]
        == {'salary': '3000', 'title': 'Motorista', 'type': 'full time'}
    )
