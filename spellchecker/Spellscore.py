from math import exp


def spell_sim(spell1, spell2, sqsigma):

    """define subscore fuction, where x is difference
    between the expected postion based on spell1
    and real position of character in spell2 """

    subscore = lambda x: exp(-(x**2)/(2*sqsigma))

#   initiate score to zero

    sim = 0

    for i in range(len(spell1)):
        for j in range(len(spell2)):
            if i+j < len(spell2) and spell2[i+j] == spell1[i]:
                sim += subscore(j)
                break
            if i >= j and i-j < len(spell2) and spell2[i-j] == spell1[i]:
                sim += subscore(j)
                break

    return sim/len(spell1)


def score(spell1,spell2,sqsigma=3):
    sim12 = spell_sim(spell1, spell2, sqsigma)
    sim21 = spell_sim(spell2, spell1, sqsigma)

#   final_score is F1 score of sim12 and sim21
    final_score = 2*sim12*sim21
    if final_score > 0 :
        final_score /= (sim12+sim21)

    return final_score






