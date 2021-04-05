# ScaffoldZoid

Considerations

Security Consideration

1. SQL Injection
2. Seller and Buyer are not able to access each others page
3. if you are not logged in you can't access the page by typing the url which requires login

Architecture used in designing the application is MVT that is Model View Template
The urls of the application is defined in urls.py in orange_seller directory

There are proper functions and classes for database and the backend. So, it is easy to go through the code and understand what exactly is happening

To execute the application
clone this project
then execute the following command in the terminal (both windows and unix friendly)

1. Install python and pip

2. Create a virtualenv
   virtualenv env_name

3. Activate the virtualenc
   source env_name/bin/activate

4. install django
   pip install django

5. execute the following command
   python manage.py makemigrations (if you have made any change in models.py)
   python manage.py migrate (if you have made any change in models.py)
   python manage.py runserver 0.0.0.0:8080 (here 8080 is the port in which you want your application to be executed)

Maintability

People working on the project changes time to time, different people can work on the project. So, it is important to maintain the code in such a way that they can easily understand about the current scenario and can work efficiently on the previously written code rather than writing theiry own. That is the thing which usually happens, people code as per the their comfort not as per the rules of coding and that results in the mess and it becomes hard for another person to understand the code.

Redability

After the completion of application design, it is important to document it, whether you are writing a framework or an application for user. Normal users also needs documentation sometimes to undestand the usage of the widgets you have implemented in your application.
Redability is more about writing things properly in order to make it easy for others to understand and for you too later. In most of the times the person you coded itself needs the documentaion to understand what he or she has coded at that time.

Job Market

I think from this term, we can understand that we have to first look into the market that what is the scope of market for the job we are going to do and that is most important part for an application, because we are desgining something for user. So, we should be aware of what users want. Until and unless the market study is not upto the mark, start coding is not a good idea.

Security and Upgrades

If you are connected to internet, you are unsecure and since you are delivering the product or service to the user you are more unsecure, because the hackers are always there to hack you. Security is most of the most important part you need to focus while designing an application, at least basic hacking attacks should be checked like SQL Injection, Bruteforce Attack etc. Let me give an example. You have deployed an application on your server, now you are live with a domain more precisely the IP, becuase finding an IP from the domain is not a big task nowadays. So, hacker can see the services you have installed on your system and if any service is not properly configured they will just upload the payload and will redirect your site or may be down your site or anything they want. So, before deploying server security, inbound and outboud rules, how many ports are open, if any unncessary port is open just shut it down, becuase all these things can result in the major security issue. There are a lot of things I can explain regarding the security.
Now lets talk about upgrades. Its a human nature, people like new things that's why every year new phones, cars etc are getting launched with very few changes. Back to the topic, if someone is using your application for a long duration than he or she may get bored from the same UI/UX or the functionality. So, to maintain the users attention you have to upgrade it regularly. Another important thing is that, as we are growing very fast, we are getting more and more unsecure everyday. New new technologies are introducing in the market that how to hack someone. The user's data is the most sensitive infomration you can have, if any one hack that then user will target you can sue you because their sensitive data is leaked. So, you have to stay alert in the market about hacking and cracking and have to upgrade your application on regular basis.
Let me give you an example, when facebook was just started it was very easy to get someones password, just click on the forgot password and enter your own email id and get the link to reset password, but whtn this technique became common the facebook updated itself to make it more secure.
So, upgrading the application to maintain the users attention and also to be secure is necessary.
