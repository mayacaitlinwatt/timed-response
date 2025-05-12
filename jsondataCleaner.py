import json
import csv
import pandas as pd

# with open ('./inputjson.json') as get_json:
# 	read_content = json.load(get_json)

with open ('./timed-response-data.json') as get_json:
	read_content = json.load(get_json)

# print(read_content['users']['g6b4b']['data'][11])
# print('')
# print('')
# print(read_content2['users']['0x9tm']['data'][11])
# print('')
# print('')



#takes stimulus data mess like '["<p><font size=\\"+3\\"><u>to wring</u></font></p>","<p><font size=\\"+3\\">wrang</font></p>"]' and returns 'wrang'
#and returns 'to wring'
def cleanStim1 (string):
	return( "to" + string.split('to')[1].split('<')[0])


#Takes a string like '["<p><font size=\\"+3\\"><u>to wring</u></font></p>","<p><font size=\\"+3\\">wrang</font></p>"]' 
#and returns 'wrang'
def cleanStim2 (string):
	return(string.split(',')[1].split('>')[2].split('<')[0])


# def getMeta (metaMess):
# 	rightDict = metaMess['rawResponses']
# 	print(rightDict)

# stranged = '''{'rt': 65734, 'preamble': '', 'superq': 'Please answer the following questions:', 'rawResponses': {'Q0': {'text': '<strong>What language do you speak most often?</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A0': 'English', 'Q1': {'text': '<strong>What language do you speak at home?</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A1': 'English', 'Q2': {'text': '<strong>What is your mother tongue? (i.e. the first language you learned at home during childhood and still understand to this day.)</strong>', 'options': ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Basque', 'Bengali', 'Bulgarian', 'Catalan', 'Cambodian', 'Chinese(Mandarin)', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Fiji', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Korean', 'Latin', 'Latvian', 'Lithuanian', 'Macedonian', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tonga', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select language'}, 'A2': 'Afrikaans', 'Q3': {'text': '<strong>What is your age?</strong>', 'options': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '28', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '75', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select age'}, 'A3': '18', 'Q4': {'text': '<strong>What is your sex?</strong>', 'options': ['Male', 'Female', 'Other'], 'allowMultipleSelections': False, 'required': True, 'placeholder': 'Select sex'}, 'A4': 'Female'}, 'responses': '{"Q0":{"text":"<strong>What language do you speak most often?</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A0":"English","Q1":{"text":"<strong>What language do you speak at home?</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A1":"English","Q2":{"text":"<strong>What is your mother tongue? (i.e. the first language you learned at home during childhood and still understand to this day.)</strong>","options":["Afrikaans","Albanian","Arabic","Armenian","Basque","Bengali","Bulgarian","Catalan","Cambodian","Chinese(Mandarin)","Croatian","Czech","Danish","Dutch","English","Estonian","Fiji","Finnish","French","Georgian","German","Greek","Gujarati","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Irish","Italian","Japanese","Javanese","Korean","Latin","Latvian","Lithuanian","Macedonian","Malay","Malayalam","Maltese","Maori","Marathi","Mongolian","Nepali","Norwegian","Persian","Polish","Portuguese","Punjabi","Quechua","Romanian","Russian","Samoan","Serbian","Slovak","Slovenian","Spanish","Swahili","Swedish","Tamil","Tatar","Telugu","Thai","Tibetan","Tonga","Turkish","Ukrainian","Urdu","Uzbek","Vietnamese","Welsh","Xhosa"],"allowMultipleSelections":false,"required":true,"placeholder":"Select language"},"A2":"Afrikaans","Q3":{"text":"<strong>What is your age?</strong>","options":["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","28","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","75","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"],"allowMultipleSelections":false,"required":true,"placeholder":"Select age"},"A3":"18","Q4":{"text":"<strong>What is your sex?</strong>","options":["Male","Female","Other"],"allowMultipleSelections":false,"required":true,"placeholder":"Select sex"},"A4":"Female"}', 'test_part': 'important', 'trial_type': 'dropdown', 'trial_index': 14, 'time_elapsed': 100611, 'internal_node_id': '0.0-5.0'} '''
# getMeta(stranged)




#loads the word into a list
listOWords = []
with open ("list_of_stimuli.txt", 'r') as common:
	for line in common:
		thisLine = line.rstrip("\n")
		thisLine = thisLine.rstrip(" ")
		listOWords.append(thisLine + ' rt')
		listOWords.append(thisLine + ' response')


#makes dictionary object from the json
dictofUsers = read_content['users']
dictOTested = []

