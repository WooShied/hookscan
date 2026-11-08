import sys
from pathlib import Path
from hookscan.parse import load_email, received_hops


def main():
    if len(sys.argv) < 2:
        print("error: missing path to email file")
        sys.exit(1)

    raw_path = sys.argv[1]
    file_path = Path(raw_path).resolve()

    if not file_path.is_file():
        print(f"error: {file_path} is not a file")
        sys.exit(1)

    msg = load_email(file_path)

    target_headers = ["From", "Reply-To", "Return-Path", "To", "Subject", "Date"]

    print(f"--- Email Metadata [{file_path.name}] ---\n")
    for header in target_headers:
        # msg.get() handles missing headers gracefully by returning None
        value = msg.get(header, "Not Found")
        print(f"{header}: {value}")

    hops = received_hops(msg)

    hops = received_hops(msg)
    print("\n--- Received hops (oldest first) ---")
    for number, hop in enumerate(hops, start=1):
        print(f"Hop {number}: {hop}")


main()