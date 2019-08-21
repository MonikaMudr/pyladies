from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
import click


db = create_engine("sqlite:///ukoly.sqlite")
Base = declarative_base()


class Ukol(Base):
    # Název tabulky v databází.
    __tablename__ = "ukoly"

    # Číselný identifikátor úkolu, toto číslo bude jedinečné.
    id = Column(Integer, primary_key=True)
    # Text úkolu.
    text = Column(String)
    # Datum a čas zadání úkolu.
    zadano = Column(DateTime)
    # Datum a čas vyřešení úkolu. Prázdná hodnota znamená nehotový úkol.
    vyreseno = Column(DateTime)

    def __repr__(self):
        return f"<Ukol(text='{self.text}', zadano={self.zadano}, vyreseno={self.vyreseno})>"


def pripoj_se():
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    return Session()


@click.group()
def ukolnik():
    pass


@ukolnik.command()
@click.option("--jen_nehotove", default=False, is_flag=True)
@click.option("--od_nejnovejsiho", default=False, is_flag=True)
def vypis(jen_nehotove, od_nejnovejsiho):
    sezeni = pripoj_se()
    dotaz = sezeni.query(Ukol)

    if jen_nehotove:
        dotaz = dotaz.filter(Ukol.vyreseno == None)

    ukoly = dotaz.all()

    if od_nejnovejsiho:
        ukoly = dotaz.order_by(Ukol.zadano.desc())
    for ukol in ukoly:
        symbol = "[x]" if ukol.vyreseno else "[ ]"
        print(f"{symbol} {ukol.id}. {ukol.text}")


@ukolnik.command()
@click.option("--novy_ukol", prompt="Novy ukol")
def pridej(novy_ukol):
    sezeni = pripoj_se()
    ukol = Ukol(text=novy_ukol, zadano=datetime.now())
    sezeni.add(ukol)
    sezeni.commit()
    print(f"OK: {novy_ukol}")


@ukolnik.command()
@click.argument("id_ukolu", type=click.INT)
def vyreseno(id_ukolu):
    sezeni = pripoj_se()
    dotaz = sezeni.query(Ukol)
    try:
        ukol = dotaz.filter_by(id=id_ukolu).one()
    except NoResultFound:
        print('Zvolene cislo neodpovida zadnemu ukolu')
    else:
        ukol.vyreseno = datetime.now()
        sezeni.add(ukol)
        sezeni.commit()
        print('{} {}. {}'.format("[x]", ukol.id, ukol.text))


@ukolnik.command()
@click.option("--id_ukol", type=click.INT)
@click.option("--jen_hotove", default=False, is_flag=True)
def smaz(id_ukol, jen_hotove):
    sezeni = pripoj_se()
    dotaz = sezeni.query(Ukol)
    if jen_hotove:
        dotaz.filter(Ukol.vyreseno != None).delete()
    else:
        try:
            ukol = dotaz.filter_by(id=id_ukol).one()
        except NoResultFound:
            print('Zvolene cislo neodpovida zadnemu ukolu')
        else:
            dotaz.filter_by(id=id_ukol).delete()
            print('Ukol c.{}({}) smazan'.format(ukol.id, ukol.text))
    sezeni.commit()



if __name__ == '__main__':
    ukolnik()

