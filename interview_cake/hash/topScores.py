def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score + 1)

    # populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1
    
    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts)-1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for _ in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)
    
    return sorted_scores

def main():
    print(sort_scores([37, 89, 41, 65, 91, 53], 100))

main()
