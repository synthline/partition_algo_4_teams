from partition_teams import partition_teams


csv_file_path = 'test1.csv'
no_desired_teams = 2
output_file_path = 'teams.txt'


mini_hackathon = partition_teams()

mini_hackathon.partition_the_teams(csv_file_path, no_desired_teams, output_file_path)