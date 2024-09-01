MIN_BALLS, MAX_BALLS = 27, 127


class BallClock:
    """
    A class to represent a Ball Clock. It allows to simulate
    the movement of the balls by minute. It has some methods
    to facilitate the implementation of the 2 modes required.
    """

    def __init__(self, number_of_balls: int) -> None:
        if not MIN_BALLS < number_of_balls < MAX_BALLS:
            ball_range = f"{MIN_BALLS} and {MAX_BALLS} balls"
            raise ValueError(f"Clock must have between {ball_range}")
        self._n = number_of_balls
        self.initial_state = list(range(1, self._n + 1))
        self.reset()

    def reset(self) -> None:
        self.queue = self.initial_state.copy()
        self.minutes = []
        self.fives = []
        self.hours = []
        self.cycles = 0

    def step(self) -> None:
        self.minutes.append(self.queue.pop(0))
        if len(self.minutes) == 5:
            self.fives.append(self.minutes.pop(-1))
            self.queue = self.queue + self.minutes[::-1]
            self.minutes = []
        if len(self.fives) == 12:
            self.hours.append(self.fives.pop(-1))
            self.queue = self.queue + self.fives[::-1]
            self.fives = []
        if len(self.hours) == 12:
            last = self.hours.pop(-1)
            self.queue = self.queue + self.hours[::-1] + [last]
            self.hours = []
            self.cycles += 1

    def match_initial_state(self) -> bool:
        return self.cycles != 0 and self.queue == self.initial_state

    def get_state(self) -> dict[str, list[int]]:
        return {
            "Min": self.minutes,
            "FiveMin": self.fives,
            "Hour": self.hours,
            "Main": self.queue,
        }


def clock_mode1(number_of_balls: int) -> BallClock:
    """
    First mode of the Ball Clock. It simulates the movement
    of the balls until they return to their initial state,
    displaying the number of days (24hrs) it took to do so.
    """
    clock = BallClock(number_of_balls)
    while not clock.match_initial_state():
        clock.step()
    days = round(clock.cycles / 2, 0)
    print(f"{number_of_balls} balls cycle after {days} days.")
    return clock


def clock_mode2(number_of_balls: int, minutes: int) -> BallClock:
    """
    Second mode of the Ball Clock. It simulates the movement
    of the balls for a given number of minutes, displaying
    the state of the clock at the end of the simulation.
    """
    clock = BallClock(number_of_balls)
    for _ in range(minutes):
        clock.step()
    print(clock.get_state())
    return clock
