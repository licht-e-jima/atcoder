from app.app import App
from app.repository.memory.memory import MemoryRepository


def main(lines):
    app = setup()
    m = int(lines[0])  # number of restaulants
    for r in lines[1:m+1]:
        app.create_restaurant(r)

    for o in lines[m+1:]:
        app.query(o)

    app.do_all_remain_query()

def setup() -> App:
    repo = MemoryRepository()
    return App(repo)

if __name__ == '__main__':
    lines = [
        "1",
        "iVehD 100 0",
        "2020-03-04 10:30 set_available Bob 50 0",
        "2020-03-04 10:32 order iVehD 5000 140 0",
        "2020-03-04 10:34 set_available Bob 50 0",
        "2020-03-04 10:37 order iVehD 5000 160 0",
    ]
    main(lines)
