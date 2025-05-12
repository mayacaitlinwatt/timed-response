from csv import reader 
import csv

# def stringIsNumber (string):
# 	try:
# 		print(int(string))
# 		return true
# 	except Exception as e:
# 		return false



# wordDataDict = { 'soze': 'j, 1', 
# 'strang': 'j, 1',
# 'hid':'f, 0',
# 'slew': 'j, 1',
# 'rang':'f, 0',
# 'blowed': 'j, 0',
# 'lit':'f, 0',
# 'glided':'f, 0',
# 'excote': 'j, 1',
# 'dived': 'f, 0' ,
# 'shined': 'j, 0',
# 'sang':'f, 0',
# 'blew':'f, 0',
# 'knowed': 'j, 0',
# 'ringed': 'j, 0',
# 'drinked': 'j, 0',
# 'slowed': 'j, 0',
# 'wringed': 'j, 0',
# 'grinded': 'j, 0',
# 'blound': 'j, 1',
# 'wrote':'f, 0',
# 'blank': 'j, 1',
# 'sode': 'j, 1',
# 'blit': 'j, 1',
# 'glid': 'j, 1',
# 'singed': 'j, 0',
# 'flew':'f, 0',
# 'rew': 'j, 1',
# 'grew':'f, 0',
# 'thrived':'f, 0',
# 'sid': 'j, 1',
# 'linked':'f, 0',
# 'whined':'f, 0',
# 'pang': 'j, 1',
# 'sprang':'f, 0',
# 'springed': 'j, 0',
# 'rowed':'f, 0',
# 'knew':'f, 0',
# 'whone': 'j, 1',
# 'snowed':'f, 0',
# 'blinded':'f, 0',
# 'snew': 'j, 1',
# 'growed': 'j, 0',
# 'slid':' f, 0',
# 'shone': ' f, 0',
# 'blighted':' f, 0',
# 'dove':' f, 0',
# 'throwed': 'j, 0',
# 'threw':' f, 0',
# 'wrang':' f, 0',
# 'lighted': 'j, 0',
# 'sank':' f, 0',
# 'rode':' f, 0',
# 'pinged': ' f, 0',
# 'rised':  'j, 0',
# 'ground':' f, 0',
# 'throve': 'j, 1',
# 'sided': ' f, 0',
# 'sinked':  'j, 0',
# 'slided':  'j, 0',
# 'sided': ' f, 0',
# 'sized': ' f, 0',
# 'flowed':  'j, 0',
# 'lank' : 'j, 1',
# 'excited': ' f, 0',
# 'stringed':  'j, 0',
# 'rose':' f, 0',
# 'rided': ' f, 0',
# 'hided':  'j, 0',
# 'blinked': ' f, 0',
# 'drank':'f, 0',
# 'writed':  'j, 0',
# 'bled': 'f, 0',
# 'bleeded': 'j, 0',
# 'kned' : 'j, 1',
# 'kneaded':' f, 0',
# 'bred': ' f, 0',
# 'breeded': 'j, 0',
# 'bed' : 'j, 1',
# 'beaded':' f, 0',
# 'fed':' f, 0',
# 'feeded': 'j, 0',
# 'ned' : 'j, 1',
# 'needed':' f, 0',
# 'flung':' f, 0',
# 'flinged': 'j, 0',
# 'fluck': 'j, 1',
# 'flicked':' f, 0',
# 'spun':' f, 0',
# 'spinned': 'j, 0',
# 'grun': 'j, 1',
# 'grinned':' f, 0',
# 'stuck':' f, 0',
# 'sticked': 'j, 0',
# 'cluck': 'j, 1',
# 'clicked':' f, 0',
# 'won':' f, 0',
# 'winned': 'j, 0',
# 'son': 'j, 1',
# 'sinned':' f, 0',
# 'wept':' f, 0',
# 'weeped': 'j, 0',
# 'bept': 'j, 1',
# 'beeped':' f, 0',
# 'dreamt':' f, 0',
# 'dreamed': 'j, 0',
# 'screamt': 'j, 1',
# 'screamed':' f, 0',
# 'meant':' f, 0',
# 'meaned': 'j, 0',
# 'beamt': 'j, 1',
# 'beamed':' f, 0',
# 'leapt':' f, 0',
# 'leaped': 'j, 0',
# 'pept': 'j, 1',
# 'peeped':' f, 0',
# 'froze':' f, 0',
# 'freezed': 'j, 0',
# 'snoze': 'j, 1',
# 'sneezed':' f, 0',
# 'spoke':' f, 0',
# 'speaked': 'j, 0',
# 'loke': 'j, 1',
# 'leaked':' f, 0',
# 'stole':' f, 0',
# 'stealed': 'j, 0',
# 'sole': 'j, 1',
# 'sealed':' f, 0',
# 'wove':' f, 0',
# 'weaved': 'j, 0',
# 'tose': 'j, 1',
# 'teased':' f, 0',
# 'bent':' f, 0',
# 'bended': 'j, 0',
# 'bont': 'j, 1',
# 'bonded':' f, 0',
# 'built':' f, 0',
# 'builded': 'j, 0',
# 'bount': 'j, 1',
# 'bounded':' f, 0',
# 'lent':' f, 0',
# 'lended': 'j, 0',
# 'lant': 'j, 1',
# 'landed':' f, 0',
# 'sent':' f, 0',
# 'sended': 'j, 0',
# 'fent': 'j, 1',
# 'fended':' f, 0',
# 'spent':' f, 0',
# 'spended': 'j, 0',
# 'blent': 'j, 1',
# 'blended':' f, 0',
# '': ',' } 


