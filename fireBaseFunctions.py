from firebase import firebase

firebase = firebase.FirebaseApplication('https://artoverflow.firebaseio.com/', None)


def postQuestion(title, description, upvotes, user, soundcloudLink):
	newQuestion = {'title': title,
				'description': description,
				'upvotes': upvotes,
				'user': user,
				'soundcloudLink': soundcloudLink,
				}
	result = firebase.post('/questions', newQuestion)
	return result


def getQuestions():
	result = firebase.get('/questions', None)
	for key in result:
		result[key]['soundcloudLink'] = "http://vocaroo.com/player.swf?playMediaID=" + (result[key]['soundcloudLink'])[21:] + "&autoplay=0"
	return result
	# return list(result.values())