from django.shortcuts import render


def homePage(request):
    return render(request, 'index.html', {'Current_Name': 'Input a player Name'})


def playerPage(request):
	print(request)
	r = str(request)
	i = r.find("player_name=")
	#print(i)
	name = r[i+12:len(r)-2].replace('+', ' ')
	print(name)
	
	return render(request, 'player.html')
