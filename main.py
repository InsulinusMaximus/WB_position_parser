import parser
import config
from repo import Repository

if __name__ == '__main__':

    parser = parser.Parser_WB()

    # Velo

    parser.run(config.velo_urls, config.query_velo)
    parser.run(config.sport_velo_urls, config.query_sport_velo)
    parser.run(config.chernie_velo_jenskie_urls, config.query_chernie_velo_jenskie)
    parser.run(config.velo_jenskie_urls, config.query_velo_jenskie)

    # Top

    # parser.run(config.beliy_top_urls, config.query_beliy_top)
    # parser.run(config.top_chernyy_urls, config.query_top_chernyy)
    # parser.run(config.topyky_jenskye_urls, config.query_topyky_jenskye)

    parser.run(config.top_sportyvniy_urls, config.query_top_sportyvniy)

    parser.run(config.zhenskiy_top_iz_hlopka_urls, config.query_zhenskiy_top_iz_hlopka)
    parser.run(config.zhenskiy_top_belyy_iz_hlopka_urls, config.query_top_zhenskiy_belyy_iz_khlopka)

    # Bruky

    # parser.run(config.shtany_urls, config.query_shtany)
    # parser.run(config.bruky_jenskye_letnye_urls, config.query_bruky_jenskye_letnye)
    # parser.run(config.bruky_urls, config.query_bruky)
    parser.run(config.ykorochenie_bruky_urls, config.query_bruky_ykorochenie)
    parser.run(config.bryuki_zhenskiye_bezhevyye_urls, config.query_bryuki_zhenskiye_bezhevyye)

    # Futbolka

    # parser.run(config.futbolka_zhenskaya_belaya_s_printom_urls, config.query_futbolka_zhenskaya_belaya_s_printom)
    parser.run(config.ukorochennaya_zhenskaya_futbolka_iz_khlopkaurls,
               config.query_ukorochennaya_zhenskaya_futbolka_iz_khlopka)
    # parser.run(config.futbolka_zhenskaya_urls,
    #            config.query_futbolka_zhenskaya)

    # Pizhamy

    # parser.run(config.pizhamy_zhenskiye_s_shortami_urls, config.query_pizhamy_zhenskiye_s_shortami)
    # parser.run(config.pizhama_zhenskaya_s_shortami_urls, config.query_pizhama_zhenskaya_s_shortami)
    # parser.run(config.pizhama_zhenskaya_s_shortami_golubaya_urls, config.query_pizhama_zhenskaya_s_shortami_golubaya)

    # Sorochky

    # Tolstovky

    # parser.run(config.tolstovka_zhenskaya_bez_kapyushona_urls, config.query_tolstovka_zhenskaya_bez_kapyushona)
    parser.run(config.khudi_zhenskoye_oversayz_sirenevoye_urls, config.query_khudi_zhenskoye_oversayz_sirenevoye)
    parser.run(config.tolstovka_zhenskaya_s_kapyushonom_rozovaya_urls,
               config.query_tolstovka_zhenskaya_s_kapyushonom_rozovaya)

    repo = Repository(parser.result)
    repo.run()

    for data in parser.result:
        print(data)

