from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    data = [data_list for data_list in data]
    industries = set([x["industry"] for x in data if x["industry"] != ""])
    return list(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
