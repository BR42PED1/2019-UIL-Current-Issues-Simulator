#import simulation
import csv
import random

#sim("3", "results3A.txt")
#sim("1", "results1A.txt")


# Simulation.py
#import csv
#import random

lastname = []
firstname = []
school = []
city = []
district = []
region = []
eliminated = []
teams = []
conference = []
high = []
low = []

inter_lastname = []
inter_firstname = []
inter_school = []
inter_city = []
inter_high = []
inter_low = []

def sim(con, textfile, reg1, reg2, reg3, reg4):
    # Append individuals
    Contestant = open('names.csv')

    with open('names.csv','r') as f:
        contents = f.read()

    contents = contents.replace('\t','')

    with open('names.csv','w') as f:
        f.write(contents)

    file = csv.DictReader(Contestant)

    printer = open(textfile, "a")

    with open(textfile,"w"):
        printer.write('')


    #Start C+P Here

    # int(col['Conference'])
    for col in file:
        #print(col['Conference'])
        # convalue = int(col['Conference'])
        if col['Conference'] == con:
            lastname.append(col['LastName'])
            firstname.append(col['FirstName'])
            school.append(col['School'])
            if (school.count(col['School'])) == 3:
                teams.append(col['School'])
            city.append(col['City'])
            print(int(col['District']))
            district.append(int(col['District']))
            region.append(int(col['Region']))
            eliminated.append(col['Eliminated'])
            high.append((int(col['High']) + int(col['Low']))/2)
            low.append((int(col['High']) + int(col['Low']))/2)

    # Append scores
    scores = []
    essay = []

    with open('scoresD1.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()

    with open('essays.txt','r') as w:
        for line in w:
            essay.append(float(line.strip()))
    essay.sort()

    competition_poolFN = []
    competition_poolLN = []
    competition_scores = []
    competition_city = []
    competition_school = []
    competition_high = []
    competition_low = []
    score_r = 0
    team_score = []
    team_competition = []
    objective = []

    region1_wildcard_team =[]
    region1_wildcard_score =[]
    region1_teams = []

    # District 1
    competition_scores.clear()
    print(" -- District 1 --")
    with open(textfile, "a") as printer:
        printer.write(" -- District 1 --\n")
    for j in range(len(lastname)):
        if district[j] == 1:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)


            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")



        '''
        while ( flagger == True):
            score_r = random.choice(scores)
            if ( score_r >= int(low[t]) ) and ( score_r <= int(high[t])):
                competition_scores.append(score_r)
                flagger = False
            
            if ( counter > 10 ):
                if ( flagger == True ):
                    competition_scores.append(int(low[t]))
                flagger = False
            counter = counter + 1
        '''

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()



    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break
    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]

    first_tie = 0
    second_tie = 0

    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = 0;
    
    # Begin Here

    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    
    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)
    
            
    

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))


    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()

    # For District 2
    with open('scoresD1.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 2")
    with open(textfile, "a") as printer:
        printer.write(" -- District 2 --\n")
    for j in range(len(lastname)):
        if district[j] == 2:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])
    
    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar


    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    '''

    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        
    '''

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]

    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 3
    with open('scoresD3.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 3")
    with open(textfile, "a") as printer:
        printer.write(" -- District 3 --\n")
    for j in range(len(lastname)):
        if district[j] == 3:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])
    
    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar


    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}   X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}   X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()

    # District 4
    with open('scoresD4.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 4")
    with open(textfile, "a") as printer:
        printer.write(" -- District 4 --\n")
    for j in range(len(lastname)):
        if district[j] == 4:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]

    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 5
    with open('scoresD5.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 5")
    with open(textfile, "a") as printer:
        printer.write(" -- District 5 --\n")
    for j in range(len(lastname)):
        if district[j] == 5:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 6
    with open('scoresD6.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 6")
    with open(textfile, "a") as printer:
        printer.write(" -- District 6 --\n")
    for j in range(len(lastname)):
        if district[j] == 6:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 7
    with open('scoresD7.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 7")
    with open(textfile, "a") as printer:
        printer.write(" -- District 7 --\n")
    for j in range(len(lastname)):
        if district[j] == 7:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 8
    with open('scoresD8.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 8")
    with open(textfile, "a") as printer:
        printer.write(" -- District 8 --\n")
    for j in range(len(lastname)):
        if district[j] == 8:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region1_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region1_wildcard_team.append(sorted_final_team[1])
        region1_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()

    # Retrieving Region 1 Wildcard Team

    region1_wildcard = list(zip(region1_wildcard_score, region1_wildcard_team))
    region1_wirdcard_sorter = sorted(region1_wildcard, key=lambda s: s[0], reverse=True)
    region1_wildcard_final = [tup[0] for tup in region1_wirdcard_sorter]
    region1_wildcard_winner = [tup[1] for tup in region1_wirdcard_sorter]
    print(region1_wildcard_winner[0])

    for a in range(len(lastname)):
        if  (school[a] == region1_wildcard_winner[0]):
            eliminated[a] = "Y"

    region1_teams.append(region1_wildcard_winner[0])
    region1_wildcard_final.clear()
    region1_wildcard_score.clear()

    region2_wildcard_team =[]
    region2_wildcard_score =[]

    region2_teams = []



    # District 9
    with open('scoresD9.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 9")
    with open(textfile, "a") as printer:
        printer.write(" -- District 9 --\n")
    for j in range(len(lastname)):
        if district[j] == 9:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])
            
    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 10
    with open('scoresD10.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 10")
    with open(textfile, "a") as printer:
        printer.write(" -- District 10 --\n")
    for j in range(len(lastname)):
        if district[j] == 10:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0
        
    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 11
    with open('scoresD11.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 11")
    with open(textfile, "a") as printer:
        printer.write(" -- District 11 --\n")
    for j in range(len(lastname)):
        if district[j] == 11:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])
            
    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 12
    with open('scoresD12.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 12")
    with open(textfile, "a") as printer:
        printer.write(" -- District 12 --\n")
    for j in range(len(lastname)):
        if district[j] == 12:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 13
    with open('scoresD13.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 13")
    with open(textfile, "a") as printer:
        printer.write(" -- District 13 --\n")
    for j in range(len(lastname)):
        if district[j] == 13:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()



    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 14
    with open('scoresD14.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 14")
    with open(textfile, "a") as printer:
        printer.write(" -- District 14 --\n")
    for j in range(len(lastname)):
        if district[j] == 14:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 37 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()



    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 15
    with open('scoresD15.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 15")
    with open(textfile, "a") as printer:
        printer.write(" -- District 15 --\n")
    for j in range(len(lastname)):
        if district[j] == 15:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()



    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 16
    with open('scoresD16.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 16")
    with open(textfile, "a") as printer:
        printer.write(" -- District 16 --\n")
    for j in range(len(lastname)):
        if district[j] == 16:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region2_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region2_wildcard_team.append(sorted_final_team[1])
        region2_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Retrieving Region 2 Wildcard Team

    region2_wildcard = list(zip(region2_wildcard_score, region2_wildcard_team))
    region2_wirdcard_sorter = sorted(region2_wildcard, key=lambda s: s[0], reverse=True)
    region2_wildcard_final = [tup[0] for tup in region2_wirdcard_sorter]
    region2_wildcard_winner = [tup[1] for tup in region2_wirdcard_sorter]
    print(region2_wildcard_winner[0])

    for a in range(len(lastname)):
        if  (school[a] == region2_wildcard_winner[0]):
            eliminated[a] = "Y"

    region2_teams.append(region2_wildcard_winner[0])
    region2_wildcard_final.clear()
    region2_wildcard_score.clear()

    region3_wildcard_team =[]
    region3_wildcard_score =[]
    region3_teams = []



    # District 17
    with open('scoresD17.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 17")
    with open(textfile, "a") as printer:
        printer.write(" -- District 17 --\n")
    for j in range(len(lastname)):
        if district[j] == 17:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 18
    with open('scoresD18.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 18")
    with open(textfile, "a") as printer:
        printer.write(" -- District 18 --\n")
    for j in range(len(lastname)):
        if district[j] == 18:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 19
    with open('scoresD19.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 19")
    with open(textfile, "a") as printer:
        printer.write(" -- District 19 --\n")
    for j in range(len(lastname)):
        if district[j] == 19:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 20
    with open('scoresD20.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 20")
    with open(textfile, "a") as printer:
        printer.write(" -- District 20 --\n")
    for j in range(len(lastname)):
        if district[j] == 20:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 21
    with open('scoresD21.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 21")
    with open(textfile, "a") as printer:
        printer.write(" -- District 21 --\n")
    for j in range(len(lastname)):
        if district[j] == 21:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 22
    with open('scoresD22.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 22")
    with open(textfile, "a") as printer:
        printer.write(" -- District 22 --\n")
    for j in range(len(lastname)):
        if district[j] == 22:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 32 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()


    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 23
    with open('scoresD23.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 23")
    with open(textfile, "a") as printer:
        printer.write(" -- District 23 --\n")
    for j in range(len(lastname)):
        if district[j] == 23:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 24
    with open('scoresD24.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 24")
    with open(textfile, "a") as printer:
        printer.write(" -- District 24 --\n")
    for j in range(len(lastname)):
        if district[j] == 24:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region3_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region3_wildcard_team.append(sorted_final_team[1])
        region3_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Retrieving Region 3 Wildcard Team

    region3_wildcard = list(zip(region3_wildcard_score, region3_wildcard_team))
    region3_wirdcard_sorter = sorted(region3_wildcard, key=lambda s: s[0], reverse=True)
    region3_wildcard_final = [tup[0] for tup in region3_wirdcard_sorter]
    region3_wildcard_winner = [tup[1] for tup in region3_wirdcard_sorter]
    print(region3_wildcard_winner[0])

    for a in range(len(lastname)):
        if  (school[a] == region3_wildcard_winner[0]):
            eliminated[a] = "Y"

    region3_teams.append(region3_wildcard_winner[0])
    region3_wildcard_final.clear()
    region3_wildcard_score.clear()

    region4_wildcard_team =[]
    region4_wildcard_score =[]
    region4_teams = []



    # District 25
    with open('scoresD25.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 25")
    with open(textfile, "a") as printer:
        printer.write(" -- District 25 --\n")
    for j in range(len(lastname)):
        if district[j] == 25:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 26
    with open('scoresD26.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 26")
    with open(textfile, "a") as printer:
        printer.write(" -- District 26 --\n")
    for j in range(len(lastname)):
        if district[j] == 26:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 27
    with open('scoresD27.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 27")
    with open(textfile, "a") as printer:
        printer.write(" -- District 27 --\n")
    for j in range(len(lastname)):
        if district[j] == 27:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 28
    with open('scoresD28.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 28")
    with open(textfile, "a") as printer:
        printer.write(" -- District 28 --\n")
    for j in range(len(lastname)):
        if district[j] == 28:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 29
    with open('scoresD29.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 29")
    with open(textfile, "a") as printer:
        printer.write(" -- District 29 --\n")
    for j in range(len(lastname)):
        if district[j] == 29:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 30
    with open('scoresD30.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 30")
    with open(textfile, "a") as printer:
        printer.write(" -- District 30 --\n")
    for j in range(len(lastname)):
        if district[j] == 30:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 31
    with open('scoresD31.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 31")
    with open(textfile, "a") as printer:
        printer.write(" -- District 31 --\n")
    for j in range(len(lastname)):
        if district[j] == 31:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # District 32
    with open('scoresD32.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- District -- 32")
    with open(textfile, "a") as printer:
        printer.write(" -- District 32 --\n")
    for j in range(len(lastname)):
        if district[j] == 32:
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

            if school[j] not in team_competition and school.count(school[j]) >= 3:
                team_competition.append(school[j])

    sully = random.randint(0, len(competition_school)-1)
    host_school = competition_school[sully]
    host_city = competition_city[sully]
    with open(textfile, "a") as printer:
        printer.write(f" March 30, 2019, {host_school}, {host_city} \n")

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 40 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)

            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]
    '''
    for m in range(len(sorted_competition_poolFN)):
        print("{} {}, {}, {}, {} ".format(sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))
    '''
    score_keeper = []
    for e in range(len(team_competition)):
        word_to_find = team_competition[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,team_competition))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]

    '''
    for s in range(len(sorted_competition_poolFN)):
        if sorted_competition_scores[s] >= cutoff:
            sorted_competition_scores[s] = sorted_competition_scores[s] + random.choice(essay)
    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]

    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)): 
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write(str("{}.   {}   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z])))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {}     X   \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write(("{}.   {}   {},   {},   {},   {}   \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z])))
    '''
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_district(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   Region".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Region\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here

    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}   X   Region".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   X   Region\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}   X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "Y"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "Y"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "Y"

    region4_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        region4_wildcard_team.append(sorted_final_team[1])
        region4_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()

    '''
    for y in range( len(firstname)):
        print("{}   {}   {}   {}   {}   {}   {}".format(firstname[y],lastname[y],school[y], city[y], district[y],region[y],eliminated[y]))
    '''


    # Retrieving Region 4 Wildcard Team

    region4_wildcard = list(zip(region4_wildcard_score, region4_wildcard_team))
    region4_wirdcard_sorter = sorted(region4_wildcard, key=lambda s: s[0], reverse=True)
    region4_wildcard_final = [tup[0] for tup in region4_wirdcard_sorter]
    region4_wildcard_winner = [tup[1] for tup in region4_wirdcard_sorter]
    print(region4_wildcard_winner[0])

    for a in range(len(lastname)):
        if  (school[a] == region4_wildcard_winner[0]):
            eliminated[a] = "Y"

    region4_teams.append(region4_wildcard_winner[0])
    region4_wildcard_final.clear()
    region4_wildcard_score.clear()

    state_wildcard_team =[]
    state_wildcard_score =[]
    state_teams = []

    # Append  Regional scores
    scores.clear()
    region_scores = []
    '''
    with open('region_scores.txt','r') as x:
        for line in x:
            region_scores.append(int(line.strip()))

    region_scores.sort()
    '''
    score_r = 0


    # Append Regional Essays
    essay.clear()
    with open('region_essays.txt','r') as w:
        for line in w:
            essay.append(float(line.strip()))
    essay.sort()



    # Region 1
    with open('scoresR1.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- Region -- 1")
    with open(textfile, "a") as printer:
        printer.write(" -- Region 1 --\n")
        printer.write(f" April 14 2019, {reg1}  \n")
    for j in range(len(lastname)):
        if (region[j] == 1) and ( eliminated[j] == "Y"):
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 36 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(region1_teams)):
        word_to_find = region1_teams[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,region1_teams))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 4):
        if (sorted_score[3] == sorted_score[4]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[3]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[4]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 5):
        if (sorted_score[4] == sorted_score[5]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[4]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[5]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[4],sorted_final_team[5] = sorted_final_team[5], sorted_final_team[4]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 6):
        if (sorted_score[5] == sorted_score[6]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[5]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[6]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[5],sorted_final_team[6] = sorted_final_team[6], sorted_final_team[5]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 7):
        if (sorted_score[6] == sorted_score[7]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[6]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[7]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[6],sorted_final_team[7] = sorted_final_team[7], sorted_final_team[6]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 8):
        if (sorted_score[7] == sorted_score[8]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[7]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[8]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[7],sorted_final_team[8] = sorted_final_team[8], sorted_final_team[7]

            first_tie = 0
            second_tie = 0



    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_region(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    '''
    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)
    '''

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]

    '''
        for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
    '''
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   State".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   State\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   State".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   State\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "S"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "S"

    state_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        state_wildcard_team.append(sorted_final_team[1])
        state_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Region 2
    with open('scoresR2.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- Region -- 2")
    with open(textfile, "a") as printer:
        printer.write(" -- Region 2 --\n")
        printer.write(f" April 14 2019, {reg2}  \n")
    for j in range(len(lastname)):
        if (region[j] == 2) and ( eliminated[j] == "Y"):
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 36 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(region2_teams)):
        word_to_find = region2_teams[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,region2_teams))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 4):
        if (sorted_score[3] == sorted_score[4]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[3]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[4]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 5):
        if (sorted_score[4] == sorted_score[5]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[4]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[5]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[4],sorted_final_team[5] = sorted_final_team[5], sorted_final_team[4]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 6):
        if (sorted_score[5] == sorted_score[6]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[5]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[6]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[5],sorted_final_team[6] = sorted_final_team[6], sorted_final_team[5]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 7):
        if (sorted_score[6] == sorted_score[7]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[6]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[7]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[6],sorted_final_team[7] = sorted_final_team[7], sorted_final_team[6]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 8):
        if (sorted_score[7] == sorted_score[8]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[7]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[8]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[7],sorted_final_team[8] = sorted_final_team[8], sorted_final_team[7]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_region(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   State".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   State\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   State".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   State\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "S"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "S"

    state_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        state_wildcard_team.append(sorted_final_team[1])
        state_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Region 3
    with open('scoresR3.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- Region -- 3")
    with open(textfile, "a") as printer:
        printer.write(" -- Region 3 --\n")
        printer.write(f" April 14 2019, {reg3}  \n")
    for j in range(len(lastname)):
        if (region[j] == 3) and ( eliminated[j] == "Y"):
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 36 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(region3_teams)):
        word_to_find = region3_teams[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,region3_teams))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 4):
        if (sorted_score[3] == sorted_score[4]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[3]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[4]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 5):
        if (sorted_score[4] == sorted_score[5]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[4]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[5]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[4],sorted_final_team[5] = sorted_final_team[5], sorted_final_team[4]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 6):
        if (sorted_score[5] == sorted_score[6]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[5]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[6]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[5],sorted_final_team[6] = sorted_final_team[6], sorted_final_team[5]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 7):
        if (sorted_score[6] == sorted_score[7]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[6]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[7]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[6],sorted_final_team[7] = sorted_final_team[7], sorted_final_team[6]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 8):
        if (sorted_score[7] == sorted_score[8]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[7]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[8]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[7],sorted_final_team[8] = sorted_final_team[8], sorted_final_team[7]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_region(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar
        
    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   State".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   State\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   State".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   State\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "S"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "S"

    state_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        state_wildcard_team.append(sorted_final_team[1])
        state_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Region 4
    with open('scoresR4.txt','r') as w:
        for line in w:
            scores.append(int(line.strip()))
    scores.sort()
    competition_scores.clear()
    print(" -- Region -- 4")
    with open(textfile, "a") as printer:
        printer.write(" -- Region 4 --\n")
        printer.write(f" April 14 2019, {reg4}  \n")
    for j in range(len(lastname)):
        if (region[j] == 4) and ( eliminated[j] == "Y"):
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_r = random.choice(scores)
            if ( score_r >= int(competition_low[t]) ) and ( score_r <= int(competition_high[t])) and ( flagger == True) and ( score_r < 36 ):
                competition_scores.append(score_r)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(region4_teams)):
        word_to_find = region4_teams[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,region4_teams))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 4):
        if (sorted_score[3] == sorted_score[4]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[3]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[4]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 5):
        if (sorted_score[4] == sorted_score[5]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[4]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[5]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[4],sorted_final_team[5] = sorted_final_team[5], sorted_final_team[4]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 6):
        if (sorted_score[5] == sorted_score[6]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[5]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[6]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[5],sorted_final_team[6] = sorted_final_team[6], sorted_final_team[5]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 7):
        if (sorted_score[6] == sorted_score[7]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[6]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[7]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[6],sorted_final_team[7] = sorted_final_team[7], sorted_final_team[6]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 8):
        if (sorted_score[7] == sorted_score[8]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[7]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[8]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[7],sorted_final_team[8] = sorted_final_team[8], sorted_final_team[7]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_region(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    '''
    for g in range(len(sorted_final_poolFN) - 1):
        if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
    '''

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   State".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   State\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   Alternate".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   Alternate\n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X   State".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   State\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X   Alternate".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X   Alternate\n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
            eliminated[h] = "S"
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
            eliminated[h] = "S"
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "S"

    state_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        state_wildcard_team.append(sorted_final_team[1])
        state_wildcard_score.append(sorted_score[1])

    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()



    # Retrieving State Wildcard Team

    state_wildcard = list(zip(state_wildcard_score, state_wildcard_team))
    state_wirdcard_sorter = sorted(state_wildcard, key=lambda s: s[0], reverse=True)
    state_wildcard_final = [tup[0] for tup in state_wirdcard_sorter]
    state_wildcard_winner = [tup[1] for tup in state_wirdcard_sorter]

    for a in range(len(lastname)):
        if  (school[a] == state_wildcard_winner[0]):
            eliminated[a] = "S"

    state_teams.append(state_wildcard_winner[0])
    state_wildcard_final.clear()
    state_wildcard_score.clear()


    # Append  State scores
    region_scores.clear()

    state_scores = []

    with open('state_scores.txt','r') as p:
        for line in p:
            scores.append(int(line.strip()))

    scores.sort()

    competition_scores.clear()



    # Append State Essays
    essay.clear()
    with open('state_essays.txt','r') as w:
        for line in w:
            essay.append(float(line.strip()))
    essay.sort()


    # State
    competition_scores.clear()
    print(" -- State -- ")
    with open(textfile, "a") as printer:
        printer.write(" -- State --\n")
        printer.write(" May 3, 2019, University of Texas at Austin \n")
    for j in range(len(lastname)):
        if ( eliminated[j] == "S"):
            competition_poolFN.append(firstname[j])
            competition_poolLN.append(lastname[j])
            competition_city.append(city[j])
            competition_school.append(school[j])
            mediator = sorting()
            competition_high.append(high[j] + mediator)
            competition_low.append(low[j] - mediator)

    for t in range(len(competition_poolFN)):
        flagger = True
        counter = 0
        while( counter <= 201 ):
            score_state = random.choice(scores)
            if ( score_state >= int(competition_low[t]) ) and ( score_state <= int(competition_high[t])) and ( flagger == True) and ( score_state < 38 ):
                competition_scores.append(score_state)
                flagger = False
        
            counter = counter + 1
        
        if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

    competition_high.clear()
    competition_low.clear()

    '''       
    for t in range(len(competition_poolFN)):
        score_state = random.choice(scores)
        competition_scores.append(score_state)
    '''



    combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
    sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
    sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
    sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
    sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
    sorted_competition_city = [tup[3] for tup in sorted_combined_id]
    sorted_school = [tup[4] for tup in sorted_combined_id]

    for m in range(len(sorted_competition_poolFN)):
        print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

    score_keeper = []
    for e in range(len(state_teams)):
        word_to_find = state_teams[e]
        count = 0
        for q in range(len(sorted_school)):
            if sorted_school[q] == word_to_find:
                score_keeper.append(sorted_competition_scores[q])
                count +=   1
                if count == 3:
                    first = score_keeper[0]
                    second = score_keeper[1]
                    third = score_keeper[2]
                    team_score.append(first + second + third)
                    score_keeper.clear()
                    count = 0
                    break

    #print(team_competition)
    #print(team_score)

    Team_List = list(zip(team_score,state_teams))
    sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
    sorted_score = [tup[0] for tup in sorted_team]
    sorted_final_team = [tup[1] for tup in sorted_team]


    if (len(sorted_final_team) > 1):
        if (sorted_score[0] == sorted_score[1]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[0]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[1]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 2):
        if (sorted_score[1] == sorted_score[2]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[1]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[2]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 3):
        if (sorted_score[2] == sorted_score[3]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[2]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[3]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

            first_tie = 0
            second_tie = 0

    if (len(sorted_final_team) > 4):
        if (sorted_score[3] == sorted_score[4]):
            for b in range(len(sorted_competition_poolFN)):
                if sorted_school[b] == sorted_final_team[3]:
                    first_tie = first_tie + sorted_competition_scores[b]
                
                if sorted_school[b] == sorted_final_team[4]:
                    second_tie = second_tie + sorted_competition_scores[b]
            
            if ( first_tie < second_tie):
                sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

            first_tie = 0
            second_tie = 0

    if ( len(sorted_competition_scores) >= 8):
        cutoff = sorted_competition_scores[7]
    else:
        cutoff = sorted_competition_scores[-1]
    # Begin Here
    for s in range(len(sorted_competition_poolFN)):

        objective.append(sorted_competition_scores[s])
        if sorted_competition_scores[s] >= cutoff:
            edgar = speech_state(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

    for g in range(len(sorted_competition_poolFN) - 1):
        if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
            sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
            sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

    #print(sorted_competition_scores)
    final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, objective))
    sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
    sorted_final_scores = [tup[0] for tup in sorted_final_list]
    sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
    sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
    final_city = [tup[3] for tup in sorted_final_list]
    final_school = [tup[4] for tup in sorted_final_list]
    final_objective = [tup[5] for tup in sorted_final_list]

    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
        


    sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
    print("-Individual Results-")
    with open(textfile, "a") as printer:
        printer.write("-Individual Results-\n")
    for z in range(len(sorted_final_poolFN)):
        with open(textfile, "a") as printer:
            if ( z < 3 ):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 3) :
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X   \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            elif ( z == 4 or z == 5):
                print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
            else:
                print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
                printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
    objective.clear()
    final_objective.clear()
    # End Here
    print("-Team Results-")
    with open(textfile, "a") as printer:
        printer.write("-Team Results-\n")
    for y in range(len(sorted_final_team)):
        with open(textfile, "a") as printer:
            if ( y == 0):
                print ("{}.   {}   {}     X ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X \n".format(y+1, sorted_final_team[y], sorted_score[y]))
            elif ( y == 1):
                print ("{}.   {}   {}     X ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}     X  \n".format(y+1, sorted_final_team[y], sorted_score[y]))
            else:
                print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
                printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))

    for h in range(len(firstname)):
        if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0] and school[h] != sorted_final_team[0]):
            eliminated[h] = "I"
            inter_lastname.append(lastname[h])
            inter_firstname.append(firstname[h])
            inter_school.append(school[h])
            inter_city.append(city[h])
            inter_high.append(high[h])
            inter_low.append(low[h])
        
        if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1] and school[h] != sorted_final_team[0]):
            eliminated[h] = "I"
            inter_lastname.append(lastname[h])
            inter_firstname.append(firstname[h])
            inter_school.append(school[h])
            inter_city.append(city[h])
            inter_high.append(high[h])
            inter_low.append(low[h])
        
        if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2] and school[h] != sorted_final_team[0]):
            eliminated[h] = "I"
            inter_lastname.append(lastname[h])
            inter_firstname.append(firstname[h])
            inter_school.append(school[h])
            inter_city.append(city[h])
            inter_high.append(high[h])
            inter_low.append(low[h])
        
        if (school[h] == sorted_final_team[0]):
            eliminated[h] = "I"
            inter_lastname.append(lastname[h])
            inter_firstname.append(firstname[h])
            inter_school.append(school[h])
            inter_city.append(city[h])
            inter_high.append(high[h])
            inter_low.append(low[h])

    interconference_teams.append(sorted_final_team[0])
    if len(sorted_final_team) > 1:
        interconference_wildcard_team.append(sorted_final_team[1])
        interconference_wildcard_score.append(sorted_score[1])

        interconference_wildcard_team.append(sorted_final_team[2])
        interconference_wildcard_score.append(sorted_score[2])

        interconference_wildcard_team.append(sorted_final_team[3])
        interconference_wildcard_score.append(sorted_score[3])

        interconference_wildcard_team.append(sorted_final_team[4])
        interconference_wildcard_score.append(sorted_score[4])
    '''
    for z in range(len(high)):
        with open(textfile, "a") as printer:
            printer.write(" First Name: {}, Last Name: {}, School: {}, City: {}, High: {}, Low: {}, \n".format(firstname[z], lastname[z], school[z], city[z], high[z], low[z]))
    '''


    with open(textfile, "a") as printer:
        printer.write("\n\n\n")

    competition_poolFN.clear()
    competition_poolLN.clear()
    competition_city.clear()
    competition_school.clear()
    team_competition.clear()
    combined_id.clear()
    sorted_combined_id.clear()
    sorted_competition_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    sorted_competition_city.clear()
    sorted_school.clear()
    team_score.clear()
    Team_List.clear()
    sorted_team.clear()
    sorted_score.clear()
    sorted_final_team.clear()
    final_school.clear()
    sorted_final_list.clear()
    sorted_final_scores.clear()
    sorted_competition_poolFN.clear()
    sorted_competition_poolLN.clear()
    final_city.clear()
    final_school.clear()
    scores.clear()

    
    lastname.clear()
    firstname.clear()
    school.clear()
    city.clear()
    district.clear()
    region.clear()
    eliminated.clear() 
    teams.clear()
    high.clear()
    low.clear()

# END OF SIMULATION FUNCTION. BEGINNING OF MAIN
    
def sorting():
    lanternoil = random.randint(1,100)
    max = 0
    if (lanternoil <= 50):
        max = 2
    elif(lanternoil <= 80):
        max = 4
    else:
        max = 8
    return max


def speech_district(objective):
    edinburg = 0
    brownsville = 0
    case = 0
    if (objective == 40 or objective == 36):
        waternoose = random.randint(1,100)
        if (waternoose <= 10):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 30):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 35 or objective == 31):
        waternoose = random.randint(1,100)
        if (waternoose <= 20):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 60):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 30 or objective == 25):
        waternoose = random.randint(1,100)
        if (waternoose <= 30):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 24 or objective == 19):
        waternoose = random.randint(1,100)
        if (waternoose <= 45):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 18 or objective == 13):
        waternoose = random.randint(1,100)
        if (waternoose <= 60):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 12 or objective == 7):
        waternoose = random.randint(1,100)
        if (waternoose <= 70):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    else:
        waternoose = random.randint(1,100)
        if (waternoose <= 80):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    district_essay = []

    with open('essays.txt','r') as w:
        for line in w:
            district_essay.append(float(line.strip()))
    district_essay.sort()

    police = 0
    flagger = True
    counter = 0
    while( counter <= 201 ):
        score_e = random.choice(district_essay)
        if ( score_e >= brownsville ) and ( score_e <= edinburg) and ( flagger == True):
            police = score_e
            flagger = False
        
        counter = counter + 1
        
    if ( flagger == True):
        if ( case == 1):
            police = 2.5
            
        if ( case == 2):
            police = 6.5
            
        if (case == 3):
            police = 9

    return police

def speech_region(objective):
    edinburg = 0
    brownsville = 0
    case = 0
    if (objective == 40 or objective == 36):
        waternoose = random.randint(1,100)
        if (waternoose <= 10):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 30):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 35 or objective == 31):
        waternoose = random.randint(1,100)
        if (waternoose <= 20):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 60):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 30 or objective == 25):
        waternoose = random.randint(1,100)
        if (waternoose <= 30):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 24 or objective == 19):
        waternoose = random.randint(1,100)
        if (waternoose <= 45):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 18 or objective == 13):
        waternoose = random.randint(1,100)
        if (waternoose <= 60):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 12 or objective == 7):
        waternoose = random.randint(1,100)
        if (waternoose <= 70):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    else:
        waternoose = random.randint(1,100)
        if (waternoose <= 80):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    region_essay = []

    region_essay.clear()
    with open('region_essays.txt','r') as w:
        for line in w:
            region_essay.append(float(line.strip()))
    region_essay.sort()

    police = 0
    flagger = True
    counter = 0
    while( counter <= 201 ):
        score_e = random.choice(region_essay)
        if ( score_e >= brownsville ) and ( score_e <= edinburg) and ( flagger == True):
            police = score_e
            flagger = False
        
        counter = counter + 1
        
    if ( flagger == True):
        if ( case == 1):
            police = 2.5
            
        if ( case == 2):
            police = 6.5
            
        if (case == 3):
            police = 9

    return police

