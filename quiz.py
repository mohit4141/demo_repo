


#initialize pygame screen
import pygame
pygame.init()

# define colours
RED      = ( 255,   0,   0)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (  73, 204,   6)
CHARCOAL = (  87,  87,  87)

pygame.mixer.music.load("main_theme.wav")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
# pygame.mixer.music.play()


def load_quizList(datafilename):
    """
    Access the data file and loads the contents into a list called qList[] in the following format:
    [[q1,a1,image1,optA,optB, optC, optD],[q2,a2,image1,optA,optB, optC, optD],...,[qN,aN,imageN,optA,optB, optC, optD]]

    This function operates under the assumption that the file that is being read (specified by the datafilename parameter)
    is of the format:

    10
    question1
    answer1
    imagefilename1
    question1 optionA
    question1 optionB
    question1 optionC
    question1 optionD
    question2
    answer2
    imagefilename2
    question2 optionA
    question2 optionB
    question2 optionC
    question2 optionD
    ...
    questionN
    answerN
    imagefilenameN
    questionN optionA
    questionN optionB
    questionN optionC
    questionN optionD

    The first line of the file (in this example 10) is the number of questions represented in the file.  All questions
    have 4 options (a,b,c,d)


    :param datafilename: string
    the filename of the file to load

    :return: qList[]
    """
    questions = open("data.txt","r")

    newlist = []

    for line in questions:
        line = line.strip() #remove \n
        newlist.append(line) #add new line to new list

    qlist = []

    initial_index = 1 #mark down where to start slicing
    final_index = 8 #mark down where to end slicing

    for i in range (3):
        qlist.append(newlist[initial_index:final_index]) #put list into list
        initial_index = initial_index + 7 #update initial index for next run
        final_index = final_index + 7 #update final index for next run

    questions.close()

    return qlist


def play_game(screen, game_data, results_list):
    """
    The playable quiz. For each question in game_data,
    presents each question to the screen, gets the response from the user, shows result, and goes next question

    :param screen: pygame screen object
    :param game_data: list object containing quiz data
    :return:
        game_state values - "results" or "quit": string
        score: int - the final total score of the user
        results_list: a list containing the results of each question, each element in the list is a three element list
        consisting of [correctAnswerLetter, playerAnswerLetter, pointsInt] i.e [['a','a',1],['d','b',0], ... ['a'False,'c',0]]

    """

    done = False
    clock = pygame.time.Clock()
    question_index = 0
    advance_question = False
    response = ""
    score = 0
    score_update = 0
    question_state = 0

    while done == False:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                return "quit",score
                # done = True # Flag that we are done so we exit this loop

            elif event.type == pygame.KEYUP:
                if event.key != pygame.K_RETURN:
                    response = chr(event.key)
                elif response != "":
                    if game_data[question_index][1].lower() == response.lower():
                        score_update = 1
                    advance_question = True


        if advance_question == True:
            # update the score and reset things for the next question
            score = score + score_update
            question_index = question_index + 1
            response = ""
            advance_question = False
            score_update = 0

        elif advance_question != True:
            show_question_response(screen,game_data[question_index],response)

        if question_index >= len(game_data):
            done = True

        clock.tick(20) #limit to 20 frames per second
        pygame.display.flip() #update screen with what's drawn
    else:
        return "final",score


def show_question_response(screen, q_data, user_response):
    """
    Shows the text for the question, options and user response to the screen

    :param screen: pygame screen object to display to
    :param q_data: list containing the info for the question to
    show in format [question_text,answer,imagefile, optionA, optionB,optionC, optionD]
    :param user_response: string -
    :return: None
    """

    # your code here
    background = pygame.image.load('background1.jpg').convert()
    screen.blit(background,[0,0])

    # load image
    image = pygame.image.load(q_data[2]).convert()
    screen.blit(image, [25,25])

    large_font = pygame.font.SysFont('Calibri',17,False,False)
    normal_font = pygame.font.SysFont('Calibri', 15, False, False)

    # load questions
    text_question = large_font.render(q_data[0],True,BLACK)
    text_option_a = normal_font.render(q_data[3],True,BLACK)
    text_option_b = normal_font.render(q_data[4],True,BLACK)
    text_option_c = normal_font.render(q_data[5],True,BLACK)
    text_option_d = normal_font.render(q_data[6],True,BLACK)
    text_answer_here = normal_font.render("Your answer here:",True,BLACK)

    text_user_response = normal_font.render(user_response,True,BLACK)

    # blit questions to screen
    screen.blit(text_question,[20,330])
    screen.blit(text_option_a,[20,350])
    screen.blit(text_option_b,[20,370])
    screen.blit(text_option_c,[20,390])
    screen.blit(text_option_d,[20,410])
    screen.blit(text_answer_here,[20,439])
    screen.blit(text_user_response,[130,439])


def show_final_results(screen, score, out_of):
    """
   Shows the final score to the screen (with out of). i.e You're final score is 18/20
   Shows a final statement based on score i.e "Great Job", "Study Harder", "Nice Try"

    :param screen: pygame screen object to display to
    :param score: int - final user score
    :param out_of: int - number of questions

    :return: string: game_state values - "play"or "quit"
    """

    done = False
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('Calibri',30,False,False)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the function
                return "quit"

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return "quit"

        background = pygame.image.load('background1.jpg').convert()
        screen.blit(background,[0,0])

        # victory_sound = pygame.mixer.Sound("Your_team_won.wav")
        # failed_sound = pygame.mixer.Sound("Your_team_lost.wav")

        if score > 1:
            text_pass = font.render("Congratulations!!! You passed!!!",True,BLACK)
            screen.blit(text_pass,[0,0])
            # victory_sound.play()

        elif score <= 1:
            text_fail = font.render("You failed!!! Study harder!!!",True,BLACK)
            screen.blit(text_fail,[0,0])
            # failed_sound.play()

        statement = "Your score is: "+ str(score)+ " out of "+ str(out_of)

        final_text = font.render(statement,True,BLACK)
        screen.blit(final_text,[0,40])

        clock.tick(20)
        pygame.display.flip()


def main():
    """
    The top function to control the overall game

    :return: None
    """

    # load data into quizList
    quizList = load_quizList("data.txt")
    size = [700, 500]
    results = []

    pyscreen = pygame.display.set_mode(size)
    pygame.display.set_caption("RBS Induction Demo Quiz")

    # initialize the game state
    game_state = "start"

    while game_state != "quit":

        if game_state == "start":
            game_state, score = play_game(pyscreen,quizList,results)

        elif game_state == "final":
            game_state = show_final_results(pyscreen, score,len(quizList))


    pygame.quit()


main()