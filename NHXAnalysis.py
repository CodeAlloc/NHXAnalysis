import csv
apercent = {}
apercent["A"] = 0
apercent["B"] = 0
apercent["C"] = 0
apercent["N"] = 0
questions = [
	{"q": "Would you call yourself a thinker", "f": "N"},
	{"q": "Are you creative", "f": "N"},
	{"q": "Do you like philosophy", "f": "N"},
	{"q": "Do you like to think about complex questions", "f": "N"},
	{"q": "Do you have an interest in artisitc pursuits like painting and writing", "f": "N"},
	{"q": "Do you like initiating conversations", "f": "A"},
	{"q": "Do you like to start talks with new people", "f": "A"},
	{"q": "Is it easy for you to adjust in an enviroment where you initially do not know anyone", "f": "A"},
	{"q": "Are you social", "f": "A"},
	{"q": "Do you like social events (parties, fests and events)", "f": "A"},
	{"q": "Do you mostly make your decisions by heart", "f": "B"},
	{"q": "Do you put others before yourself", "f": "B"},
	{"q": "Do you think that one should change their views if they hurt someone", "f": "B"},
	{"q": "Do you often get lost in your feelings", "f": "B"},
	{"q": "Are you run more by your feelings than logic", "f": "B"},
	{"q": "Can you make a timetable and stick to it", "f": "C"},
	{"q": "Do you usually follow the rules/laws", "f": "C"},
	{"q": "Are you organised", "f": "C"},
	{"q": "Do you plan before doing something", "f": "C"},
	{"q": "Are you ok with following orders", "f": "C"}
]
def question(index, inp, func):
	if bool(input(str(index + 1) + ". " + inp + "? Yes/No:\t").lower().strip("no. \t")):
		apercent[func] = apercent[func] + 20
try:
     for q in range(len(questions)):
          question(q, questions[q]["q"], questions[q]["f"])
except KeyboardInterrupt:
     exit(0)
print("Your extroversion percentage : ", apercent["A"], "%")
print("Your creativity percentage : ", apercent["N"], "%")
print("Your feeling percentage : ", apercent["B"], "%")
print("Your conscientious percentage : ", apercent["C"], "%")
if apercent["N"] > 50:
    sn = "N"
else:
    sn = "S"
if apercent["A"] > 50:
    ie = "E"
else:
    ie = "I"

if apercent["C"] > 50:
    jp = "J"
else:
    jp = "P"

if apercent["B"] > 50:
    tf = "F"
else:
    tf = "T"
ptype = ie + sn + tf + jp
print("Your personality type is: ", ptype)
if ptype == "INTP":
	print("Your career choices are: Physicists, chemists, biologists, photographers, strategic planners," 
          " mathematicians,"
          " university professors, computer programmers, computer animators, technical writers, engineers, lawyers, "
          "forensic researchers, writers, artists, psychologists, social scientists, systems analysts, researchers,"
          " surveyors. Highly analytical, you can discover connections between two seemingly unrelated things, "
          "and work best when allowed to use your imagination and critical thinking. You like working independently with creative"
          " freedom which will help you realise your full poetential. In difficult circumstances, you do not like taking"
          "orders from other people and [prefer it when things go as you personally like them to be")
elif ptype == "ENTP":
	print("Your career choices are:  Entrepreneurs, lawyers, psychologists, consultants, sales representatives,"
          " actors, engineers, scientists, inventors, marketers, computer programmers, comedians, computer analysts,"
          " credit investigators, journalists, psychiatrists, public relations, designers, writers, artists, musicians,"
          " politicians. Very freedom-oriented, youb need a career which allows you to act independent and express"
          " your creativity and insight.You do not like following rules if they do not make sense to you and prefer working independently.")
elif ptype == "INTJ":
	print("Your career choices are: Scientists, engineers, professors, teachers, medical doctors, dentists,"
          " corporate strategists, organization"
          " founders, business administrators, managers, military, lawyers, judges, computer programmers,"
          " system analysts, computer specialists, psychologists, photographers, research department managers,"
          " researchers, university instructors. You have a particular skill at grasping difficult,"
          " complex concepts and building strategies.")
elif ptype == "ENTJ":
	print(" Your career choices are: Business executives, CEOs, organization founders, business administrators,"
          " managers, entrepreneurs, "
          "judges, lawyers, computer consultants, university professors, politicians, credit investigators, "
          "labor relations worker, marketing department manager, mortgage banker, systems analysts, scientists. "
          "They are born to lead and can steer the organization towards their vision, using their excellent organizing "
          "and understanding of what needs to get done.")

elif ptype == "INFP":
	print("Your career choices are: Writers, artists, counselors, social workers, English teachers, fine arts teachers,"
          "child care workers,"
          " clergy, missionaries, psychologists, psychiatrists, scientists, political activists, editors,"
          " education consultants, journalists, religious educators, social scientists."
          " Driven by a strong sense of personal values, they are also highly creative and"
          " can offer support from behind the scenes.")