wordDataDict = { 'soze': 'j, 1, i', 
'strang': 'j, 1, i',
'hid':'f, 0, i',
'slew': 'j, 1, i',
'rang':'f, 0, i',
'blowed': 'j, 0, r',
'lit':'f, 0, i',
'glided':'f, 0, r',
'excote': 'j, 1, i',
'dived': 'f, 0, r' ,
'shined': 'j, 0, r',
'sang':'f, 0, i',
'blew':'f, 0, i',
'knowed': 'j, 0, r',
'ringed': 'j, 0, r',
'drinked': 'j, 0, r',
'slowed': 'j, 0, r',
'wringed': 'j, 0, r',
'grinded': 'j, 0, r',
'blound': 'j, 1, i',
'wrote':'f, 0, i',
'blank': 'j, 1, i',
'sode': 'j, 1, i',
'blit': 'j, 1, i',
'glid': 'j, 1, i',
'singed': 'j, 0, r',
'flew':'f, 0, i',
'rew': 'j, 1, i',
'grew':'f, 0, i',
'thrived':'f, 0, r',
'sid': 'j, 1, i',
'linked':'f, 0, r',
'whined':'f, 0, r',
'pang': 'j, 1, i',
'sprang':'f, 0, i',
'springed': 'j, 0, r',
'rowed':'f, 0, r',
'knew':'f, 0, i',
'whone': 'j, 1, i',
'snowed':'f, 0, r',
'blinded':'f, 0, r',
'snew': 'j, 1, i',
'growed': 'j, 0, r',
'slid':' f, 0, i',
'shone': ' f, 0, i',
'blighted':' f, 0, r',
'dove':' f, 0, i',
'throwed': 'j, 0, r',
'threw':' f, 0, i',
'wrang':' f, 0, i',
'lighted': 'j, 0, r',
'sank':' f, 0, i',
'rode':' f, 0, i',
'pinged': ' f, 0, r',
'rised':  'j, 0, r',
'ground':' f, 0, i',
'throve': 'j, 1, i',
'sided': ' f, 0, r',
'sinked':  'j, 0, r',
'slided':  'j, 0, r',
'sided': ' f, 0, r',
'sized': ' f, 0, r',
'flowed':  'j, 0, r',
'lank' : 'j, 1, i',
'excited': ' f, 0, r',
'stringed':  'j, 0, r',
'rose':' f, 0, i',
'rided': ' f, 0, r',
'hided':  'j, 0, r',
'blinked': ' f, 0, r',
'drank':'f, 0, i',
'writed':  'j, 0, r',
'bled': 'f, 0, i',
'bleeded': 'j, 0, r',
'kned' : 'j, 1, i',
'kneaded':' f, 0, r',
'bred': ' f, 0, i',
'breeded': 'j, 0, r',
'bed' : 'j, 1, i',
'beaded':' f, 0, r',
'fed':' f, 0, i',
'feeded': 'j, 0, r',
'ned' : 'j, 1, i',
'needed':' f, 0, r',
'flung':' f, 0, i',
'flinged': 'j, 0, r',
'fluck': 'j, 1, i',
'flicked':' f, 0, r',
'spun':' f, 0, i',
'spinned': 'j, 0, r',
'grun': 'j, 1, i',
'grinned':' f, 0, r',
'stuck':' f, 0, i',
'sticked': 'j, 0, r',
'cluck': 'j, 1, i',
'clicked':' f, 0, r',
'won':' f, 0, i',
'winned': 'j, 0, r',
'son': 'j, 1, i',
'sinned':' f, 0, r',
'wept':' f, 0, i',
'weeped': 'j, 0, r',
'bept': 'j, 1, i',
'beeped':' f, 0, r',
'dreamt':' f, 0, i',
'dreamed': 'j, 0, r',
'screamt': 'j, 1, i',
'screamed':' f, 0, r',
'meant':' f, 0, i',
'meaned': 'j, 0, r',
'beamt': 'j, 1, i',
'beamed':' f, 0, r',
'leapt':' f, 0, i',
'leaped': 'j, 0, r',
'pept': 'j, 1, i',
'peeped':' f, 0, r',
'froze':' f, 0, i',
'freezed': 'j, 0, r',
'snoze': 'j, 1, i',
'sneezed':' f, 0, r',
'spoke':' f, 0, i',
'speaked': 'j, 0, r',
'loke': 'j, 1, i',
'leaked':' f, 0, r',
'stole':' f, 0, i',
'stealed': 'j, 0, r',
'sole': 'j, 1, i',
'sealed':' f, 0, r',
'wove':' f, 0, i',
'weaved': 'j, 0, r',
'tose': 'j, 1, i',
'teased':' f, 0, r',
'bent':' f, 0, i',
'bended': 'j, 0, r',
'bont': 'j, 1, i',
'bonded':' f, 0, r',
'built':' f, 0, i',
'builded': 'j, 0, r',
'bount': 'j, 1, i',
'bounded':' f, 0, r',
'lent':' f, 0, i',
'lended': 'j, 0, r',
'lant': 'j, 1, i',
'landed':' f, 0, r',
'sent':' f, 0, i',
'sended': 'j, 0, r',
'fent': 'j, 1, i',
'fended':' f, 0, r',
'spent':' f, 0, i',
'spended': 'j, 0, r',
'blent': 'j, 1, i',
'blended':' f, 0, r',
'swinged':' f, 0, r',
'brang':' f, 0, i',
'bringed':' j, 0, r',
'swang':' j, 1, i',
'': ',,' }


