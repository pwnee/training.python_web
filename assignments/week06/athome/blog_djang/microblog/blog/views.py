# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Context, loader
from blog.models import BlogPost
#from django.template import RequestContext
#from blog.models import ContactForm
#from django.core.context_processor import csrf
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

def blog_index(request):
	latest_blog_posts = BlogPost.objects.order_by('pub_date')	
	template = loader.get_template('C:\cygwin\home\wtb\\blog_djang\microblog\\blog\\templates\\blog.html')
	output = ', ' .join(b.title for b in latest_blog_posts)
	context = Context({
		'latest_blog_posts': latest_blog_posts,
		})
	return HttpResponse(template.render(context))
	
'''def add_entry(request):
	if request.method = 'POST':
		data = BlogPost(request.POST)
	entry = BlogPost(title = "asdf", post = "f2fw", pub_date = timezone.now, user = user)
	entry.save()

def detail(request, entry_id):
	requested_entry = BlogPost.objects.filter(id=entry_id)
	template = loader.get_template('C:\cygwin\home\wtb\\blog_djang\microblog\\blog\\templates\\entry.html')
	 utput = ', ' .join(b.title for b in )
	return HttpResponse("Blog Post Title %s." % requested_entry.[0]title)'''
@csrf_protect
def add_entry(request):
	print "wtf:", request

	if request.method == 'POST': # If the form has been submitted...
	    form = ContactForm(request.POST) # A form bound to the POST data
	    if form.is_valid(): # All validation rules pass
	        # Process the data in form.cleaned_data
	        # ...
	        return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
	    form = ContactForm() # An unbound form

	return render_to_response('contact.html', {
	    'form': form,},context_instance = RequestContext(request) )

	#
