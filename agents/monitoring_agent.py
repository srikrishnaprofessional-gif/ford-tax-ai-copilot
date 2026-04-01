def monitor_integrations():

    systems = [
        {"system": "ERP", "status": "success"},
        {"system": "Vertex", "status": "success"},
        {"system": "TaxDataHub", "status": "failed"}
    ]

    failures = [s for s in systems if s["status"] == "failed"]

    return failures