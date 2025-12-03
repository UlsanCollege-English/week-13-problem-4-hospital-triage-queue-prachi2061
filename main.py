
def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients are dictionaries with:
      - "name": string
      - "severity": integer 1 (most urgent) to 5 (least urgent)
      - "arrival_order": integer, smaller means arrived earlier

    Priority rules:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.

    Return a list of names in the correct order. If k is 0 or there are
    no patients, return [].
    """
    if not patients or k <= 0:
        return []

    # Sort by (severity asc, arrival_order asc); Python's sort is stable,
    # so equal keys keep original input order.
    ordered = sorted(patients, key=lambda p: (p["severity"], p["arrival_order"]))

    # Take the first k and return their names
    return [p["name"] for p in ordered[:k]]
