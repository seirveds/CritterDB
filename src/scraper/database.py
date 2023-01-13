import json
import logging
import os
import sqlite3


class CritterDatabase:

    def __init__(self, file: str):
        self.file = file

        exists = os.path.exists(file)

        # Connects to .db file if exists, otherwise makes new .db
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

        if not exists:
            logging.info(f"Passed file '{self.file}' does not exist, creating new database")
            self.init_database()

    def init_database(self):
        self.execute("""
            CREATE TABLE CRITTERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(32) NOT NULL,
                game VARCHAR(32) NOT NULL,
                type VARCHAR(16) NOT NULL,
                num TINYINT NOT NULL,
                b64_img VARCHAR NOT NULL,
                catching_quote VARCHAR(128) NOT NULL,
                months_available JSON NOT NULL,
                time_available JSON NOT NULL,
                tortimer_island BIT NOT NULL,
                location VARCHAR(32),
                selling_price SMALLINT NOT NULL,
                shadow_size VARCHAR(16),
                shadow_movement VARCHAR(16),
                spawn_requirement VARCHAR(64),
                tortimer_island_exclusive BIT
            )
        """)
        self.execute("""
            CREATE UNIQUE INDEX idx
            ON CRITTERS (name, game, type);
        """)

    def insert_row(self, infobox: dict):
        try:
            query = f"""
                INSERT OR IGNORE INTO CRITTERS (
                    name, game, type, num, b64_img, catching_quote, months_available,
                    time_available, tortimer_island, location, selling_price, shadow_size,
                    shadow_movement, spawn_requirement, tortimer_island_exclusive
                )
                VALUES (
                    '{infobox["name"].replace("'", "''")}', '{infobox["game"]}', '{infobox["type"]}',
                     {infobox["num"]}, '{infobox["b64_img"]}', '{infobox["catching_quote"].replace("'", "''")}',
                    '{json.dumps(infobox["months_available"])}', '{json.dumps(infobox["time_available"])}',
                     {infobox["tortimer_island"]}, '{infobox.get("location", None)}', {infobox["selling_price"]},
                    '{infobox.get("shadow_size", "NULL")}', '{infobox.get("shadow_movement", "NULL")}',
                    '{infobox.get("spawn_requirement", "NULL")}', {infobox.get("tortimer_island_exclusive", "NULL")}
                )
            """.replace("'NULL'", "NULL")
            self.execute(query)
        except sqlite3.OperationalError as e:
            print(query)
            raise e

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.file, check_same_thread=False)

    def execute(self, query: str):
        """Execute queries that don't return anything."""
        self.cursor.execute(query)
        self.connection.commit()

    def query(self, query: str) -> list[dict]:
        """Retrieve data from database with select query"""
        result = self.cursor.execute(query)
        column_names = [tup[0] for tup in result.description]
        return [dict(zip(column_names, row)) for row in result.fetchall()]

    def close(self):
        self.connection.close()
