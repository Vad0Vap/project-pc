import argparse
from parser import YouTubeParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    yt = YouTubeParser(args.url)
    data = yt.get_video_info()

    print(data)

    if args.output:
        YouTubeParser.save_to_json(data, args.output)


if __name__ == "__main__":
    main()
