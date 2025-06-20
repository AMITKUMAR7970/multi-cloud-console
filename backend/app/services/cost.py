# Service logic for cost 
def get_cloud_costs(user):
    # Replace with real integration (AWS Cost Explorer, Azure Cost Management, etc.)
    # Here we return a mock response
    return {
        "aws": {"monthly_usd": 123.45},
        "azure": {"monthly_usd": 234.56},
        "gcp": {"monthly_usd": 99.99}
    }