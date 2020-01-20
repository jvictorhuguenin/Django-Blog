from django.shortcuts import render

posts=[
	{'author':'alex',
	'date':'12/2/2020',
	'content':'first post',
	'title':'Brazil'
	},
	{'author':'marie',
	'date':'12/3/2020',
	'content':'second post',
	'title':'fuck you'
	}
]


def home(request):
	context={
		'posts':posts
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})