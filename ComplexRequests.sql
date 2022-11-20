SELECT iduser, count(*) AS count
FROM ratings
where grade > 5
group by iduser
having sum(grade) > 10;

select content,
	   (select title from games
	   where reviews.idgame = games.id) as game,
	   (select name from users
	   where reviews.iduser = users.id) as username
from reviews;

select Users.Name, Users.lastname, Roles.name
from users
join roles on users.idrole = roles.id;

select Users.Name, Users.lastname, ratings.grade as gamegrade
from users 
left join ratings on ratings.iduser = users.id;

select name
from users
where idrole = 1
union
select name
from users
where idrole = 2;

select * 
from users
where exists (select 1
			 from roles
			 where users.idrole = roles.id)