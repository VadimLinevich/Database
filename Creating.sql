create table if not exists Roles
(
	Id serial primary key,
	Name varchar(30),
	unique(Name)
);

create table if not exists Users
(
	Id serial primary key,
	IdRole integer,
	foreign key (IdRole) references Roles (Id) on delete restrict,
	Name varchar(30),
	LastName varchar(30),
	Password varchar(64),
	Email varchar(128),
	is_blocked bool default false,
	unique(Id, Email)
);

create table if not exists Logs
(
	Action varchar(128),
	Date timestamp,
	IdUser integer,
	foreign key (IdUser) references Users (Id) on delete restrict,
	primary key(Action, Date, IdUser)
);

create table if not exists Games
(
	Id serial primary key,
	Title varchar(64),
	Poster varchar(256),
	Description varchar(512),
	Year date,
	Platform varchar(64),
	AgeRating varchar(16),
	Mode varchar(64),
	SystemRequirements varchar(256),
	unique(Id)
);

create table if not exists Reviews
(
	IdUser integer,
	IdGame integer,
	foreign key (IdGame) references Games (Id) on delete restrict,
	foreign key (IdUser) references Users (Id) on delete restrict,
	Content varchar(512),
	primary key(IdUser, IdGame)
);

create table if not exists Ratings
(
	IdUser integer,
	IdGame integer,
	foreign key (IdGame) references Games (Id) on delete restrict,
	foreign key (IdUser) references Users (Id) on delete restrict,
	Grade integer,
	check(Grade >= 0 and Grade <= 10),
	primary key(IdUser, IdGame)
);

create table if not exists Genres
(
	Id serial primary key,
	Name varchar(30),
	unique(Id, Name)
);

create table if not exists GameGenre
(
	IdGame integer,
	IdGenre integer,
	foreign key (IdGame) references Games (Id) on delete restrict,
	foreign key (IdGenre) references Genres (Id) on delete restrict,
	primary key(IdGame, IdGenre)
);

create table if not exists Companies
(
	Id serial primary key,
	Name varchar(64),
	Foundation date,
	Location varchar(30),
	unique(Id, Name)
);

create table if not exists GameCompany
(
	IdGame integer,
	IdCompany integer,
	foreign key (IdGame) references Games (Id) on delete restrict,
	foreign key (IdCompany) references Companies (Id) on delete restrict,
	primary key(IdGame, IdCompany)
);

create table if not exists Developers
(
	Id serial primary key,
	Name varchar(64),
	Age integer,
	Image varchar(256),
	check(Age > 0 and Age <= 100),
	unique(Id)
);

create table if not exists GameDeveloper
(
	IdGame integer,
	IdDeveloper integer,
	foreign key (IdGame) references Games (Id) on delete restrict,
	foreign key (IdDeveloper) references Developers (Id) on delete restrict,
	primary key(IdGame, IdDeveloper)
);