def speech_state(objective):
    edinburg = 0
    brownsville = 0
    case = 0
    if (objective == 40 or objective == 36):
        waternoose = random.randint(1,100)
        if (waternoose <= 10):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 30):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 35 or objective == 31):
        waternoose = random.randint(1,100)
        if (waternoose <= 20):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 60):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 30 or objective == 25):
        waternoose = random.randint(1,100)
        if (waternoose <= 30):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 24 or objective == 19):
        waternoose = random.randint(1,100)
        if (waternoose <= 45):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 18 or objective == 13):
        waternoose = random.randint(1,100)
        if (waternoose <= 60):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    elif (objective == 12 or objective == 7):
        waternoose = random.randint(1,100)
        if (waternoose <= 70):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    else:
        waternoose = random.randint(1,100)
        if (waternoose <= 80):
            case = 1
            edinburg = 5
            brownsville = 0
        elif(waternoose <= 90):
            case = 2
            edinburg = 8
            brownsville = 5.1
        else:
            case = 3
            edinburg = 10
            brownsville = 8.1

    state_essay = []

    state_essay.clear()
    with open('state_essays.txt','r') as w:
        for line in w:
            state_essay.append(float(line.strip()))
    state_essay.sort()

    police = 0
    flagger = True
    counter = 0
    while( counter <= 201 ):
        score_e = random.choice(state_essay)
        if ( score_e >= brownsville ) and ( score_e <= edinburg) and ( flagger == True):
            police = score_e
            flagger = False
        
        counter = counter + 1
        
    if ( flagger == True):
        if ( case == 1):
            police = 2.5
            
        if ( case == 2):
            police = 6.5
            
        if (case == 3):
            police = 9

    return police

        

