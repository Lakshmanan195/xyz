from phone_location_finder import get_phone_location

# Hardcoded phone number with country code
phone_number = "+919962177272"  # Replace with your actual phone number

# Get location information
result = get_phone_location(phone_number)

# Print the results
print("\nPhone Number Information:")
print(f"Valid: {result['valid']}")
print(f"Location: {result['location']}")
print(f"Carrier: {result['carrier']}")
print(f"Country Code: {result['country_code']}")
print(f"National Number: {result['national_number']}")
print(f"Coordinates: {result['coordinates']}")