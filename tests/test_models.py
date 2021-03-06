# -*- coding: utf-8 -*-
import datetime
from arrow import arrow

tzutc = arrow.dateutil_tz.tzutc


def test_user():
    from annict.models import User
    json = {
        "id": 2,
        "username": "shimbaco",
        "name": "Koji Shimba",
        "description": "",
        "url": None,
        "records_count": 1234,
        "created_at": "2016-05-03T19:06:59.929Z"
    }
    user = User.parse(None, json)
    assert user.id == 2
    assert user.created_at == datetime.datetime(2016, 5, 3, 19, 6, 59, 929000, tzinfo=tzutc())


def test_work():
    json = {
        'episodes_count': 21,
        'id': 4636,
        'media': 'tv',
        'media_text': 'TV',
        'official_site_url': 'http://re-zero-anime.jp/',
        'released_on': '2016-04-03',
        'released_on_about': '',
        'season_name': '2016-spring',
        'season_name_text': '2016年春',
        'title': 'Re:ゼロから始める異世界生活',
        'title_kana': 'りぜろからはじめるいせかいせいかつ',
        'twitter_hashtag': 'rezero',
        'twitter_username': 'Rezero_official',
        'watchers_count': 970,
        'wikipedia_url': ('https://ja.wikipedia.org/wiki/Re:%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5'
                          '%A7%8B%E3%82%81%E3%82%8B%E7%95%B0%E4%B8%96%E7%95%8C%E7%94%9F%E6%B4%BB'),
    }
    from annict.models import Work

    work = Work.parse('dummy_api', json)

    assert work.id == 4636
    assert work.title == 'Re:ゼロから始める異世界生活'
    assert work.released_on == datetime.date(2016, 4, 3)


def test_episode():
    json = {
        "id": 45,
        "number": None,
        "number_text": "第2話",
        "sort_number": 2,
        "title": "殺戮の夢幻迷宮",
        "records_count": 0,
        "work": {
            "id": 3831,
            "title": "NEWドリームハンター麗夢",
            "title_kana": "",
            "media": "ova",
            "media_text": "OVA",
            "season_name": "1990-autumn",
            "season_name_text": "1990年秋",
            "released_on": "1990-12-16",
            "released_on_about": "",
            "official_site_url": "",
            "wikipedia_url": "",
            "twitter_username": "",
            "twitter_hashtag": "",
            "episodes_count": 2,
            "watchers_count": 10
        },
        "prev_episode": {
            "id": 44,
            "number": None,
            "number_text": "第1話",
            "sort_number": 1,
            "title": " 夢の騎士達",
            "records_count": 0
        },
        "next_episode": None
    }
    from annict.models import Episode

    episode = Episode.parse(None, json)

    assert episode.id == 45
    assert episode.work.id == 3831
    assert episode.prev_episode.id == 44
    assert episode.next_episode is None


def test_record():
    json = {
        "id": 425551,
        "comment": "ゆるふわ田舎アニメかと思ったらギャグと下ネタが多めのコメディアニメだった。これはこれで。日岡さんの声良いなあ。",
        "rating": 4,
        "is_modified": False,
        "likes_count": 0,
        "comments_count": 0,
        "created_at": "2016-04-11T14:19:13.974Z",
        "user": {
            "id": 2,
            "username": "shimbaco",
            "name": "Koji Shimba",
            "description": "アニメ好きが高じてこのサービスを作りました。聖地巡礼を年に数回しています。",
            "url": "http://shimba.co",
            "records_count": 1906,
            "created_at": "2014-03-02T15:38:40.000Z"
        },
        "work": {
            "id": 4670,
            "title": "くまみこ",
            "title_kana": "くまみこ",
            "media": "tv",
            "media_text": "TV",
            "season_name": "2016-spring",
            "season_name_text": "2016年春",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://kmmk.tv/",
            "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%81%8F%E3%81%BE%E3%81%BF%E3%81%93",
            "twitter_username": "kmmk_anime",
            "twitter_hashtag": "kumamiko",
            "episodes_count": 6,
            "watchers_count": 609
        },
        "episode": {
            "id": 74669,
            "number": "1",
            "number_text": "第壱話",
            "sort_number": 10,
            "title": "クマと少女 お別れの時",
            "records_count": 183
        }
    }

    from annict.models import Record

    record = Record.parse(None, json)

    assert record.id == 425551
    assert record.user.id == 2
    assert record.work.id == 4670
    assert record.episode.id == 74669
    assert record.created_at == datetime.datetime(2016, 4, 11, 14, 19, 13, 974000, tzinfo=tzutc())


def test_program():
    json = {
        "id": 35387,
        "started_at": "2016-05-07T20:10:00.000Z",
        "is_rebroadcast": False,
        "channel": {
            "id": 4,
            "name": "日本テレビ"
        },
        "work": {
            "id": 4681,
            "title": "ふらいんぐうぃっち",
            "title_kana": "ふらいんぐうぃっち",
            "media": "tv",
            "media_text": "TV",
            "season_name": "2016-spring",
            "season_name_text": "2016年春",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://www.flyingwitch.jp/",
            "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%81%B5%E3%82%89%E3%81%84%E3%82%93%E3%81%90%E3%81%86%E3%81%83%E3%81%A3%E3%81%A1",
            "twitter_username": "flying_tv",
            "twitter_hashtag": "flyingwitch",
            "episodes_count": 5,
            "watchers_count": 695
        },
        "episode": {
            "id": 75187,
            "number": "5",
            "number_text": "第5話",
            "sort_number": 50,
            "title": "使い魔の活用法",
            "records_count": 0
        }
    }

    from annict.models import Program

    program = Program.parse(None, json)

    assert program.id == 35387
    assert program.started_at == datetime.datetime(2016, 5, 7, 20, 10, 0, 0, tzinfo=tzutc())
    assert program.channel['id'] == 4
    assert program.work.id == 4681
    assert program.episode.id == 75187
