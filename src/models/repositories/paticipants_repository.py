from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipansRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participants(self, participants_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO pariticipants
                (id, trip_id emails_to_invite, name)
                VALUES
                    (?, ?, ?, ?)
            ''',(
                participants_infos["id"],
                participants_infos["trip_id"],
                participants_infos["emails_to_invite_id"],
                participants_infos["name"]
            )
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.mail
                FROM participants AS p
                JOIN emails_to_invite AS e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, panticipant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE
                    id = ?
            ''', (panticipant_id)
        )
        self.__conn.commit()