#given an output location, writes a csv w the exp data 
def writeCsv (outFileName):
	with open(outFileName, 'a') as f:
			fieldnames = ['user' ,'what language do you speak most often?', 'what language do you speak at home?', 'what is your mother tongue?', 'what is your age?', 'what is your sex?','group']
			fieldnames = fieldnames + listOWords
			print(fieldnames)
			writer = csv.DictWriter(f, fieldnames = fieldnames)
			writer.writeheader()

			for user in read_content['users']:

				usrDict = {}

				# for word in fieldnames:
				# 	usrDict[word] = ''

				profile = dictofUsers[user]
				#print(profile)
				dataInst = json.loads(profile['data'])



				print('yipuypuyp')
				j = 0
				
				for item in dataInst:
					print(' ')
					print(user)
					#print (item)
					try:
						print(cleanStim2(dataInst[j]['stimulus']))
						
					except Exception as e:
						print(e)
				
					
					print(j)
					print('')

					j = j + 1






				print("  ")
				usrDict['user'] = user 
				usrDict['what language do you speak most often?'] = (dataInst[6]['rawResponses']['A0'])
				usrDict['what language do you speak at home?'] = (dataInst[6]['rawResponses']['A1'])
				usrDict['what is your mother tongue?'] = (dataInst[6]['rawResponses']['A2'])
				usrDict['what is your age?'] = (dataInst[6]['rawResponses']['A3'])
				usrDict['what is your sex?'] = (dataInst[6]['rawResponses']['A4'])
				usrDict['group'] = ''

				i = 17

				while i < 89 :
					try:
						#print (dataInst[i])

						atHand = cleanStim2(dataInst[i]['stimulus'])

						if (atHand + ' rt') in fieldnames:
							usrDict[atHand + ' rt'] = dataInst[i]['rt']
							print(dataInst[i]['key_press'])
							if dataInst[i]['key_press'] == 70:
								usrDict[atHand + ' response'] = 'f'
							elif dataInst[i]['key_press'] == 74:
								usrDict[atHand + ' response'] = 'j'
						else:
							usrDict[atHand + ' response'] = 'none'
							usrDict[atHand + ' rt'] = 'none'

						
					except Exception as e:
						print(e)
						pass

					i = i + 1

				try:
					print(usrDict['soze response'])
					usrDict['group'] = '1'
				except Exception as e:
					usrDict['group'] = 2
					print(e)


				# if usrDict['soze response'] == 'j' or usrDict['soze response'] == 'f':
				# 	usrDict['group'] = '1'
				# else:
				# 	usrDict['group'] = '2'

				writer.writerow(usrDict)
						


				#print(usrDict)










			# global globalCount
			
			# if globalCount is 0:
			# 	writer.writeheader()

writeCsv('cleandata.csv')












#print(listOWords)




#print(type(dictofUsers))

#print (type(dictofUsers['xytok']))

# for user in read_content['users']:
# 	profile = dictofUsers[user]
# 	#print(profile)
# 	dataInst = json.loads(profile['data'])
# 	#print(dataInst[11])
# 	print("  ")
# 	print(dataInst[11]['rawResponses']['Q0'])
# 	print(dataInst[11]['rawResponses']['Q1'])
# 	print(dataInst[11]['rawResponses']['Q2'])
# 	print(dataInst[11]['rawResponses']['Q3'])
# 	print(dataInst[11]['rawResponses']['Q4'])




# for user in read_content['users']:
# 	profile = dictofUsers[user]
# 	#print(profile)
# 	dataInst = json.loads(profile['data'])
# 	#print(dataInst[15]['stimulus'])
# 	print("  ")

# 	count = 0
# 	for row in dataInst:
# 		print(dataInst[count])
# 		print("")
# 		print(count)
# 		# try:
# 		# 	if 'to' in (dataInst[count]['stimulus']) and 'turk' not in (dataInst[count]['stimulus']): 
# 		# 		print(cleanStim2((dataInst[count]['stimulus'])))
# 		# 		#print(dataInst[count]['rt'])
# 		# 		#print(count)
# 		# 		#print('')
# 		# 	pass
# 		# except Exception as e:
# 		# 	pass
		
# 		# print(dataInst[count])
# 		# print("")
# 		count = count + 1


# # for user in read_content['users']:
# # 	profile = dictofUsers[user]
# # 	#print(profile)
# # 	dataInst = json.loads(profile['data'])
# # 	#print(dataInst[15]['stimulus'])
# # 	print("  ")

# # 	count = 0
# # 	for row in dataInst:
# # 		print(dataInst[count])
# # 		print("")
		
# # 		# print(dataInst[count])
# # 		# print("")
# # 		count = count + 1

print(len(dictOTested))
print(len(listOWords))
print(dictOTested)


# print(cleanStim2('["<p><font size=\\"+3\\"><u>to wring</u></font></p>","<p><font size=\\"+3\\">wrang</font></p>"]'))

# # print (cleanStim2('<p>Thank you for completing the practice test.</p><p>A pop-up will appear at the end of the experiment. This pop-up will contain a code you can copy-paste into Mechanical Turk. I understand that if I close the pop-up, there is no way to re-access the code. I understand that if I close the pop-up before copying the code, I will not be paid.</p>'))
