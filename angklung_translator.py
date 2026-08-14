import argparse
import re

KEYS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_TO_SHARP = {
    "DB": "C#",
    "EB": "D#",
    "GB": "F#",
    "AB": "G#",
    "BB": "A#",
}
SEMITONE_TO_NUMBER = {
    0: "1",
    1: "b2",
    2: "2",
    3: "b3",
    4: "3",
    5: "4",
    6: "#4",
    7: "5",
    8: "b6",
    9: "6",
    10: "b7",
    11: "7",
}
NUMBER_TO_SEMITONE = {
    "1": 0,
    "b2": 1,
    "2": 2,
    "b3": 3,
    "3": 4,
    "4": 5,
    "#4": 6,
    "5": 7,
    "b6": 8,
    "6": 9,
    "b7": 10,
    "7": 11,
}
TOKEN_PATTERN = re.compile(r"^(#|b)?([1-7])([+-]\d+)?$")


def normalize_key(key: str) -> str:
    upper = key.strip().upper()
    if upper in KEYS:
        return upper
    if upper in FLAT_TO_SHARP:
        return FLAT_TO_SHARP[upper]
    raise ValueError(f"Nada dasar tidak valid: {key}")


def token_to_absolute_semitone(token: str, source_key: str):
    if token == "0":
        return None, False
    match = TOKEN_PATTERN.match(token)
    if not match:
        raise ValueError(f"Format nomor tidak valid: {token}")

    accidental, degree, octave_part = match.groups()
    key = f"{accidental or ''}{degree}"
    if key not in NUMBER_TO_SEMITONE:
        raise ValueError(f"Nomor tidak didukung: {token}")

    octave = int(octave_part or 0)
    source_index = KEYS.index(source_key)
    return source_index + NUMBER_TO_SEMITONE[key] + octave * 12, bool(octave_part)


def absolute_semitone_to_token(
    abs_semitone: int, target_key: str, keep_octave: bool = False
) -> str:
    if abs_semitone is None:
        return "0"
    target_index = KEYS.index(target_key)
    relative = abs_semitone - target_index
    octave = relative // 12
    semitone_in_octave = relative % 12
    base = SEMITONE_TO_NUMBER[semitone_in_octave]
    if not keep_octave or octave == 0:
        return base
    return f"{base}{octave:+d}"


def translate_numbers(numbers: str, source_key: str, target_key: str) -> str:
    src = normalize_key(source_key)
    dst = normalize_key(target_key)
    tokens = numbers.split()
    translated = []
    for token in tokens:
        absolute, had_octave = token_to_absolute_semitone(token, src)
        translated.append(
            absolute_semitone_to_token(absolute, dst, keep_octave=had_octave)
        )
    return " ".join(translated)


def translate_to_all_keys(numbers: str, source_key: str):
    src = normalize_key(source_key)
    return {key: translate_numbers(numbers, src, key) for key in KEYS}


def main():
    parser = argparse.ArgumentParser(
        description="Penerjemah nomor Angklung untuk semua nada dasar"
    )
    parser.add_argument("numbers", help='Urutan nomor, contoh: "1 2 3 4 5 6 7"')
    parser.add_argument("--source", default="C", help="Nada dasar sumber (default: C)")
    parser.add_argument(
        "--target",
        default=None,
        help="Nada dasar tujuan (opsional). Jika kosong, terjemahkan ke semua nada dasar.",
    )
    args = parser.parse_args()

    if args.target:
        print(translate_numbers(args.numbers, args.source, args.target))
        return

    results = translate_to_all_keys(args.numbers, args.source)
    for key in KEYS:
        print(f"{key}: {results[key]}")


if __name__ == "__main__":
    main()
