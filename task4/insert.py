from create import session, Actor, Movie
import datetime


if __name__ == '__main__':
    actor1 = Actor(name="Leonardo DiCaprio")
    actor2 = Actor(name="Tom Hanks")
    actor3 = Actor(name="Brad Pitt")
    actor4 = Actor(name="Kate Winslet")

    movie1 = Movie(
        title="Titanic",
        year=1997,
        rating=7.9,
        actors=[actor1, actor4]
    )

    movie2 = Movie(
        title="Inception",
        year=2010,
        rating=8.8,
        actors=[actor1]
    )

    movie3 = Movie(
        title="Catch Me If You Can",
        year=2002,
        rating=8.1,
        actors=[actor1, actor2]
    )

    movie4 = Movie(
        title="Forrest Gump",
        year=1994,
        rating=8.8,
        actors=[actor2]
    )

    movie5 = Movie(
        title="Once Upon a Time in Hollywood",
        year=2019,
        rating=7.6,
        actors=[actor1, actor3]
    )

    session.add_all([
        movie1, movie2, movie3, movie4, movie5
    ])

    session.commit()