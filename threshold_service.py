def adaptive_threshold(quality, confidence):

    threshold = (
        0.55
        + (1-quality)*0.2
        - (1-confidence)*0.1
    )

    return threshold