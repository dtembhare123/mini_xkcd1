import argparse
from random import randrange
from typing import List


def rand_range(start: int = 1, stop: int = 83, limit: int = 15) -> List[int]:
    """
    Args:
       start (int):first numeric values of the range
       stop (int):last numeric values of the range
       limit(int):number of results to yield
    Returns:
       list(int):random values range(start:stop)with count limited
         to 'limit'
   """
    result = [randrange(start, stop + 1) for i in range(limit)]
    return result


if __name__ == "__main__":
    example = """example:
        python task_one.py --max 87  --any 15
   """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )
    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunk of resources to be fetched"
    )
    #breakpoint()
    args = parser.parse_args()
    print(args.any)
    print(args.max)

    comic_number_set = rand_range(1, args.max, args.any)
