-- Parameters:

-- Zsoli's requests:
-- no rock, maximize energy and danceability

-- Noah's requests:
-- no country, keep all Jazz, keep all indie music, prefer songs no longer than 4 minutes


create table combined_music as
select * from noahs_music
union
select * from zsolis_music;

-- let's go through and capture all of the songs that we WANT to keep based on the requirements, then append those at the end 
create table temp_music_table as 
(select * from combined_music where 1=2);

-- insert jazz music
insert into temp_music_table
select * from combined_music 
where genre like '%jazz%';

-- insert movie sountracks
insert into temp_music_table
select * from combined_music 
where genre like '%theme%' or genre like '%soundtrack%';

select * from temp_music_table;

-- now lets trim down based on what we both don't want


-- delete songs according to zsoli's requests
delete from combined_music where genre like '%rock%';
delete from combined_music where energy <= 0.5;
delete from combined_music where danceability <= 0.5;

-- delete songs according to noah's requests:
delete from combined_music where genre like '%country%';
delete from combined_music where duration_ms >= 240000;

-- now add back in the songs with conditions we wanted to keep
insert into combined_music
select * from temp_music_table;


select distinct * from combined_music;
