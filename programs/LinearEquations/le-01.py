# 36 workers can build a wall in 12 days
# how many days will it take 16 workers to build the same wall

# Total work required to complete wall is constant
total_work = 36 * 12

# Work done by 36 workers in a day
work_36w_day = total_work / 12

# Work done by a single worker in a day
work_1w_day = work_36w_day / 36

# Work done by 16 workers in a day
work_16w_day = work_1w_day * 16

num_days_worked = 0
remaining_work = total_work

while remaining_work > 0:
    num_days_worked = num_days_worked + 1
    remaining_work = remaining_work - work_16w_day
    print( "16 workers worked for", num_days_worked, "days." )

print( "Total num of days required =", num_days_worked )
    

