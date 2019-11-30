Your submission is scored according to the penalty cost to Santa for suboptimal scheduling. The constraints and penalties are as follows:

    The total number of people attending the workshop each day must be between 125 - 300; if even one day is outside these occupancy constraints, the submission will error and will not be scored.
    Santa provides consolation gifts (of varying value) to families according to their assigned day relative to their preferences. These sum up per family, and the total represents the preferencecost

    .
        choice_0: no consolation gifts
        choice_1: one $50 gift card to Santa's Gift Shop
        choice_2: one $50 gift card, and 25% off Santa's Buffet (value $9) for each family member
        choice_3: one $100 gift card, and 25% off Santa's Buffet (value $9) for each family member
        choice_4: one $200 gift card, and 25% off Santa's Buffet (value $9) for each family member
        choice_5: one $200 gift card, and 50% off Santa's Buffet (value $18) for each family member
        choice_6: one $300 gift card, and 50% off Santa's Buffet (value $18) for each family member
        choice_7: one $300 gift card, and free Santa's Buffet (value $36) for each family member
        choice_8: one $400 gift card, and free Santa's Buffet (value $36) for each family member
        choice_9: one $500 gift card, and free Santa's Buffet (value $36) for each family member, and 50% off North Pole Helicopter Ride tickets (value $199) for each family member
        otherwise: one $500 gift card, and free Santa's Buffet (value $36) for each family member, and free North Pole Helicopter Ride tickets (value $398) for each family member
    Santa's accountants have also developed an empirical equation for cost to Santa that arise from many different effects such as reduced shopping in the Gift Shop when it gets too crowded, extra cleaning costs, a very complicated North Pole tax code, etc. This cost in in addition to the consolation gifts Santa provides above, and is defined as:

accountingpenalty=∑d=1001(Nd−125)400Nd(12+|Nd−Nd+1|50)

where Nd
is the occupancy of the current day, and Nd+1 is the occupancy of the previous day (since we're counting backwards from Christmas!). For the initial condition of d=100, N101=N100

.

To be clear on the above summation, it starts on the date 100 days before Christmas and ends on Christmas Eve.

And finally:

score=preferencecost+accountingpenalty

This may seem complicated, but this nifty-difty starter notebook should get you started fast!
Submission File

For each family_id in the family_data.csv file, list their assigned_day to attend the workshop. Each family should have one and only one assigned_day, which is one of the available days between 1 and 100 days before Christmas. The file should contain a header and have the following format:

family_id,assigned_day
0,100
1,99
2,98
etc.
