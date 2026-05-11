# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    valid_parcels = []
    for code in parcel_codes:
        if code == "DAMAGED":
            print("Skipped damaged parcel")
            continue

        if code == "STOP":
            print("Critical error: Stopping scan")
            break

        print(f"Scanned parcel: {code}")
        valid_parcels.append(code)
    else:
        print("All parcels have been scanned successfully.")
    
    return valid_parcels