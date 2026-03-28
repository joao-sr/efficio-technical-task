import pytest
from src.parsers.data_parser import merge_company_data

def test_merge_company_with_hierarchy():
    # Case 1: Company with hierarchy info
    company = {
        "duns": "081466849",
        "primary_name": "Microsoft Corporation",
        "start_date": "1975"
    }
    hierarchy = {
        "parent_duns": None,
        "hierarchy_level": 1
    }
    merged = merge_company_data(company, hierarchy)
    assert merged["duns"] == "081466849"
    assert merged["primary_name"] == "Microsoft Corporation"
    assert merged["parent_duns"] is None
    assert merged["hierarchy_level"] == 1

    # Case 2: Subsidiary with parent
    company2 = {
        "duns": "690763115",
        "primary_name": "MICROSOFT JAPAN CO., LTD.",
        "start_date": "1986-02"
    }
    hierarchy2 = {
        "parent_duns": "081466849",
        "hierarchy_level": 2
    }
    merged2 = merge_company_data(company2, hierarchy2)
    assert merged2["parent_duns"] == "081466849"
    assert merged2["hierarchy_level"] == 2

    # Case 3: Company not in hierarchy (no hierarchy dict)
    company3 = {
        "duns": "999999999",
        "primary_name": "Some Other Corp"
    }
    # Simulate missing hierarchy (hierarchy could be None or empty)
    hierarchy3 = None
    merged3 = merge_company_data(company3, hierarchy3)
    assert merged3["duns"] == "999999999"
    assert merged3.get("parent_duns") is None
    assert merged3.get("hierarchy_level") is None