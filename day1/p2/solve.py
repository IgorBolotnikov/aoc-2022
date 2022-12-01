import os.path

INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solve(s: list[str]) -> int:
    res = [0]
    for line in s:
        stripped = line.strip()
        if stripped:
            res[-1] += int(stripped)
        else:
            res.append(0)
    return sum(sorted(res, key=lambda x: -x)[:3])


TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
TEST_EXPECTED = 45000


def test() -> None:
    assert solve(TEST_INPUT.split('\n')) == TEST_EXPECTED


def main() -> int:
    with open(INPUT) as file:
        print(solve(file.readlines()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
