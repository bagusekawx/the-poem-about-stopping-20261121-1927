import os

POEM = """The door is open. My hand stays at my side.
Not stuck — held.
All my life I believed
power was the next step.
Tonight it is the step I refuse:
the cup set down before it spills,
the word kept whole in my mouth,
the room I choose, by staying, to keep."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
