def match(me, other_array):
    others=[]
    print(other_array)
    user = [[me['country'], me['age'], me['country'], me['occupation'], me['myers'], me["interests"], me["sports"], me["songs"], me["languages"], me["food"]], [me['gender'], me['ethnicity'], me['class'], me['university']], [me['username'], me['email'], me['name']]]
    for x in other_array:
        print(x)
        if x["complete"] == "true":
            temp = [[x['country'], x['age'], x['country'], x['occupation'], x['myers'], x["interests"], x["sports"], x["songs"], x["languages"], x["food"]], [x['gender'], x['ethnicity'], x['class'], x['university']], [x['username'], x['email'], x['name']]]
            others.append(temp)
    rating_array=[]
    common_interests=[]
    print("ouoeuaoeuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    print(others)
    for other in others:
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
                        common_interests.append(other_string[i])
        if score > 10:
            score = 10
        if score < 0:
            score = 0
        rating_array.append([user[2],score])
    print(rating_array)
    return rating_array



# Example input = 
# user: [[location, age,], [gender, ethnicity], Michael]
# others: [[[location, age,], [gender, ethnicity]], [[location, age,], [gender, ethnicity]]]]