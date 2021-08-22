def match(me, other_array):
    others=[]
    user = [[me['country'], me['age'], me['occupation'], me['myers'], me["interests"], me["sports"], me["songs"], me["languages"], me["food"]], [me['gender'], me['ethnicity'], me['class'], me['university']], [me['username'], me['email'], me['name'], me['country'], me['ethnicity'], me['gender']]]
    for x in other_array:
        if x["complete"] == "true":
            temp = [[x['country'], x['age'], x['occupation'], x['myers'], x["interests"], x["sports"], x["songs"], x["languages"], x["food"]], [x['gender'], x['ethnicity'], x['class'], x['university']], [x['username'], x['email'], x['name'], x['country'], x['ethnicity'], x['gender']]]
            others.append(temp)
    rating_array=[]
    for other in others:
        common_interests=[]
        score=5
        user_upgrades=user[0]
        user_downgrades=user[1]
        other_upgrades=other[0]
        other_downgrades=other[1]
        for user_stat in user_upgrades:
            for other_stat in other_upgrades:
                user_string = user_stat.split(',')
                other_string = other_stat.split(',')
                for i in range(len(other_string)):
                    if other_string[i] in user_string:
                        score += 1
                        common_interests.append(other_string[i])
        for user_stat in user_downgrades:
            for other_stat in other_downgrades:
                user_string = user_stat.split(',')
                other_string = other_stat.split(',')
                for i in range(len(other_string)):
                    if other_string[i] in user_string:
                        score -= 1
        if score > 10:
            score = 10
        if score < 0:
            score = 0
        rating_array.append([other[2],score,common_interests])
    print(rating_array)
    return rating_array



# Example input = 
# user: [[location, age,], [gender, ethnicity], Michael]
# others: [[[location, age,], [gender, ethnicity]], [[location, age,], [gender, ethnicity]]]]

def stats(me, scores):
    potential_matches = 0
    different_countries = 0
    different_genders = 0
    different_ethnicites = 0
    for person in scores:
        if person[1] > 7:
            potential_matches += 1
        if person[0][3] != me["country"]:
            different_countries += 1
        if person[0][5] != me["gender"]:
            different_genders += 1
        if person[0][4] != me["ethnicity"]:
            different_ethnicites += 1

    return [potential_matches, different_countries, different_genders, different_ethnicites]
