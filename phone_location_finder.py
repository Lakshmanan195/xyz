import phonenumbers
from phonenumbers import geocoder, carrier
import requests

def get_phone_location(phone_number):
    """
    Get location information for a given phone number including precise coordinates.
    Args:
        phone_number (str): Phone number with country code (e.g. '+1234567890')
    Returns:
        dict: Dictionary containing location, carrier and coordinate information
    """
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Get the location (country/region)
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Get the carrier
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        # Check if the number is valid
        is_valid = phonenumbers.is_valid_number(parsed_number)
        
        # Get coordinates using NumverifyAPI (you'll need to sign up for an API key)
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                latitude = data.get('latitude', 'Unknown')
                longitude = data.get('longitude', 'Unknown')
            else:
                latitude = 'Unknown'
                longitude = 'Unknown'
        except:
            latitude = 'Unknown'
            longitude = 'Unknown'
        
        return {
            "valid": is_valid,
            "location": location if location else "Unknown",
            "carrier": service_provider if service_provider else "Unknown",
            "country_code": f"+{parsed_number.country_code}",
            "national_number": parsed_number.national_number,
            "coordinates": {
                "latitude": latitude,
                "longitude": longitude
            }
        }
    except Exception as e:
        return {
            "error": str(e),
            "valid": False,
            "location": "Unknown",
            "carrier": "Unknown",
            "coordinates": {
                "latitude": "Unknown",
                "longitude": "Unknown"
            }
        }

if __name__ == "__main__":
    # Example usage
    phone_number = input("Enter phone number with country code (e.g. +1234567890): ")
    result = get_phone_location(phone_number)
    
    print("\nPhone Number Information:")
    print("-" * 25)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Valid Number: {result['valid']}")
        print(f"Location: {result['location']}")
        print(f"Carrier: {result['carrier']}")
        print(f"Country Code: {result['country_code']}")
        print(f"National Number: {result['national_number']}")