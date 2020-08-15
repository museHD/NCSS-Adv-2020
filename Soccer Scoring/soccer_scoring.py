for line in open("commentary.txt"):
	line_list = line.strip().split()
	team1,team2 = line_list[0],line_list[2]
	break

score1,score2 = -1,-1
for linee in open("commentary.txt"):
	morelines = linee.strip().split()
	if team1 in morelines:
		score1 += 1

	if team2 in morelines:
		score2 += 1

if score1 > score2:
	print(f"{team1} {score1}")
	print(f"{team2} {score2}")
else:
	print(f"{team2} {score2}")
	print(f"{team1} {score1}")


# scorelist = [score1,score2]
# scorelist.sort()
# scorelist.reverse()

# final_scores = {score1:team1, score2:team2}

# for scores in scorelist:
# 	print(f"{final_scores[scores]} {scores}")

