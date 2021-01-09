def normalize_range_limits(value, limits):
    value = max(value, limits[0])
    value = min(value, limits[1])
    return value

def normalize_glide_limits(value, limits):
    sign = bool(value > 0) - bool(value < 0)
    return normalize_range_limits(value * sign, limits) * sign
