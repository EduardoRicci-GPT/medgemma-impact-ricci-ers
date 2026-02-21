def generate_audit_summary(data):
    """
    Generate an audit summary from the provided data.
    
    Parameters:
    data (list): A list of audit records.
    
    Returns:
    dict: A summary of the audit results.
    """
    summary = {
        'total_records': len(data),
        'valid_records': len([d for d in data if d['valid']]),
        'invalid_records': len([d for d in data if not d['valid']]),
    }
    return summary

def print_audit_summary(summary):
    """
    Print the audit summary.
    
    Parameters:
    summary (dict): The summary information to print.
    """
    print(f"Total Records: {summary['total_records']}")
    print(f"Valid Records: {summary['valid_records']}")
    print(f"Invalid Records: {summary['invalid_records']}")
