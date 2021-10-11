create database test;
use test;

drop table tmp;

CREATE TABLE tmp(
	ti tinyint(4),
	i int(11),
	d DATE,
	dt DATETIME NOT NULL,
	ts TIMESTAMP NOT NULL,
);

INSERT INTO tmp (d,dt)
VALUES
	( '2021-12-30', '2021-11-30 12:00:00');


INSERT INTO tmp VALUES
	(1,2,NULL, now(),now());

DELETE FROM tmp
	WHERE tmp.ts="2021-10-11 19:24:06";

UPDATE tmp SET ti=1,i=200000
	WHERE ts='2021-10-11 19:24:30';