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
   * Name - text(user name)
   * LastName - text(user last name)
   * Password - text(user password)
   * Email - text(user email)
   * is_blocked - bool(is banned user or not)
2. Role - role for users
   * **IdRole** - uuid
   * Name - text(role name)
3. Log - logs for users action
   * **IdUser** - uuid(foreign key)
   * Action - text(user action)
   * Date - time(time of action)
4. Review - game review
   * **IdReview** - uuid
   * IdGame - uuid(foreign key)
   * Content - text(review content)
   * User - uuid(IdUser, one to one review user)
5. Rating - game score
   * **IdRating** - uuid
   * IdGame - uuid(foreign key)
   * User - uuid(IdUser, one to one rating user)
   * Grade - int(game score from 1 to 10)
6. Genre - game genre
   * **IdGenre** - uuid
   * Name - text(genre name)
7. GameGenre - many to many table
   * **IdGame** - uuid(foreign key)
   * **IdGenre** - uuid(foreign key)
8. Company - company who develop and publish games
   * **IdCompany** - uuid
   * Name - text(company name)
   * Foundation - time(company foundation date)
   * Location - text(company location)
9. GameCompany - many to many table
   * **IdGame** - uuid(foreign key)
   * **IdCompany** - uuid(foreign key)
10. Developer - person who develop the game
    * **IdDeveloper** - uuid
    * Name - text(developer name)
    * Age - int(developer age)
    * Image - text(developer image path)
11. GameDeveloper - many to many table
    * **IdGame** - uuid(foreign key)
    * **IdDeveloper** - uuid(foreign key)
12. Game
    * **IdGame** - uuid
    * Title - text(game title)
    * Poster - text(game poser image path)
    * Description - text(game description)
    * Year - time(game release year)
    * Platform - text(game platform)
    * AgeRating - text(game age rating)
    * Mode - text(game mode)
    * SystemRequirements - text(game system requirements)
---
DB NF Scheme:

![alt text](pictures/DBSchemeNF.png)
