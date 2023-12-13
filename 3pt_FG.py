import matplotlib.pyplot as plt
# Initialize figure and axis
fig, ax = plt.subplots()

# Data for Eastern Kentucky
eastern_kentucky_fg = 50
eastern_kentucky_fga = 86
eastern_kentucky_3pt = 10
eastern_kentucky_3pta = 29

# Data for Bethany
Bethany_fg = 21
Bethany_fga = 64
Bethany_3pt = 9
Bethany_3pta = 32

# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
Bethany_fg_percentage = Bethany_fg / Bethany_fga * 100
Bethany_3pt_percentage = Bethany_3pt / Bethany_3pta * 100

# Set bar width and positions
bar_width = 0.35  # Width of each bar
index = [1, 2, 4, 5]  # X-axis positions for the bars

# Set bar colors
colors = ["#800000", "#000000", "#F1D302", "#00FF00"]  # Maroon, Black, Yellow, Green

# Create the bars
ax.bar(index[0], eastern_kentucky_fg_percentage, bar_width, label="EKU FG%", color=colors[0])
ax.bar(index[1], eastern_kentucky_3pt_percentage, bar_width, label="EKU 3PT%", color=colors[1])
ax.bar(index[2], Bethany_fg_percentage, bar_width, label="Bethany FG%", color=colors[2])
ax.bar(index[3], Bethany_3pt_percentage, bar_width, label="Bethany 3PT%", color=colors[3])

# Set x-axis ticks and labels
ax.set_xticks([index[0] + bar_width / 2, index[1] + bar_width / 2, index[2] + bar_width / 2, index[3] + bar_width / 2])
ax.set_xticklabels(["EKU FG%", "EKU 3PT%", "Bethany FG%", "Bethany 3PT%"])

# Show the graph
plt.show()
