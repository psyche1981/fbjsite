from django.shortcuts import render

# Create your views here.

def index(request):
#	return render(request, 'tempSite/index.html') # main static old site, templated but with no link to the test page
	return render(request, 'tempSite/index_cp.html') # static old site with link to test page in fbj logo

def test(request):
	return render(request, 'tempSite/test_page.html')
