import cv2
import mediapipe as mp
import pygame
import numpy as np
import math
import time

def format_data(array, ratio=1):
    center_x = 0
    center_y = 0
    center_z = 0

    for i in range(array.shape[0]):
        center_x += array[i,0]
        center_y += array[i,1]
        center_z += array[i,2]
            
    center_x /= array.shape[0]
    center_y /= array.shape[0]
    center_z /= array.shape[0]

    # Center hands and find furthest point from center

    max_magnitude = 0

    for i in range(array.shape[0]):
        array[i, 0] = (array[i, 0] - center_x)
        array[i, 1] = (array[i, 1] - center_y)
        array[i, 2] = (array[i, 2] - center_z)

        max_magnitude = max(max_magnitude, math.hypot(array[i, 0], array[i, 1]))

    # Normalize points according to furthest point

    for i in range(array.shape[0]):
        array[i,0] = array[i, 0] / max_magnitude
        array[i,1] = array[i, 1] / max_magnitude
        array[i,2] = array[i, 2] / max_magnitude

    return array

class HandInput:

    def __init__(self, camera=0):
        self._hand_processor = mp.solutions.hands.Hands()
        self._cap = cv2.VideoCapture(camera)
        self.falling_edge = False
        self._fire = False
    
    def process_game_input(self):
        _, image = self._cap.read()
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self._hand_processor.process(image_rgb).multi_hand_landmarks

        if (results is None or len(results) != 2):
            return None
        
        hand_a = results[0]
        hand_b = results[1]

        # mp_drawing.draw_landmarks(image, hand_a, mp_hands.HAND_CONNECTIONS)
        # mp_drawing.draw_landmarks(image, hand_b, mp_hands.HAND_CONNECTIONS)

        # cv2.imshow("display", cv2.flip(image, 1))

        fire_hand = hand_a
        move_hand = hand_b
        if (hand_a.landmark[0].y > hand_b.landmark[0].y):
            fire_hand = hand_b
            move_hand = hand_a

        ratio = image.shape[1] / image.shape[0]

        array = np.zeros((len(fire_hand.landmark), 3))

        for i in range(array.shape[0]):
            array[i,0] = fire_hand.landmark[i].x * ratio
            array[i,1] = fire_hand.landmark[i].y
            array[i,2] = fire_hand.landmark[i].z
        
        array = format_data(array)

        fire = math.hypot(array[4,0] - array[8,0], array[4, 1] - array[8, 1]) < 0.4
        move = move_hand.landmark[0].x

        if (not self._fire and fire):
            self.falling_edge = True
        else:
            self.falling_edge = False
        
        self._fire = fire

        return self.falling_edge, move
        
def main():
    player_input = HandInput()
    while True:
        print(player_input.process())
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

def main_test():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands()

    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    done = False
    while not done:
        _, image = cap.read()
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        timer = time.time()
        results = hands.process(image_rgb)
        print(time.time() - timer)

        screen.fill((0, 0, 0))

        if (results.multi_hand_landmarks and len(results.multi_hand_landmarks) > 1):

            hand_a = results.multi_hand_landmarks[0]
            mp_drawing.draw_landmarks(image, hand_a, mp_hands.HAND_CONNECTIONS)

            hand_b = results.multi_hand_landmarks[1]
            mp_drawing.draw_landmarks(image, hand_b, mp_hands.HAND_CONNECTIONS)

            hand = hand_a
            if (hand_a.landmark[0].x < hand_b.landmark[0].x):
                hand = hand_b

            ratio = image.shape[1] / image.shape[0]

            array = np.zeros((len(hand.landmark), 3))

            for i in range(array.shape[0]):
                array[i,0] = hand.landmark[i].x * ratio
                array[i,1] = hand.landmark[i].y
                array[i,2] = hand.landmark[i].z

            array = format_data(array)

            # print(math.hypot(array[4,0] - array[8,0], array[4, 1] - array[8, 1]) < 0.2)

            for i in range(array.shape[0]):
                pygame.draw.circle(screen, (0, 255, 0), (int(array[i, 0] * 100) + 250, int(array[i, 1] * 100) + 250), 4) 
        
        cv2.imshow("display", cv2.flip(image, 1))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            done = True

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_test()