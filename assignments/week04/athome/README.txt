Here is the URL to hit the WSGI book information server:

http://block647040-vrs.blueboxgrid.com:8080/

There are also two servers in the week04/athome folder.  The first one (book_wsgi_server.py) was a first cut at the assignment before I really took a look at it.  It was a rough working copy, but it didn't have any error handling, and it isn't nearly as elegant as the example provided in the blogpost.  The second one is that one that is running on my VM and it is probably superior considering the error handling and general readability.  I do have a few comments that I'll list below.

I ran into issues trying to server up images using PIL and the code I have in the original server I created (book_wsgi_server.py).  I couldn't figure out a good way to get PIL on my VM via virtualenv.  Googling around showed that there are issues with PIL and virtualenv.  I'm bummed I couldn't get that up and running live, but I didn't want to contaminate the VM w/PIL... 

Also, one thought I had when setting up the image serving--do you have any suggestions on caching the image?  If I were to serve it up via WSGI, it doesn't scale very well because with each request to either page, it had to return the image.  Ideally it would cache after the first request to the index and then it wouldn't kill the server with each subsequent request.  I understand that this isn't a hot webapp that's going to get slammed with traffic, just wondering what others might do if they wanted to cache and use WSGI to serve their content.  Middleware?