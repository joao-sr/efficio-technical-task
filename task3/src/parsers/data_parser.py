def merge_company_data(company_data_block: dict, company_family_data: dict):
    """Enrich company data with hierarchy data"""
    ## receive company data
    # do stuff

    # receive family tree data
    if company_family_data is None:
        company_family_data = {}

    # create a new joined dictionary with data from both sources
    merged_data = {}
    merged_data['duns'] = company_data_block.get('duns')
    merged_data['primary_name'] = company_data_block.get('primary_name')
    merged_data['start_date'] = company_data_block.get('start_date')

    merged_data['parent_duns'] = company_family_data.get('parent_duns')
    merged_data['hierarchy_level'] = company_family_data.get('hierarchy_level')

    return merged_data



    
