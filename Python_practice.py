counties_dict={"Arapahoe":422829, "Denver":463356, "Jefferson":432438}
for county, voters, in counties_dict.items():
    print (f"{county} county has {voters:,} registered voters.")

counties = ["Arapahoe" , "Denver", "Jefferson"]

for county in counties:
    print (county)

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print (counties_dict[county])
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county,voters)

voting_data=[{"county":"Arapahoe","registered_voters":422829},
                {"county":"Denver","registered_voters":463356},
                {"county":"Jefferson","registered_voters":432438}]
for counties_dict in voting_data:
    print(counties_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict["county"])

candidate_votes=[3345]
total_votes=[23123]
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("what is the total number of votes in the election?"))
message_to_candidate =(
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes.")
print(message_to_candidate)