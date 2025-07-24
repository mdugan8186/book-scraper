# ==== postprocess.py ====

"""
Analyze and summarize the latest CSV file in output/
Save summary as plain text and markdown in samples/
"""

import pandas as pd
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path("output")
SAMPLES_DIR = Path("samples")
SAMPLES_DIR.mkdir(exist_ok=True)


def get_latest_csv(directory: Path) -> Path | None:
    csv_files = sorted(directory.glob("books_*.csv"), reverse=True)
    return csv_files[0] if csv_files else None


def load_data(filepath: Path) -> pd.DataFrame:
    return pd.read_csv(filepath)


def validate_data(df: pd.DataFrame) -> str:
    messages = []
    if df.duplicated().any():
        messages.append(f"⚠️ {df.duplicated().sum()} duplicate rows found.")
    else:
        messages.append("✅ No duplicate rows found.")

    if df.isnull().any().any():
        null_counts = df.isnull().sum()
        messages.append("⚠️ Missing values detected:\n" + str(null_counts))
    else:
        messages.append("✅ No missing values detected.")
    return "\n".join(messages)


def summarize_data(df: pd.DataFrame) -> str:
    total = len(df)
    price_stats = df["price"].agg(["min", "max", "mean"])
    avail_counts = df["availability"].value_counts()
    rating_counts = df["rating"].value_counts().sort_index()

    lines = [
        f"📚 Total books: {total}",
        f"💷 Price range: £{price_stats['min']:.2f} - £{price_stats['max']:.2f}",
        f"💰 Average price: £{price_stats['mean']:.2f}",
        "\n📦 Availability breakdown:",
        avail_counts.to_string(),
        "\n⭐ Star rating distribution:",
        rating_counts.to_string()
    ]
    return "\n".join(lines)


def save_summary(text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    txt_file = SAMPLES_DIR / "summary.txt"
    md_file = SAMPLES_DIR / "summary.md"

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(f"Summary generated on {timestamp}\n\n")
        f.write(text)

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(f"# Summary (Generated {timestamp})\n\n")
        for line in text.splitlines():
            if line.startswith("📚") or line.startswith("💷") or line.startswith("💰"):
                f.write(f"**{line}**\n\n")
            elif line.startswith("📦") or line.startswith("⭐"):
                f.write(f"### {line}\n\n")
            else:
                f.write(f"{line}\n")

    print(f"✅ Summary saved to:\n- {txt_file}\n- {md_file}")


def main():
    latest_csv = get_latest_csv(OUTPUT_DIR)
    if not latest_csv:
        print("❌ No CSV files found in output/")
        return

    print(f"📄 Processing: {latest_csv.name}")
    df = load_data(latest_csv)
    validation = validate_data(df)
    summary = summarize_data(df)
    report = validation + "\n\n" + summary

    save_summary(report)


if __name__ == "__main__":
    main()
