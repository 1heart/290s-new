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
	return result
	# return list(result.values())