# Database code for the DB Forum, full solution!
import psycopg2


def get_posts():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("""select  articles.title,
        count(*) from articles inner join log on
        articles.slug = split_part(path, '/article/', 2)
        group by articles.title order by count
        desc limit 3""")
        posts = c.fetchall()
        db.close()
        return posts
    except Exception as e:
        raise


def popular_authoer():
    """Return all posts from the 'database', most recent first."""
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("""select authors.name, count(*)
        from articles inner join authors
         on articles.author = authors.id inner join log
         on articles.slug = split_part(log.path, '/article/', 2)
         group by authors.name order by count desc;""")
        posts = c.fetchall()
        db.close()
        return posts
    except Exception as e:
        print("This is an error message!")


def request_error():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select sub.time::timestamp::date, CAST(sub.failed AS float)
    / (CAST(sub.sucess AS float)+CAST(sub.failed AS float)) * 100 as final
    from (SELECT time::timestamp::date, COUNT(*) as length,
    SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END) as failed,
    SUM(CASE WHEN status != '404 NOT FOUND' THEN 1 ELSE 0 END) as sucess
    FROM log  GROUP BY time::timestamp::date ORDER BY length DESC
    ) as sub where CAST(sub.failed AS float)
    / (CAST(sub.sucess AS float)+CAST(sub.failed AS float)) * 100  >=2;""")
    posts = c.fetchall()
    db.close()
    return posts