interconference_wildcard_team = []
interconference_wildcard_score = []
interconference_teams = []




sim("1", "results1A.txt", "South Plains College, Levelland", "Angelo State University, San Angelo", "Keller ISD", "Blinn College, Brenham Campus" )
sim("2", "results2A.txt", "Odessa College, Odessa", "Grayson College, Denison", "Panola College, Carthage", "Texas A&M University - Corpus Christi")
sim("3", "results3A.txt", "Abilene Christian University", "Tyler Junior College, Tyler", "Blinn College, Brenham Campus", "Texas State University - San Marcos")
sim("4", "results4A.txt", "Texas Tech University - Lubbock", "Texas A&M University - Commerce", "Sam Houston State University, Huntsville", "Texas A&M University - Corpus Christi")
sim("5", "results5A.txt", "Texas Tech University - Lubbock", "Prosper ISD", "Foster HS", "University of Texas-San Antonio")
sim("6", "results6A.txt", "University of Texas at Arlington", "Baylor University", "Katy Seven Lakes HS", "University of Texas-San Antonio")

# Append Wildcard

inter_wildcard = list(zip(interconference_wildcard_score, interconference_wildcard_team))
inter_wirdcard_sorter = sorted(inter_wildcard, key=lambda s: s[0], reverse=True)
inter_wildcard_final = [tup[0] for tup in inter_wirdcard_sorter]
inter_wildcard_winner = [tup[1] for tup in inter_wirdcard_sorter]

