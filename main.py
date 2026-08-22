import time

from sqlalchemy import text
from load_data import engine, load_data
from process_data import process_data
from recommendation import get_recommendation

def get_last_event_id():

    query = text("""
        SELECT COALESCE(MAX(event_id), 0)
        FROM public.event
    """)

    with engine.connect() as connection:
        return connection.execute(query).scalar()

# public.table_name -> to make sure accessing the public table
def get_latest_event(last_event_id):

    query = text("""
        SELECT event_id, user_id
        FROM public.event
        WHERE event_id > :last_event_id
        ORDER BY event_id
        LIMIT 1
    """)

    with engine.connect() as connection:
        result = connection.execute( query, {"last_event_id": last_event_id} )

        row = result.fetchone()
        # looks like:
        """
        ROW(
            event_id = 15,
            user_id=7
        )
        """
        if row is None:
            return None

        return row


def generate_recommendations(user_id):

    data = load_data()
    data = process_data(data)

    return get_recommendation(
        data,
        user_id,
        num=20
    )

def save_recommendations(recommendations):

    if not recommendations:
        return

    query = text("""
        INSERT INTO public."Recommendations" (user_id, receipt_id, seen)
        VALUES (:user_id, :receipt_id, :seen)
    """)

    with engine.begin() as connection:
        for recommendation in recommendations:
            connection.execute(query, recommendation)


def listen_for_events():

    last_event_id = get_last_event_id()

    # print("New event")

    while True:

        event = get_latest_event(last_event_id)

        if event is not None:

            event_id = event.event_id
            user_id = event.user_id

            # print( f"New event: {event_id} "
                # f"for user {user_id}"
            # ) 

            recommendations = generate_recommendations(user_id)

            save_recommendations(recommendations)

            # print(
                # f"Inserted {len(recommendations)} "
                # f"recommendations for user {user_id}"
            # )

            last_event_id = event_id

        time.sleep(2)


if __name__ == "__main__":
    listen_for_events()