def reWrite_2groups (outfile):

	#makes a space where you can write to the outfile 
	with open(outfile, 'a') as f:

		fieldnames = ['user', 'word', 'response time', 'response' , 'correct response', 'user correct?', 'word important?','word average rt', 'word type', 'what language do you speak most often?', 'what language do you speak at home?', 'what is your mother tongue?', 'what is your age?', 'what is your sex?','group']

		writer = csv.DictWriter(f, fieldnames = fieldnames)
		writer.writeheader()


		#reference list that always reflects the header of the inData
		headerRef = []
		with open('cleandata.csv', 'r') as read_object:
			myReader  = reader(read_object)
			count = 0
			for row in myReader:
				if count == 0:
					headerRef = row
				count = count + 1000





		#gets AVG data for each word 
		avgCount = 7
		wordAvg = {}
		while avgCount < len(headerRef): 
			with open('cleandata.csv', 'r') as read_object0:
				myReader = reader(read_object0)
				lilCount = 0

				avgTotal = 0
				avgNumUsers = 0 

				for row in myReader:

					print(row[avgCount])

					if lilCount == 0:
						print(':0')
					else:
						if row[avgCount].isspace() or not row[avgCount]:
							print('nope')
						else: 
							avgTotal = avgTotal + int(row[avgCount])
							avgNumUsers = avgNumUsers + 1


					lilCount = lilCount + 1

				print(avgTotal)
				print(avgNumUsers)
				if avgNumUsers > 0:
					wordAvg[headerRef[avgCount].split(' ')[0]] = avgTotal/avgNumUsers




			avgCount = avgCount + 2
		print(wordAvg)
		#gets AVG data ^




		#gets %-of-catch-trials-incorrect 
		
		#avgCount = 7
		catchCount = 7
		
		#wordAvg = {}
		percentOfCTIncorrect = {}

		while catchCount < len(headerRef): 
			with open('cleandata.csv', 'r') as read_object1:
				myReader1 = reader(read_object1)
				lilCount1 = 0

				avgTotal1 = 0
				avgNumUsers1 = 0
				numberCorrect1 = 0

				for row in myReader1:

					print(row[catchCount])

					if lilCount1 == 0:
						print(':0')
					else:
						if row[catchCount].isspace() or not row[catchCount]:
							print('nope')
						
						elif row[catchCount] = 'f' and row[catchCount]  and (user is correct):
							numberCorrect = numberCorrect + 1
							avgNumUsers1 = avgNumUsers1 + 1

						else: 
							#avgTotal = avgTotal + int(row[avgCount])
							avgNumUsers1 = avgNumUsers1 + 1


					lilCount1 = lilCount1 + 1

				print(avgTotal1)
				print(avgNumUsers1)
				if avgNumUsers1 > 0:
					percentOfCTIncorrect[headerRef[catchCount].split(' ')[0]] = numberCorrect/avgNumUsers1




			catchCount = catchCount + 2
		print(percentOfCTIncorrect)

		#end of my bullshit





		globalCount = 7

		

		while globalCount < 6:
			
			with open('cleandata.csv', 'r') as read_object:
				myReader = reader(read_object)
				for row in myReader:
					wordVar = headerRef[i].split(' ')[0]
					answrDict = {}
					answrDict['user'] = row[0]
					answrDict['word'] = wordVar
					answrDict['response time'] = row[i]
					answrDict['reponse'] = row[i + 1]
					answrDict['correct response'] = wordDataDict[wordVar].split(',')[0]
					answrDict['user correct?']
					answrDict['word important?'] = wordDataDict[wordVar].split(',')[1]
					answrDict['what language do you speak most often?'] = row[1]
					answrDict['what language do you speak at home?'] = row[2]
					answrDict['what is your mother tongue?'] = row[3]
					answrDict['what is your age'] = row[4]
					answrDict['what is your sex?'] = row[5]
					answrDict['group'] = row[6]
					writer.writerow(answrDict)





		while globalCount < len(headerRef):
			#makes a space where you can read the infile
			with open('cleandata.csv', 'r') as read_object:
				myReader = reader(read_object)
				lilCount = 0
				for row in myReader:
					if lilCount == 0:
						print(':0')
					else:
						wordVar = headerRef[globalCount].split(' ')[0]
						correctResponse = wordDataDict[wordVar].split(',')[0]
						answrDict = {}
						answrDict['user'] = row[0]
						answrDict['word'] = headerRef[globalCount].split(' ')[0]
						answrDict['response time'] = row[globalCount]
						answrDict['response'] = row[globalCount + 1]
						answrDict['correct response'] = correctResponse

						if 'j' in row[globalCount + 1] or 'f' in row[globalCount + 1]:
							if row[globalCount + 1] in correctResponse:
								answrDict['user correct?'] = 'correct'
							else:
								answrDict['user correct?'] = 'incorrect'
						else: 
							answrDict['user correct?'] = ''

						

						answrDict['word important?'] = wordDataDict[wordVar].split(',')[1]

						if 'stole' not in wordVar and 'stealed' not in wordVar and 'sole' not in wordVar and 'sealed' not in wordVar and wordVar:
							answrDict['word average rt'] = wordAvg[wordVar]
						else:
							answrDict['word average rt'] = 0

						print(wordVar)
						answrDict['word type'] = wordDataDict[wordVar].split(',')[2]

						answrDict['what language do you speak most often?'] = row[1]
						answrDict['what language do you speak at home?'] = row[2]
						answrDict['what is your mother tongue?'] = row[3]
						answrDict['what is your age?'] = row[4]
						answrDict['what is your sex?'] = row[5]
						answrDict['group'] = row[6]
						writer.writerow(answrDict)
					lilCount = lilCount + 1


			globalCount = globalCount + 2













reWrite_2groups('cleanerdata.csv')		
	
#rewrite filetype*





# with open('cleandata.csv', 'r') as read_object:
# 	myReader = reader(read_object)
# 	for row in myReader:
# 		#print(row)
# 		print(len(row))
# 		print(row[6])