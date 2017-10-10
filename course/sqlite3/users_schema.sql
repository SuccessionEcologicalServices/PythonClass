# https://github.com/SuccessionEcologicalServices/PythonClass/blob/master/course/sqlite3.md

CREATE TABLE IF NOT EXISTS "users" (
	"pKey" INTEGER PRIMARY KEY,
	"username" varchar(255) DEFAULT NULL,
	"age" INT DEFAULT NULL,
	"first_name" varchar(255) DEFAULT NULL,
	"last_name" varchar(255) DEFAULT NULL,
	"fav_color" varchar(255) DEFAULT NULL
);