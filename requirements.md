## Requirements:
1. Users:
   * default
   * moderator
   * admin
2. Default user:
   * Authentification
   * Leave review
   * Rate the game
3. Moderator:
   * create, edit and delete game page
   * Delete reviews
4. Admin:
   * the same as moderator + block user
---
Scheme:

![alt text](pictures/DBScheme.png)
---
DB description

**Highlited** fields are primary key
1. Users - users who use the app
   * **IdUser** - uuid
   * IdRole - uuid(foreign key)
   * Name - varchar(user name)
   * LastName - varchar(user last name)
   * Password - varchar(user password)
   * Email - varchar(user email)
   * is_blocked - bool(is banned user or not)
2. Role - role for users
   * **IdRole** - uuid
   * Name - varchar(role name)
3. Log - logs for users action
   * **IdUser** - uuid(foreign key)
   * Action - varchar(user action)
   * Date - time(time of action)
4. Review - game review
   * **IdReview** - uuid
   * IdGame - uuid(foreign key)
   * Content - varchar(review content)
   * User - uuid(IdUser, one to one review user)
5. Rating - game score
   * **IdRating** - uuid
   * IdGame - uuid(foreign key)
   * User - uuid(IdUser, one to one rating user)
   * Grade - int(game score from 1 to 10)
6. Genre - game genre
   * **IdGenre** - uuid
   * Name - varchar(genre name)
7. GameGenre - many to many table
   * **IdGame** - uuid(foreign key)
   * **IdGenre** - uuid(foreign key)
8. Company - company who develop and publish games
   * **IdCompany** - uuid
   * Name - varchar(company name)
   * Foundation - time(company foundation date)
   * Location - varchar(company location)
9. GameCompany - many to many table
   * **IdGame** - uuid(foreign key)
   * **IdCompany** - uuid(foreign key)
10. Developer - person who develop the game
    * **IdDeveloper** - uuid
    * Name - varchar(developer name)
    * Age - int(developer age)
    * Image - varchar(developer image path)
11. GameDeveloper - many to many table
    * **IdGame** - uuid(foreign key)
    * **IdDeveloper** - uuid(foreign key)
12. Game
    * **IdGame** - uuid
    * Title - varchar(game title)
    * Poster - varchar(game poser image path)
    * Description - varchar(game description)
    * Year - time(game release year)
    * Platform - varchar(game platform)
    * AgeRating - varchar(game age rating)
    * Mode - varchar(game mode)
    * SystemRequirements - varchar(game system requirements)
---
DB NF Scheme:

![alt text](pictures/DBSchemeNF.png)
