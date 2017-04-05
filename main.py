import random

def main():
    # 0: rock
    # 1: paper
    # 2: scissors
    previous_rounds = [0, 1, 2]

    def determine_winner(human_choice, computer_choice):
        if outcome == 0:
            print 'It\'s a draw'
        elif outcome == 1:
            print 'It\'s a win'
            choices = [human_choice, computer_choice]
            winning_choice = set(filter(lambda x: x not in choices, previous_rounds)).pop()
            previous_rounds.append(winning_choice)
        else:
            print 'It\'s a loss'
            previous_rounds.append(computer_choice)

    while True:
        print previous_rounds
        human_choice = int(raw_input('Make your choice: '))
        computer_choice = random.choice(previous_rounds)
        print 'You chose ' + str(human_choice)

        outcome = (human_choice - computer_choice) % 3
        determine_winner(human_choice, computer_choice)


if __name__ == '__main__':
    main()
