def main():
    src = "junk.txt"

    # Read file and count lines
    with open(src, "r") as f:
        lines = f.read().splitlines()
    total_lines = len(lines)
    print(f"Total lines: {total_lines}")

    # Convert to lowercase and append required line
    processed = [line.lower() for line in lines]
    processed.append("text file nanalyssis")

    # Save processed content (each line on its own line)
    with open(src, "w") as f:
        f.write("\n".join(processed) + "\n")

if __name__ == "__main__":
    main()