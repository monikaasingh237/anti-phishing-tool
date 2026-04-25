def extract_features(url):
    features = []

    # Feature 1: URL length
    features.append(len(url))

    # Feature 2: Check for HTTPS
    features.append(1 if "https" in url else 0)

    # Feature 3: Check for '@'
    features.append(1 if "@" in url else 0)

    # Feature 4: Count dots
    features.append(url.count('.'))

    return features