wildcard = open('names.csv')
file2 = csv.DictReader(wildcard)

for col in file2:
    if (col['School'] == inter_wildcard_winner[0]):

        is_there = True
        for a in range(len(inter_lastname)):
            if (col['LastName'] == inter_lastname[a]) and (col['FirstName'] == inter_firstname[a]):
                is_there = False
        
        if ( is_there == True ):
            inter_lastname.append(col['LastName'])
            inter_firstname.append(col['FirstName'])
            inter_school.append(col['School'])
            inter_city.append(col['City'])
            inter_high.append(((int(col['High']) + int(col['Low']))/2))
            inter_low.append(((int(col['High']) + int(col['Low']))/2))

interconference_teams.append(inter_wildcard_winner[0])
inter_wildcard_final.clear()
interconference_wildcard_score.clear()


for k in range(len(inter_firstname)):
    print("   {}   {},   {},   {} ".format(inter_firstname[k],inter_lastname[k],inter_school[k], inter_city[k]))


competition_poolFN = []
competition_poolLN = []
competition_scores = []
competition_city = []
competition_school = []
competition_high = []
competition_low = []
competition_objective = []

score_r = 0
team_score = []
team_competition = []

'''
    region_scores.clear()

    state_scores = []

    with open('state_scores.txt','r') as p:
        for line in p:
            scores.append(int(line.strip()))

    scores.sort()

    competition_scores.clear()
'''

