from django.shortcuts import render

from .models import League, Team

# Create your views here.

def index(request):
#	return render(request, 'tempSite/index.html') # main static old site, templated but with no link to the test page
	return render(request, 'tempSite/index_cp.html') # static old site with link to test page in fbj logo

def test(request):
	teams_qs = Team.objects.filter(league__active = True).select_related('league')
	leagues_qs = League.objects.filter(active = True).order_by('league_id')
	pl = []
	ch = []
	l1 = []
	l2 = []
	sp = []
	for t in teams_qs:
		if t.league == leagues_qs[0]:
			pl.append(t)
		if t.league == leagues_qs[1]:
			ch.append(t)
		if t.league == leagues_qs[2]:
			l1.append(t)
		if t.league == leagues_qs[3]:
			l2.append(t)
		if t.league == leagues_qs[4]:
			sp.append(t)
	teams = {
		'pl':pl,
		'ch':ch,
		'l1':l1,
		'l2':l2,
		'sp':sp
	}
	team_zip = zip(ch, l1, l2)
	context={
		'leagues':leagues_qs,
		'teams':teams,
		'heads':['Player', 'Team', 'Goals'],
		'team_zip':team_zip
	}
	return render(request, 'tempSite/test_page.html',context)
