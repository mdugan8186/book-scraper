# ==== utils.py ====

import csv
from datetime import datetime
from pathlib import Path
from config import OUTPUT_DIR, CSV_FILENAME_TEMPLATE


def ensure_output_dir_exists():
    """Create the output directory if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_timestamped_filename(template: str) -> Path:
    """Generate a filename with current timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = template.format(timestamp=timestamp)
    return OUTPUT_DIR / filename


def save_to_csv(data: list[dict], template: str = CSV_FILENAME_TEMPLATE) -> Path:
    """
    Save a list of dictionaries to a timestamped CSV file in the output directory.

    Returns the Path to the saved file.
    """
    ensure_output_dir_exists()
    filepath = generate_timestamped_filename(template)

    if not data:
        raise ValueError("No data provided to save.")

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Data saved to {filepath}")
    return filepath