# Clear results.txt
with open("results.txt","w") as printer:
    printer.write('')


# Append Inter-Conference Scores
state_scores = []
scores = []

with open('inter_scores.txt','r') as p:
    for line in p:
        scores.append(int(line.strip()))

scores.sort()


# Append Inter-Conference Essays
inter_essay = []
with open('state_essays.txt','r') as w:
    for line in w:
        inter_essay.append(float(line.strip()))
inter_essay.sort()

# Append  Inter-Conference scores
# region_scores.clear()

state_scores = []

with open('inter_scores.txt','r') as p:
    for line in p:
        scores.append(int(line.strip()))

scores.sort()

competition_scores.clear()


# Interconference
first_tie = 0
second_tie = 0
competition_scores.clear()
print(" -- Inter-Conference -- ")
with open("results.txt", "a") as printer:
    printer.write(" -- Inter-Conference --\n")
    printer.write(" May 4, 2019, University of Texas at Austin \n")
for j in range(len(inter_lastname)):
    
    competition_poolFN.append(inter_firstname[j])
    competition_poolLN.append(inter_lastname[j])
    competition_city.append(inter_city[j])
    competition_school.append(inter_school[j])
    mediator = sorting()
    competition_high.append(inter_high[j] + mediator)
    competition_low.append(inter_low[j] - mediator)

