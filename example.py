from shapely.geometry import Point, LineString, Polygon


def is_potentially_two_phones_for_one_person(circle_a, circle_b, threshold=0.5):
    intersection_area = circle_a.intersection(circle_b).area
    first_area_share = intersection_area / circle_a.area
    second_area_share = intersection_area / circle_b.area
    return min(first_area_share, second_area_share) > threshold


circle_polygon_a = Point(0, 0).buffer(1)
circle_polygon_b = Point(0, 1).buffer(1)
is_potentially_two_phones_for_one_person(circle_polygon_a, circle_polygon_b)
