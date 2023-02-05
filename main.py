import sqlalchemy as db
from config import save_data, engine, Advertisement
from parser import search_ads, get_soup, get_ads, get_last_page


def main():
    if not db.inspect(engine).has_table('advertisement'):
        Advertisement.__table__.create(bind=engine, checkfirst=True)

    ads = []
    page = 1
    while True:
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        html = search_ads(url)
        soup = get_soup(html)
        data = get_ads(soup)
        ads.extend(data)
        page += 1
        if get_last_page(soup) is None:
            break
    save_data(ads)


if __name__ == '__main__':
    main()

