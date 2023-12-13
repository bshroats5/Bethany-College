import matplotlib.pyplot as plt

# Example data for teams
teams = ['Bethany Bisons', 'Eastern Kentucky Colonels']
fouls = [13, 14]

# Create a bar graph
plt.bar(teams, fouls)

# Define colors for each team
Bethany_color = 'Green'
eastern_kentucky_color = 'Maroon'

# Create a bar graph with custom colors
plt.bar(teams, fouls, color=[Bethany_color, eastern_kentucky_color])


# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
