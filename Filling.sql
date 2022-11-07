insert into Roles(name)
values
('admin'),
('user');

insert into Users(idrole, name, lastname, password, email)
values
(1, 'Vadim', 'Linevich', '123456789', 'vad@gmail.com'),
(2, 'Vlad', 'Linevich', '1234', 'vlad@gmail.com'),
(2, 'Adam', 'Jensen', 'deus25', 'adam@gmail.com');

insert into Games(title, poster, description, year, platform, agerating, mode, systemrequirements)
values
('Deus ex', 'link', 'GOTY 2000', '2000-06-23', 'Windows, Xbox', '18+', 'single-player', 'Video Card: Geforce2, Free Disk Space: 150MB'),
('Deus ex: Invisible War', 'link', 'Deus ex sequel', '2003-12-02', 'Windows, Xbox', '18+', 'single-player', 'Video Card: Geforce3, Free Disk Space: 2GB'),
('Detroit: Become Human', 'link', 'Adventure video hame', '2018-05-25', 'Windows, Playstation 4', '18+', 'single-player', 'Video Card: Geforce GTX 1060, Free Disk Space: 55GB');

insert into Reviews(idgame, content, visitor)
values
(1, 'One of the greatest game of all time', 3),
(1, 'Legendary game and legendary series', 1),
(2, 'Mediocre sequel', 1),
(3, 'Amazing story + Connor', 3),
(3, 'Love this game', 2);

insert into Ratings(idgame, visitor, grade)
values
(1, 1, 10),
(2, 1, 6),
(3, 3, 9);

insert into Genres(name)
values
('Immersive sim'),
('adventure'),
('action-RPG');

insert into GameGenre(idgame, idgenre)
values
(1,1),
(1,3),
(2,1),
(2,3),
(3,2);

insert into Companies(name, foundation, location)
values
('Ion Storm', '1996-11-15', 'Austin, Texas'),
('Eidos Interactive', '1984-12-11', 'Southwork, London'),
('Quantic Dream', '1997-05-02', 'Paris, France');

insert into GameCompany(idgame, idcompany)
values
(1,1),
(1,2),
(2,1),
(2,2),
(3,3);

insert into Developers(name, age, image)
values
('Warren Spector', 67, 'link'),
('Harvey Smith', 55, 'link'),
('Daniel Cage', 53, 'link');

insert into GameDeveloper(idgame, iddeveloper)
values
(1,1),
(1,2),
(2,1),
(2,2),
(3,3);