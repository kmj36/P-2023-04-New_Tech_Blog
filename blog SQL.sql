/*CREATE TABLE IF NOT EXISTS Users (
	userid		char(20) 		PRIMARY KEY,
	password	char(64)		NOT NULL,
	nickname	varchar(255)	UNIQUE NOT NULL,
	usernum		SERIAL 			NOT NULL,
	createdate	timestamp with time zone NOT NULL,
	lastlogin	timestamp with time zone,
	isalive		boolean			NOT NULL,
	CONSTRAINT	chk_userid CHECK (CHAR_LENGTH(userid) >= 4)
);*/

/*CREATE TABLE IF NOT EXISTS Posts (
	postid		SERIAL			PRIMARY KEY,
	userid		char(20)		NOT NULL,
	tagid		INTEGER,
	title		varchar(255)	NOT NULL,
	content		text,
	createdate	timestamp with time zone NOT NULL,
	ispublic	boolean			NOT NULL,
	isserect	boolean			NOT NULL,
	password	char(64),
	CONSTRAINT	fk_userid FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);*/

/*CREATE TABLE IF NOT EXISTS tags (
	tagid		SERIAL			PRIMARY KEY,
	tagname		varchar(255)	NOT NULL
);*/

/*CREATE TABLE IF NOT EXISTS comments (
	commentid INTEGER PRIMARY KEY,
	postid SERIAL NOT NULL,
	userid char(20) NOT NULL,
	comment text,
	createdate timestamp with time zone NOT NULL,
	isserect boolean NOT NULL,
	password char(64),
	CONSTRAINT	fk_postid FOREIGN KEY(postid) REFERENCES Posts(postid) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT	fk_userid FOREIGN KEY(userid) REFERENCES Users(userid) ON DELETE CASCADE ON UPDATE CASCADE
);*/

--DROP TABLE tags;
--SELECT * FROM users;
--SHOW TIMEZONE;

-- SELECT encode(digest('assdf', 'sha256'), 'hex');

/*INSERT INTO Users VALUES
(
	'admin',
	encode(digest('Wpo@0406*0013-', 'sha256'), 'hex'),
	'관리자',
	DEFAULT,
	now(),
	NULL,
	true
);*/


/*INSERT INTO Users VALUES
(
	'test',
	encode(digest('1234', 'sha256'), 'hex'),
	'테스트계정',
	DEFAULT,
	now(),
	NULL,
	true
);*/