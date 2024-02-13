def detect_chosen_option_from_transcript(
        transcript: str, options: List[str]) -> str:
    best_match_score = 0
    best_match = ""

    for option in options:
        score = fuzz.token_set_ratio(transcript.lower(), option.lower())
        if score > best_match_score:
            best_match_score = score
            best_match = option

    if best_match_score >= 70:
        return best_match
    else:
        return ""
