def match(user, others):
    rating_array=[]
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
        rating_array.append([user[2],score])
    return rating_array


# Example input = 
# user: [[location, age,], [gender, ethnicity], Michael]
# others: [[[location, age,], [gender, ethnicity]], [[location, age,], [gender, ethnicity]]]]