'''
for t in range(len(competition_poolFN)):
    score_state = random.choice(scores)
    competition_scores.append(score_state)
'''

for t in range(len(competition_poolFN)):
    flagger = True
    counter = 0
    while( counter <= 201 ):
        score_state = random.choice(scores)
        if ( score_state >= int(competition_low[t]) ) and ( score_state <= int(competition_high[t])) and ( flagger == True) and ( score_state < 38 ):
            competition_scores.append(score_state)
            flagger = False
        
        counter = counter + 1
        
    if ( flagger == True):
            if ( int(competition_low[t]) > 40 ):
                competition_scores.append(40)
            else:
                competition_scores.append(int(competition_low[t]))

competition_high.clear()
competition_low.clear()

combined_id = list(zip(competition_scores,competition_poolFN,competition_poolLN, competition_city, competition_school))
sorted_combined_id = sorted(combined_id, key=lambda x: x[0], reverse=True)
sorted_competition_scores = [tup[0] for tup in sorted_combined_id]
sorted_competition_poolFN = [tup[1] for tup in sorted_combined_id]
sorted_competition_poolLN = [tup[2] for tup in sorted_combined_id]
sorted_competition_city = [tup[3] for tup in sorted_combined_id]
sorted_school = [tup[4] for tup in sorted_combined_id]

