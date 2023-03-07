import csv
import itertools

def partition_teams(csv_file_path, team_size):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        name_scores = [(row[0], int(row[1])) for row in reader]
    
    # Sort name-scores by scores
    name_scores.sort(key=lambda x: x[1])
    
    # Initialize the groups
    num_groups = (len(name_scores) + team_size - 1) // team_size  # Round up to the nearest integer
    groups = [[] for _ in range(num_groups)]
    
    # Divide the name-scores into groups
    for i, name_score in enumerate(name_scores):
        group_idx = i % num_groups
        groups[group_idx].append(name_score)
    
    # Calculate the average score for each group
    group_avgs = [sum(s for _, s in group) / len(group) for group in groups]
    
    # Find the best partition by brute force
    min_diff = float('inf')
    best_partition = None
    for partition in itertools.combinations(groups, 2):
        diff = 0
        for i in range(num_groups):
            group_avg = sum(s for _, s in groups[i]) / len(groups[i])
            if groups[i] in partition[0]:
                diff += abs(group_avgs[0] - group_avg)
            else:
                diff += abs(group_avgs[1] - group_avg)
        if diff < min_diff:
            min_diff = diff
            best_partition = partition
    
    return best_partition
