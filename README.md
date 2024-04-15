# Django
This repository includes a Django tutorial on how to create a Django environment and how to create a superuser in it.

# What you need to do.?
1. you should install
     ```py
     pip install django
2. after that type command to run server (which will redirect you to the main Django page) and click localhost destination link:
     ```py
     python manage.py runserver
     
     
![image](https://github.com/DonKravche/django-test/assets/138400870/6f77ee07-9d1d-4cc4-b73f-4b5cde059c85)
![image](https://github.com/DonKravche/django-test/assets/138400870/dccc17e9-6652-4039-8047-3883fcfcd7c0)

3. type in search bar (/admin after localhost address) to move Administering Django page
     ```
     http://127.0.0.1:8000/admin/login/?next=/admin/

4. Before you enter the users in the fields, you must run the migrations to create the basic Jago database.
     ```py
     python manage.py migrate

5. To Create super user write:
     ```py
     python manage.py createsuperuser
     
6. Follow the instructions

7. now you are ready to write created user to the Administering Django page and log in <3
     ![image](https://github.com/DonKravche/django-test/assets/138400870/e00afa62-409a-40dd-8d08-f67fa41a3471)
     
8. Congratulations You made it !
  ![image](https://github.com/DonKravche/django-test/assets/138400870/9ac3de9b-f6e2-4ff6-96e2-ebff650bdb80)

9. Fell Free to test and use my code !


# New Version 1.0.1
## Whats new?
*** Changed Main Page Visula From Django Default page to 404 not found***

also improved code:

1. we added Market app to our project and you can create and add books into database,
![image](https://github.com/DonKravche/django-testV2/assets/138400870/1544bddd-b5cd-42d7-8c5a-7c5991f57ac5)

2. also now you can check db items as json!
![image](https://github.com/DonKravche/django-testV2/assets/138400870/bdf299b4-d609-4207-97da-2c7eeb5be56e)

3. you also can filter items by id like that in url:
   
![image](https://github.com/DonKravche/django-testV2/assets/138400870/75136a24-a4a2-4c87-98d8-5cafc48b275c)


# new Version 1.0.2
## Whats new?

1. fixed few issues from previous version
2. added sort function in market app (now you can filter items using: id, name, price, author name, pages, img)
3. *** Changed Main Page Visula From Django Default page to 404 not found*** remains same when you run django
4.  added new html to display books (per page 3)
5.  when you click book name, you will redirected to book main page
   ![image](https://github.com/DonKravche/django-ultimate-v3/assets/138400870/e4113db3-e2e1-477d-b1fa-147877ab3d05)

   ![image](https://github.com/DonKravche/django-ultimate-v3/assets/138400870/cf973386-781a-45b9-b4ef-dab96778e28f)

6.  added next & previous pages for better user experience


Feel free to use my code!
GL HF <3
