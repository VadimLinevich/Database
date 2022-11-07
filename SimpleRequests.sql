select * from users
order by name;

select * from games
limit 2 offset 1;

select * from ratings
where grade between 5 and 7;

select * from games
where title like 'Deus ex%';

select * from roles
where name in ('user');

insert into users(idrole, name, lastname, password, email)
values
(2, 'Hank', 'Anderson', 'dumbpasswordRK800', 'Hank@gmail.com');

update users
set email = 'Anderson@gmail.com'
where lastname = 'Anderson';

delete from users
where name = 'Hank';

select avg(grade) from ratings
where idgame = 1;