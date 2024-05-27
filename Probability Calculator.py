import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.items = list(kwargs.items())

        contents = []
        for item in self.items:
            for count in range(1, item[1] + 1):
                contents.append(item[0])

        self.contents = contents

    def draw(self, num_ball_draw):
        removed_ball = []

        if num_ball_draw == 0:
            return removed_ball

        elif len(self.contents) <= num_ball_draw:
            all_items = copy.deepcopy(self.contents)
            # random.shuffle(all_items)
            self.contents.clear()
            return all_items

        else:
            for count in range(1, num_ball_draw + 1):
                removed_ball.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
            return removed_ball

    def renew_contents(self):
        contents = []
        for item in self.items:
            for count in range(1, item[1] + 1):
                contents.append(item[0])

        self.contents = contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_contents = copy.deepcopy(hat.contents)
    expected_balls_list = list(expected_balls.items())
    expected_balls_total_num = 0
    case_happen = 0

    if len(hat_contents) == 0:
        return 'Hat should always be created with at least one ball.'

    if num_experiments <= 0:
        return 0

    if num_balls_drawn <= 0:
        return 0

    for ball_tuple in expected_balls_list:
        if ball_tuple[1] <= 0:
            return 0
        else:
            try:
                hat_contents.index(ball_tuple[0])
            except ValueError:
                return 0

            if ball_tuple[1] > hat_contents.count(ball_tuple[0]):
                return 0
            else:
                expected_balls_total_num += ball_tuple[1]

    if expected_balls_total_num > num_balls_drawn:
        return 0

    else:
        for exper in range(1, num_experiments + 1):
            drawn_ball_set = hat.draw(num_balls_drawn)
            check_criteria = []

            for ball_tuple in expected_balls_list:
                if drawn_ball_set.count(ball_tuple[0]) >= ball_tuple[1]:
                    check_criteria.append(True)
                else:
                    check_criteria.append(False)

            if all(check_criteria):
                case_happen += 1
            else:
                case_happen += 0

            hat.renew_contents()

    return round(case_happen / num_experiments, 3)
