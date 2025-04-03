import math

# Earth radius in kilometers
EARTH_RADIUS = 6371.0

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth specified in decimal degrees of latitude and longitude.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Distance in kilometers
    return EARTH_RADIUS * c

def circle_area(radius_km):
    """Calculate the area of a circle with given radius in km²."""
    return math.pi * (radius_km ** 2)

def circle_intersection_area(lat1, lon1, radius1_km, lat2, lon2, radius2_km):
    """
    Calculate the approximate intersection area of two circles on Earth's surface.
    
    This is an approximation that works well for small distances.
    For very large circles or circles near poles, more complex calculations would be needed.
    """
    d = haversine_distance(lat1, lon1, lat2, lon2)
    
    # If circles don't intersect
    if d >= radius1_km + radius2_km:
        return 0
    
    # If one circle is inside the other
    if d <= abs(radius1_km - radius2_km):
        smaller_radius = min(radius1_km, radius2_km)
        return circle_area(smaller_radius)
    
    # Calculate intersection area using circle segment formula
    r1_sq = radius1_km ** 2
    r2_sq = radius2_km ** 2
    
    # Calculate the areas of the two circle segments
    d1 = (r1_sq - r2_sq + d ** 2) / (2 * d)
    d2 = d - d1
    
    # Calculate the areas of the two circular segments
    a1 = r1_sq * math.acos(d1 / radius1_km) - d1 * math.sqrt(r1_sq - d1 ** 2)
    a2 = r2_sq * math.acos(d2 / radius2_km) - d2 * math.sqrt(r2_sq - d2 ** 2)
    
    return a1 + a2

def is_potentially_two_phones_for_one_person(lat1, lon1, radius1_km, lat2, lon2, radius2_km, threshold=0.5):
    """
    Determine if two location circles potentially represent the same person with two phones.
    
    Parameters:
    - lat1, lon1: Latitude and longitude of first circle center
    - radius1_km: Radius of first circle in kilometers
    - lat2, lon2: Latitude and longitude of second circle center
    - radius2_km: Radius of second circle in kilometers
    - threshold: Minimum overlap ratio to consider as same person
    
    Returns:
    - Boolean indicating if the circles overlap enough to potentially be the same person
    """
    area1 = circle_area(radius1_km)
    area2 = circle_area(radius2_km)
    
    intersection_area = circle_intersection_area(lat1, lon1, radius1_km, lat2, lon2, radius2_km)
    
    first_area_share = intersection_area / area1
    second_area_share = intersection_area / area2
    
    return min(first_area_share, second_area_share) > threshold

# Example usage with coordinates (latitude, longitude) and radius in kilometers
# Circle A centered at 40.7128° N, 74.0060° W (New York) with 1km radius
# Circle B centered at 40.7150° N, 74.0080° W (nearby in New York) with 0.8km radius
lat1, lon1 = 40.7128, -74.0060
radius1_km = 1.0

lat2, lon2 = 40.7250, -74.0080
radius2_km = 0.8

result = is_potentially_two_phones_for_one_person(lat1, lon1, radius1_km, lat2, lon2, radius2_km)
print(f"Are these potentially two phones for one person? {result}")