elif ptype == "ENFP":
	print("Your career choices are: Actors, journalists, writers, musicians, painters, consultants, psychologists, "
          "psychiatrists,"
          " entrepreneurs, teachers, counselors, politicians, television reporters, marketers, scientists,"
          " sales representatives, artists, clergy, public relations, social scientists, social workers."
          " Very creative and fun- loving, they excel at careers which allow them to express their ideas"
          " and spontaneity.")
elif ptype == "INFJ":
	print("Your career choices are: Counselors, clergy, missionaries, teachers, medical doctors, dentists,"
          " chiropractors, psychologists,"
          " psychiatrists, writers, musicians, artists, psychics, photographers, child care workers,"
          " education consultants, librarians, marketers, scientists, social workers."
          " Blessed with an idealistic vision, they do best when they seek to make that vision a reality.")
elif ptype == "ENFJ":
	print("Your career choices are: Teachers, consultants, psychiatrists, social workers, counselors, clergy,"
          " sales representative,"
          " human resources, managers, events coordinators, politicians, diplomats, writers, actors, designers, "
          "musicians, religious workers, writers. They have a gift of encouraging others actualize themselves,"
          " and provide excellent leadership.")
elif ptype == "ISFP":
	print("Your career choices are: Artists, musicians, composers, designers, child care workers, social workers,"
          " counselors, teachers,"
          " veterinarians, forest rangers, bookkeepers, carpenters, personal service workers, clerical supervisors,"
          " secretaries, dental and medical staffers, waiters and waitresses, chefs, nurses, mechanics,"
          " physical therapists, x-ray technicians. They tend to do well in the arts, as well"
          " as helping others and working with people.")
elif ptype == "ESFP":
	print("Your career choices are: Actors, painters, comedians, sales representatives, teachers, counselors,"
          " social workers, child care,"
          " fashion designers, interior decorators, consultants, photographers, musicians, human resources managers,"
          "clerical supervisors, coaches, factory supervisors, food service workers, receptionists, recreation workers,"
          " religious educators, respiratory therapists. "
          "Optimistic and fun-loving, their enthusiasm is great for motivating others.")

elif ptype == "ISTP":
	print("Your career choices are: Police, detectives, forensic pathologists, computer programmers, system analysts,"
          " computer specialists,"
          " engineers, carpenters, mechanics, pilots, drivers, athletes, entrepreneurs, firefighters, paramedics,"
          " construction workers, dental hygienists, electrical engineers, farmers, military, probation officers,"
          " steelworkers, transportation operatives. With the ability to stay calm under pressure,"
          " they excel in any job which requires immediate action.")
elif ptype == "ESTP":
	print("Your career choices are: Sales representatives, marketers, police, detectives, paramedics,"
          " medical technicians, computer technicians,"
          " computer technical support, entrepreneurs, comedians, agents, firefighters, military, auditors, carpenters,"
          " craft workers, farmers, laborers, service workers, transportation operatives. They have a gift for reacting"
          "to and solving immediate problems, and persuading other people.")
elif ptype == "ISFJ":
	print("Your career choices are:  Interior decorators, designers, nurses, administrators, managers, secretaries, "
          "child care/early childhood development, social work, counselors, paralegals, clergy, office managers,"
          " shopkeepers, bookkeepers, gardeners, clerical supervisors, curators, family practice physicians,"
          " health service workers, librarians, medical technologists, typists."
          " Tradition-oriented and down-to-earth, they do best in jobs where"
          " they can help people achieve their goals, or where structure is needed.")
elif ptype == "ESFJ":
	print("Your career choices are: Home economics, nursing, teaching, administrators, child care,"
          " family practice physician, clergy,"
          " office managers, counselors, social workers, bookkeeping, accounting, secretaries,"
          " organization leaders, dental assistants, radiological technologists,"
          " receptionists, religious educators, speech pathologists."
          " They do best in jobs where they can apply their natural"
          " warmth at building relationships with other people.")
elif ptype == "ISTJ":
	print("Your career choices are:  Business executives, administrators and managers, accountants,"
          " police, detectives, judges, lawyers, "
          "medical doctors, dentists, computer programmers, systems analysts, computer specialists, auditors,"
          " electricians, math teachers, mechanical engineers, steelworkers, technicians."
          " Similar to the House husbands, they have a knack for detail and memorization,"
          " but work more behind the scenes instead of up front as a leader. ")
elif ptype == "ESTJ":
	print("Your career choices are: Teacher, Professor, "
          "Military, business administrators, managers, police/detective work,"
          " judges,"
          " financial officers, teachers,"
          " sales representatives, government workers, insurance agents, underwriters, nursing administrators,"
          " trade and technical teachers, Natural leaders, they work best when"
          " they are in charge and enforcing the rules.")
else:
	exit(-1)