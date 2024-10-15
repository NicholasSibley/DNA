import csv
import sys

# Program to identify to whom a sequence of DNA belongs

def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    rows = []
    with open(sys.argv[1], 'r') as database:
        database_reader = csv.DictReader(database)
        for row in database_reader:
            rows.append(row)

    with open(sys.argv[2], 'r') as sequence:
        sequence_string = sequence.read()

    STR_dict = {}
    for fieldname in database_reader.fieldnames:
        if fieldname != 'name':
            STR_dict [fieldname] = longest_match(sequence_string, fieldname)

    for row in rows:
        match = True
        for fieldname in database_reader.fieldnames:
            if fieldname != "name" and int(row[fieldname]) != int(STR_dict[fieldname]):
                match = False
                break
        if match:
            print(row["name"])
            return
    print("no match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
