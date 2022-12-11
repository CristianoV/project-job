from typing import Union, List, Dict

from .jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    data = [data_list for data_list in data]
    salary = [int(x["max_salary"]) for x in data if x["max_salary"].isdigit()]
    max_salary = max(salary)
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    data = [data_list for data_list in data]
    salary = [int(x["min_salary"]) for x in data if x["min_salary"].isdigit()]
    max_salary = min(salary)
    return max_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        (type(salary) == int or type(salary) == str)
        and job.keys() == {"min_salary", "max_salary"}
        and (
            type(job["min_salary"]) == str
            and type(job["max_salary"]) == str
            or type(job["min_salary"]) == int
            and type(job["max_salary"]) == int
        )
        and int(job["min_salary"]) < int(job["max_salary"])
        and int(job["min_salary"]) >= 0 < int(job["max_salary"])
    ):
        if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
            return True
        else:
            return False
    else:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list
