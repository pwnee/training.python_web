Hi Cris,

I made the mistake of not looking at the repo before I started down the path I took.  I also didn't that there were instructions and I started work against what I thought we had to do for homework.  I spent the majority of today trying to get the blog part up and running and now I'm hitting a point where I'm going to submit what I have and hopefully learn about better ways to get data into your database.  I've been struggling with trying to create the proper way to get the POST set up so a user can submit a blog post.  It's been frustrating because I feel like I know exactly what needs to be done (get POST parameters from HTML, send the POST, set the post entries in the BlogPost class I have and then save the blogpost).  I have not been able to get that working because, from what I can tell, I haven't got the CSRF verification configured properly when I post.  I get this error:

CSRF verification failed. Request aborted.
Help
Reason given for failure:
    CSRF token missing or incorrect.
    
In general, this can occur when there is a genuine Cross Site Request Forgery, or when Django's CSRF mechanism has not been used correctly. For POST forms, you need to ensure:
Your browser is accepting cookies.
The view function uses RequestContext for the template, instead of Context.
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
You're seeing the help section of this page because you have DEBUG = True in your Django settings file. Change that to False, and only the initial error message will be displayed.
You can customize this page using the CSRF_FAILURE_VIEW setting.

Do you have any tips on getting past this?  
I've verified that browser is accepting cookies, so I'm guessing it has to do with making sure the view function uses RequestContext for the template?  