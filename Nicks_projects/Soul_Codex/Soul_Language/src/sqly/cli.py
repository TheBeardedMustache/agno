import argparse

from . import parse
from .lowering import lower
from ..ntru import generate_keypair


from typing import Sequence


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Process SQLy query files")
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="path to text file containing the query",
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="query string (if --file is not used)",
    )
    parser.add_argument(
        "--show-frames",
        action="store_true",
        help="print lowered frame encodings",
    )
    args = parser.parse_args(argv)

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            query_text = f.read()
    elif args.query:
        query_text = args.query
    else:
        parser.error("must specify QUERY or --file")

    ast = parse(query_text)
    print(ast)

    if args.show_frames:
        frames = lower(ast, "intent", generate_keypair())
        for frame in frames:
            print(frame.encode())


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