for m in range(len(sorted_competition_poolFN)):
    print("{}.  {}   {},   {},   {},   {} ".format(m+1,sorted_competition_poolFN[m],sorted_competition_poolLN[m],sorted_school[m], sorted_competition_city[m],sorted_competition_scores[m]))

score_keeper = []
for e in range(len(interconference_teams)):
    word_to_find = interconference_teams[e]
    count = 0
    for q in range(len(sorted_school)):
        if sorted_school[q] == word_to_find:
          score_keeper.append(sorted_competition_scores[q])
          count +=   1
          if count == 3:
              first = score_keeper[0]
              second = score_keeper[1]
              third = score_keeper[2]
              team_score.append(first + second + third)
              score_keeper.clear()
              count = 0
              break

#print(team_competition)
#print(team_score)

Team_List = list(zip(team_score,interconference_teams))
sorted_team = sorted(Team_List, key=lambda x: x[0], reverse=True)
sorted_score = [tup[0] for tup in sorted_team]
sorted_final_team = [tup[1] for tup in sorted_team]


if (len(sorted_final_team) > 1):
    if (sorted_score[0] == sorted_score[1]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[0]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[1]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[0],sorted_final_team[1] = sorted_final_team[1], sorted_final_team[0]

        first_tie = 0
        second_tie = 0

if (len(sorted_final_team) > 2):
    if (sorted_score[1] == sorted_score[2]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[1]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[2]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[1],sorted_final_team[2] = sorted_final_team[2], sorted_final_team[1]

        first_tie = 0
        second_tie = 0

if (len(sorted_final_team) > 3):
    if (sorted_score[2] == sorted_score[3]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[2]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[3]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[2],sorted_final_team[3] = sorted_final_team[3], sorted_final_team[2]

        first_tie = 0
        second_tie = 0

if (len(sorted_final_team) > 4):
    if (sorted_score[3] == sorted_score[4]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[3]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[4]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[3],sorted_final_team[4] = sorted_final_team[4], sorted_final_team[3]

        first_tie = 0
        second_tie = 0

if (len(sorted_final_team) > 5):
    if (sorted_score[4] == sorted_score[5]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[4]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[5]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[4],sorted_final_team[5] = sorted_final_team[5], sorted_final_team[4]

        first_tie = 0
        second_tie = 0

if (len(sorted_final_team) > 6):
    if (sorted_score[5] == sorted_score[6]):
        for b in range(len(sorted_competition_poolFN)):
            if sorted_school[b] == sorted_final_team[5]:
                first_tie = first_tie + sorted_competition_scores[b]
            
            if sorted_school[b] == sorted_final_team[6]:
                second_tie = second_tie + sorted_competition_scores[b]
        
        if ( first_tie < second_tie):
            sorted_final_team[5],sorted_final_team[6] = sorted_final_team[6], sorted_final_team[5]

        first_tie = 0
        second_tie = 0

if ( len(sorted_competition_scores) >= 10):
    cutoff = sorted_competition_scores[9]
else:
    cutoff = sorted_competition_scores[-1]
'''
for s in range(len(sorted_competition_poolFN)):
    if sorted_competition_scores[s] >= cutoff:
        sorted_competition_scores[s] = sorted_competition_scores[s] + random.choice(inter_essay)
#print(sorted_competition_scores)
final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school))
sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
sorted_final_scores = [tup[0] for tup in sorted_final_list]
sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
final_city = [tup[3] for tup in sorted_final_list]
final_school = [tup[4] for tup in sorted_final_list]

for g in range(len(sorted_final_poolFN) - 1):
    if (sorted_final_scores[g] == sorted_final_scores[g+1]) and ( sorted_final_scores[g] >= cutoff):
        sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
        sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
        sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
        final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
        final_school[g+1], final_school[g] = final_school[g], final_school[g+1]

sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
print("-Individual Results-")
with open("results.txt", "a") as printer:
    printer.write("-Individual Results-\n")
for z in range(len(sorted_final_poolFN)): 
    with open("results.txt", "a") as printer:
        if ( z < 3 ):
            print("{}.   {}   {},   {},   {},   {}     X ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {}     X \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
        elif ( z == 3) :
            print("{}.   {}   {},   {},   {},   {}     X  ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write(str("{}.   {}   {},   {},   {},   {}     X \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z])))
        elif ( z == 4 or z == 5):
            print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {}     X   \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
        else:
            print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write(("{}.   {}   {},   {},   {},   {}   \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z])))
'''

    # Begin Here
for s in range(len(sorted_competition_poolFN)):

    competition_objective.append(sorted_competition_scores[s])
    if sorted_competition_scores[s] >= cutoff:
            edgar = speech_state(sorted_competition_scores[s])
            sorted_competition_scores[s] = sorted_competition_scores[s] + edgar

for g in range(len(sorted_competition_poolFN) - 1):
    if (sorted_competition_scores[g] == sorted_competition_scores[g+1]) and ( sorted_competition_scores[g] >= cutoff) and ( sorted_competition_scores[g] < 49 ):
        sorted_competition_scores[g] = sorted_competition_scores[g] + (random.randint(0,10)/10)
        sorted_competition_scores[g+1] = sorted_competition_scores[g+1] + (random.randint(0,10)/10)

#print(sorted_competition_scores)
final_list = list(zip(sorted_competition_scores,sorted_competition_poolFN,sorted_competition_poolLN, sorted_competition_city, sorted_school, competition_objective))
sorted_final_list = sorted(final_list, key=lambda s: s[0], reverse=True)
sorted_final_scores = [tup[0] for tup in sorted_final_list]
sorted_final_poolFN = [tup[1] for tup in sorted_final_list]
sorted_final_poolLN = [tup[2] for tup in sorted_final_list]
final_city = [tup[3] for tup in sorted_final_list]
final_school = [tup[4] for tup in sorted_final_list]
final_objective = [tup[5] for tup in sorted_final_list]

for g in range(len(sorted_final_poolFN) - 1):
    if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
        sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
        sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
        sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
        final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
        final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
        final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]

'''
    for g in range(len(sorted_final_poolFN) - 1):
        if ((sorted_final_scores[g] == sorted_final_scores[g+1]) and (sorted_final_scores[g] - final_objective[g]) < (sorted_final_scores[g+1] - final_objective[g+1])) and ( sorted_final_scores[g] >= cutoff):
            sorted_final_scores[g+1], sorted_final_scores[g] = sorted_final_scores[g], sorted_final_scores[g+1]
            sorted_final_poolFN[g+1], sorted_final_poolFN[g] = sorted_final_poolFN[g], sorted_final_poolFN[g+1]
            sorted_final_poolLN[g+1], sorted_final_poolLN[g] = sorted_final_poolLN[g], sorted_final_poolLN[g+1]
            final_city[g+1], final_city[g] = final_city[g], final_city[g+1]
            final_school[g+1], final_school[g] = final_school[g], final_school[g+1]
            final_objective[g+1], final_objective[g] = final_objective[g], final_objective [g+1]
'''
        


sorted_final_scores = [int(num) if isinstance(num, float) and num.is_integer() else num for num in sorted_final_scores]
print("-Individual Results-")
with open("results.txt", "a") as printer:
    printer.write("-Individual Results-\n")
for z in range(len(sorted_final_poolFN)):
    with open("results.txt", "a") as printer:
        if ( z < 3 ):
            print("{}.   {}   {},   {},   {},   {}     X ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
        elif ( z == 3) :
            print("{}.   {}   {},   {},   {},   {}     X ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
        elif ( z == 4 or z == 5):
            print("{}.   {}   {},   {},   {},   {}     X   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {},   {}     X  \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
        else:
            print("{}.   {}   {},   {},   {},   {}   ".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z],sorted_final_scores[z]))
            printer.write("{}.   {}   {},   {},   {},   {},   {}    \n".format(z+1, sorted_final_poolFN[z],sorted_final_poolLN[z],final_school[z], final_city[z], final_objective[z], sorted_final_scores[z]))
competition_objective.clear()
final_objective.clear()
    # End Here
print("-Team Results-")
with open("results.txt", "a") as printer:
    printer.write("-Team Results-\n")
for y in range(len(sorted_final_team)):
    with open("results.txt", "a") as printer:
        if ( y == 0):
            print ("{}.   {}   {}     X ".format(y+1, sorted_final_team[y], sorted_score[y]))
            printer.write("{}.   {}   {}     X \n".format(y+1, sorted_final_team[y], sorted_score[y]))
        elif ( y == 1):
            print ("{}.   {}   {}     X ".format(y+1, sorted_final_team[y], sorted_score[y]))
            printer.write("{}.   {}   {}     X  \n".format(y+1, sorted_final_team[y], sorted_score[y]))
        else:
            print ("{}.   {}   {}   ".format(y+1, sorted_final_team[y], sorted_score[y]))
            printer.write("{}.   {}   {}   \n".format(y+1, sorted_final_team[y], sorted_score[y]))
'''
for h in range(len(firstname)):
    if (firstname[h] == sorted_final_poolFN[0] and lastname[h] == sorted_final_poolLN[0] and school[h] == final_school[0]):
        eliminated[h] = "S"
    
    if (firstname[h] == sorted_final_poolFN[1] and lastname[h] == sorted_final_poolLN[1] and school[h] == final_school[1]):
        eliminated[h] = "S"
    
    if (firstname[h] == sorted_final_poolFN[2] and lastname[h] == sorted_final_poolLN[2] and school[h] == final_school[2]):
        eliminated[h] = "S"
    
    if (school[h] == sorted_final_team[0]):
        eliminated[h] = "S"
'''

'''
state_teams.append(sorted_final_team[0])
if len(sorted_final_team) > 1:
    state_wildcard_team.append(sorted_final_team[1])
    state_wildcard_score.append(sorted_score[1])
'''

with open("results.txt", "a") as printer:
    printer.write("\n\n\n")

competition_poolFN.clear()
competition_poolLN.clear()
competition_city.clear()
competition_school.clear()
team_competition.clear()
combined_id.clear()
sorted_combined_id.clear()
sorted_competition_scores.clear()
sorted_competition_poolFN.clear()
sorted_competition_poolLN.clear()
sorted_competition_city.clear()
sorted_school.clear()
team_score.clear()
Team_List.clear()
sorted_team.clear()
sorted_score.clear()
sorted_final_team.clear()
final_school.clear()
sorted_final_list.clear()
sorted_final_scores.clear()
sorted_competition_poolFN.clear()
sorted_competition_poolLN.clear()
final_city.clear()
final_school.clear()
scores.clear()

utopia = ''

print(utopia)

# Restart at 6A District 3 ( Region 1 )

