
land_records = {
    "John Doe": {
        "personal_details": {
            "parentage": "Robert Doe",
            "address": "123 Green Street",
            "contact_number": "9876543210"
        },
        "land_details": [
            {
                "mouza": "Greenfield",
                "khasra_number": "101",
                "type_of_land": "Agricultural",
                "total_area": "10 Kanals",
                "ownership_share": "Full"
            }
        ],
        "revenue_information": {
            "annual_tax": 1500,
            "payment_status": "Paid"
        }
    }
}

# Function to display all records
def display_all_records():
    print("\n--- All Land Records ---")
    for owner, details in land_records.items():
        print(f"Owner: {owner}")
        for section, info in details.items():
            print(f"  {section.capitalize()}: {info}")
    print()
display_all_records()    

# Function to add a new record
def add_land_record(owner_name, personal_details, land_details, revenue_info):
    land_records.setdefault(owner_name, {})
    land_records[owner_name]['personal_details'] = personal_details
    land_records[owner_name]['land_details'] = [land_details]
    land_records[owner_name]['revenue_information'] = revenue_info
    print(f"\nRecord added for {owner_name}.\n")

# # Function to update payment status
def update_payment_status(owner_name, new_status):
    if owner_name in land_records:
        land_records[owner_name]['revenue_information']['payment_status'] = new_status
        print(f"\nPayment status updated for {owner_name}.\n")
    else:
        print("\nOwner not found.\n")

# # Function to get details of an owner by mouza
def get_owner_by_mouza(mouza_name):
    for owner, details in land_records.items():
        for land in details.get("land_details", []):
            if land.get("mouza") == mouza_name:
                return {
                    "name": owner,
                    "parentage": details["personal_details"]["parentage"],
                    "address": details["personal_details"]["address"]
                }
    return None

# # Function to delete a record
def delete_owner_record(owner_name):
    removed = land_records.pop(owner_name, None)
    if removed:
        print(f"\nRecord for {owner_name} deleted.\n")
    else:
        print("\nOwner not found.\n")

# Function to show revenue statistics
def show_revenue_stats():
    total_tax = sum(
        details['revenue_information']['annual_tax']
        for details in land_records.values()
    )
    unpaid_owners = [
        owner for owner, details in land_records.items()
        if details['revenue_information']['payment_status'] == "Unpaid"
    ]
    print("\n--- Revenue Statistics ---")
    print(f"Total Tax Collected: {total_tax}")
    print(f"Owners with Unpaid Tax: {unpaid_owners}\n")

# # Main Execution
# display_all_records()

# Adding a new record
add_land_record(
    "Jane Smith",
    personal_details={
        "parentage": "Emma Smith",
        "address": "456 Hilltop Lane",
        "contact_number": "8765432109"
    },
    land_details={
        "mouza": "Meadowview",
        "khasra_number": "202",
        "type_of_land": "Residential",
        "total_area": "3 Marlas",
        "ownership_share": "Joint"
    },
    revenue_info={
        "annual_tax": 2000,
        "payment_status": "Unpaid"
    }
)

display_all_records()

# Updating payment status
update_payment_status("Jane Smith", "Paid")
display_all_records()

# Getting owner details by mouza
mouza_result = get_owner_by_mouza("Greenfield")
print("\n--- Owner Details by Mouza ---")
print(mouza_result)

# Deleting a record
delete_owner_record("John Doe")
display_all_records()

# Show revenue statistics
show_revenue_stats()
