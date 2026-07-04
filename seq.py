def read_fasta(filename):
    """
    Reads a FASTA file and returns a dictionary where:
        key   = sequence ID
        value = sequence
    """
    sequences = {}
    seq_id = None
    seq_lines = []

    with open(filename, "r") as fasta_file:
        for line in fasta_file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Header line
            if line.startswith(">"):
                # Save the previous sequence
                if seq_id is not None:
                    sequences[seq_id] = "".join(seq_lines)

                # Extract sequence ID (first word after '>')
                seq_id = line[1:].split()[0]
                seq_lines = []
            else:
                # Add sequence line
                seq_lines.append(line)

        # Save the last sequence
        if seq_id is not None:
            sequences[seq_id] = "".join(seq_lines)

    return sequences


# Example usage
fasta_file = "sequence.fasta"
fasta_dict = read_fasta(fasta_file)

# Print the dictionary
for seq_id, sequence in fasta_dict.items():
    print(f"ID: {seq_id}")
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)}")
    print("-" * 40)