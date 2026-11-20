from create import session, Actor, Movie
from sqlalchemy import select, func, desc


if __name__ == '__main__':
    stmt = select(Actor).order_by(Actor.name)

    for actor in session.scalars(stmt):
        print(actor.name, actor.movies)

    print('* ' * 20)
    
    stmt = select(Movie).order_by(Movie.title)

    for movie in session.scalars(stmt):
        print(movie, movie.actors)

    print('* ' * 20)
    
    stmt = select(Movie, Actor).select_from(Movie).join(Actor.movies)

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)

    stmt = (
        select(Actor, func.avg(Movie.rating).label('avg_rating'), func.max(Movie.year))
        .select_from(Actor)
        .join(Movie.actors)
        .group_by(Actor.id)
        .order_by(desc('avg_rating'))
        # .limit(3)
    )

    for tpl in session.execute(stmt):
        print(tpl)

    print('* ' * 20)




    