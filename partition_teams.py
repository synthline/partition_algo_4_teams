import csv
import itertools
import math

class partition_teams():
    def __init__(self):
        pass

    def partition_the_teams(self, csv_file_path, no_desired_teams, output_file_path):
        
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            name_scores = [(row[0], int(row[1])) for row in reader]
    
        # Sort name-scores by scores
        name_scores.sort(key=lambda x: x[1])
        
        # Initialize the groups
        num_groups = math.ceil(len(name_scores) / no_desired_teams)
        groups = [[] for _ in range(num_groups)]
        
        # Divide the name-scores into groups
        for i, name_score in enumerate(name_scores):
            group_idx = i % num_groups
            groups[group_idx].append(name_score)
        
        # Calculate the average score for each group
        group_avgs = []
        for i, group in enumerate(groups):
            group_avg = sum(s for _, s in group) / len(group)
            group_avgs.append(group_avg)
    
        # Find the combinations of groups that have similar average scores
        best_team_assignments = None
        best_score_diff = float('inf')
        for team_idxs in itertools.combinations(range(num_groups), no_desired_teams):
            team = [groups[i] for i in team_idxs]
            group_avgs_subset = [group_avgs[i] for i in team_idxs]
            score_diff = max(group_avgs_subset) - min(group_avgs_subset)
            if score_diff < best_score_diff:
                best_team_assignments = team
                best_score_diff = score_diff
    
        # Write the team assignments to a text file and print them
        with open(output_file_path, 'w') as output_file:
            for i, team in enumerate(best_team_assignments):
                output_file.write(f'Team {i+1}:\n')
                print(f'Team {i+1}:')
                for name, score in team:
                    output_file.write(f'{name}, {score}\n')
                    print(f'{name}, {score}')
                output_file.write('\n')
                print()
        
        """  
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            name_scores = [(row[0], int(row[1])) for row in reader]
    
        # Sort name-scores by scores
        name_scores.sort(key=lambda x: x[1])
    
        # Initialize the groups
        total_size = sum(team_sizes)
        num_groups = math.ceil(len(name_scores) / total_size)
        groups = [[] for _ in range(num_groups)]
        
        # Divide the name-scores into groups
        for i, name_score in enumerate(name_scores):
            group_idx = i % num_groups
            groups[group_idx].append(name_score)
    
        # Calculate the average score for each group
        group_avgs = []
        for i, group in enumerate(groups):
            group_size = min(len(group), team_sizes[i % len(team_sizes)])
            group_avg = sum(s for _, s in group) / group_size
            group_avgs.append(group_avg)
    
        # Find the combinations of groups that have similar average scores
        team_assignments = []
        for i, j in itertools.combinations(range(num_groups), 2):
            avg_diff = abs(group_avgs[i] - group_avgs[j])
            if avg_diff <= 0.5:
                team_assignments.append((groups[i], groups[j]))
    
        # Check if there are any groups left over that can't form a team
        unassigned_groups = set(range(num_groups))
        for group_idxs in itertools.combinations(range(num_groups), len(team_sizes)):
            if set(group_idxs) not in itertools.combinations(unassigned_groups, len(team_sizes)):
                continue
            assigned = False
            for perm in itertools.permutations(group_idxs):
                group_avgs_subset = [group_avgs[i] for i in perm]
                avg_diff = max(group_avgs_subset) - min(group_avgs_subset)
                if avg_diff <= 0.5:
                    team_assignments.append([groups[i] for i in perm])
                    assigned = True
                    break
            if assigned:
                unassigned_groups.difference_update(group_idxs)
    
        # Write the team assignments to a text file and print them
        with open(output_file_path, 'w') as output_file:
            for i, team in enumerate(team_assignments):
                output_file.write(f'Team {i+1}:\n')
                print(f'Team {i+1}:')
                for member in team:
                    for name, score in member:
                        output_file.write(f'{name}, {score}\n')
                        print(f'{name}, {score}')
                    output_file.write('\n')
                    print()
        
        
        
        
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            name_scores = [(row[0], int(row[1])) for row in reader]
        
        # Sort name-scores by scores
        name_scores.sort(key=lambda x: x[1])
        
        # Initialize the groups
        total_size = sum(team_sizes)
        num_groups = math.ceil(len(name_scores) / total_size)
        groups = [[] for _ in range(num_groups)]
        
        # Divide the name-scores into groups
        for i, name_score in enumerate(name_scores):
            group_idx = i % num_groups
            groups[group_idx].append(name_score)
        
        # Calculate the average score for each group
        group_avgs = []
        for i, group in enumerate(groups):
            group_size = min(len(group), team_sizes[i])
            group_avg = sum(s for _, s in group) / group_size
            group_avgs.append(group_avg)
        
        # Find the best partition by brute force
        min_diff = float('inf')
        best_partition = None
        for partition in itertools.combinations(groups, 2):
            diff = 0
            for i in range(num_groups):
                group_size = min(len(groups[i]), team_sizes[i])
                group_avg = sum(s for _, s in groups[i]) / group_size
                if groups[i] in partition[0]:
                    diff += abs(group_avgs[0] - group_avg)
                else:
                    diff += abs(group_avgs[1] - group_avg)
            if diff < min_diff:
                min_diff = diff
                best_partition = partition
        
        # Write the result to a text file and print it to the console
        with open(output_file_path, 'w') as output_file:
            for i, group in enumerate(best_partition):
                group_size = min(len(group), team_sizes[i])
                output_file.write(f'Team {i + 1}:\n')
                print(f'Team {i + 1}:')
                for name, score in group[:group_size]:
                    output_file.write(f'- {name}: {score}\n')
                    print(f'- {name}: {score}')
        
        return best_partition

    
    
    
    
    
    
    def partition_the_teams(self, csv_file_path, team_size, output_file_path):
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
        
        # Write the result to a text file and print it to the console
        with open(output_file_path, 'w') as output_file:
            for i, group in enumerate(best_partition):
                output_file.write(f'Team {i + 1}:\n')
                print(f'Team {i + 1}:')
                for name, score in group:
                    output_file.write(f'- {name}: {score}\n')
                    print(f'- {name}: {score}')
        
        return best_partition

--------------------------------------------------------------------

def partition_teams(csv_file_path, team_size, output_file_path):
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
    
    # Write the result to a text file
    with open(output_file_path, 'w') as output_file:
        for i, group in enumerate(best_partition):
            output_file.write(f'Team {i + 1}:\n')
            for name, score in group:
                output_file.write(f'- {name}: {score}\n')
    
    return best_partition
"""