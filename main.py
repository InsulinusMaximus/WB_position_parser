import parser
import config


if __name__ == '__main__':

    parser = parser.Parser_WB()
    parser.run(config.topyky_jenskye_urls, config.query_topyky_jenskye)

    for data in parser.result:
        print(data)

