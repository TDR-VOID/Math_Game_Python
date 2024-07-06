#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer, QTime
import random

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.user_name = None  # Initialize user_name attribute
        self.left_value = 0  # Initialize left_value attribute
        self.right_value = 0  # Initialize right_value attribute
        self.count = 0  # Initialize score count
        self.miss = 0  # Initialize miss count
        self.current_timer_val = 10  # Initialize timer value to 10 seconds
        self.initUI()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle_timeout)
        self.timer_value = 10  # Timer duration in seconds




    def initUI(self):
        self.setWindowTitle('Math Game')
        self.setFixedSize(600, 400)
        
        # Create layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(20)  # Set spacing between widgets
        
        # Create label for title
        title_label = QLabel('Welcome to the Game!')
        title_label.setFont(QFont('Arial', 18))
        self.layout.addWidget(title_label)
        
        # Create label for name entry
        self.name_label = QLabel('Enter your name:')
        self.layout.addWidget(self.name_label)
        
        # Create text entry box for the name
        self.name_entry = QLineEdit(self)
        self.name_entry.setPlaceholderText('Enter your name')
        self.layout.addWidget(self.name_entry)
        
        # Create login button
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.on_login_button_clicked)
        self.layout.addWidget(self.login_button)
        # Set the layout
        self.setLayout(self.layout)
        
    def on_login_button_clicked(self):
        name = self.name_entry.text()
        if name:
            self.user_name = name  # Store the user's name
            self.start_game_session()
        else:
            QMessageBox.warning(self, 'Input Error', 'Please enter your name.')
    
    def random_answers(self):
        # Generate random numbers for the answers
        first_button = random.randint(0, 1000)
        second_button = random.randint(0, 1000)
        third_button = random.randint(0, 1000)
        fourth_button = random.randint(0, 1000)
        return first_button, second_button, third_button, fourth_button
    
    def button_clicked(self):
        # Determine which button was clicked
        clicked_button = self.sender()  # This will give you the button instance that was clicked
        clicked_value = clicked_button.text()  # Get the text of the clicked button
    
        # Check if the clicked value matches the left_value or right_value
        if (clicked_value == str(self.multiply)):
            self.count += 1
            self.refresh_numbers()
            self.timer.stop()  # Stop the timer
            self.timer_value = 10  # Reset timer value
            self.start_timer()  # Start timer again

        else:
            self.miss += 1
            self.refresh_numbers()

        self.score_label.setText(f'Score: {self.count}')
        self.miss_label.setText(f'Misses: {self.miss}')

        if self.miss >= 10:
            self.game_over()
        

    def start_game_session(self):
        # Clear the existing layout
        for i in reversed(range(self.layout.count())): 
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Create a label for the game session
        game_label = QLabel('Game Session')
        game_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.layout.addWidget(game_label, alignment=Qt.AlignCenter)
        
        # Display the user's name
        name_label = QLabel(f'Player: {self.user_name}')
        name_label.setFont(QFont('Arial', 14))
        self.layout.addWidget(name_label, alignment=Qt.AlignCenter)
        
        # Create a horizontal layout for score and misses
        score_layout = QHBoxLayout()
        
        self.score_label = QLabel(f'Score: {self.count}')
        self.score_label.setFont(QFont('Arial', 12))
        score_layout.addWidget(self.score_label, alignment=Qt.AlignLeft)
        
        self.miss_label = QLabel(f'Misses: {self.miss}')
        self.miss_label.setFont(QFont('Arial', 12))
        score_layout.addWidget(self.miss_label, alignment=Qt.AlignRight)
        
        self.layout.addLayout(score_layout)
        
        # Create a horizontal layout for the random number boxes
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignCenter)
        h_layout.setSpacing(20)  # Set spacing between widgets
        
        # Create left random number box
        self.left_box = QLabel()
        self.left_box.setStyleSheet("QLabel { background-color : lightblue; padding: 10px; border: 1px solid black; }")
        self.left_box.setFont(QFont('Arial', 18))
        self.left_box.setAlignment(Qt.AlignCenter)
        self.left_box.setMinimumWidth(200)
        h_layout.addWidget(self.left_box, alignment=Qt.AlignLeft)
        
        # Create multiplication mark box
        self.mul_box = QLabel('×')
        self.mul_box.setFont(QFont('Arial', 18))
        self.mul_box.setStyleSheet("QLabel { padding: 10px; }")
        h_layout.addWidget(self.mul_box)
        
        # Create right random number box
        self.right_box = QLabel()
        self.right_box.setStyleSheet("QLabel { background-color : lightblue; padding: 10px; border: 1px solid black; }")
        self.right_box.setFont(QFont('Arial', 18))
        self.right_box.setAlignment(Qt.AlignCenter)
        self.right_box.setMinimumWidth(200)
        h_layout.addWidget(self.right_box, alignment=Qt.AlignRight)
        
        self.layout.addLayout(h_layout)
        h_layout.setSpacing(30)
        
        # Generate random numbers for the buttons
        first_button, second_button, third_button, fourth_button = self.random_answers()
        
        # Create answer buttons with random numbers
        button_layout = QVBoxLayout()
        button_layout.setSpacing(10)  # Set spacing between buttons
    
        row1_layout = QHBoxLayout()
        self.refresh_button1 = QPushButton(str(first_button))
        self.refresh_button1.setFont(QFont('Arial', 16))  # Increase button font size
        self.refresh_button1.clicked.connect(self.button_clicked)
        row1_layout.addWidget(self.refresh_button1)
        
        self.refresh_button2 = QPushButton(str(second_button))
        self.refresh_button2.setFont(QFont('Arial', 16))  # Increase button font size
        self.refresh_button2.clicked.connect(self.button_clicked)
        row1_layout.addWidget(self.refresh_button2)

        button_layout.addLayout(row1_layout)
        
        row2_layout = QHBoxLayout()
        self.refresh_button3 = QPushButton(str(third_button))
        self.refresh_button3.setFont(QFont('Arial', 16))  # Increase button font size
        self.refresh_button3.clicked.connect(self.button_clicked)
        row2_layout.addWidget(self.refresh_button3)
 
        self.refresh_button4 = QPushButton(str(fourth_button))
        self.refresh_button4.setFont(QFont('Arial', 16))  # Increase button font size
        self.refresh_button4.clicked.connect(self.button_clicked)
        row2_layout.addWidget(self.refresh_button4)
        
        button_layout.addLayout(row2_layout)

        # Add a label for current timer value
        self.timer_label = QLabel(str(self.current_timer_val))
        self.timer_label.setFont(QFont('Arial', 12))
        button_layout.addWidget(self.timer_label, alignment=Qt.AlignCenter)

        self.layout.addLayout(button_layout)
        
        # Initial random number generation
        self.refresh_numbers()
        self.start_timer()

    def start_timer(self):
        self.timer.start(1000)  # Update the timer every second
        self.timer_value = 10
        self.current_timer_val = self.timer_value
        self.timer_label.setText(str(self.current_timer_val))
        

    def handle_timeout(self):
        self.timer_value -= 1
        self.current_timer_val = self.timer_value
        self.timer_label.setText(str(self.current_timer_val))
        if self.timer_value == 0:
            self.miss += 1
            self.refresh_numbers()
            self.timer_value = 10



        self.score_label.setText(f'Score: {self.count}')
        self.miss_label.setText(f'Misses: {self.miss}')

        if self.miss >= 10:
            self.game_over()

    def refresh_numbers(self):
        # Generate new random numbers and update the boxes
        self.left_value = random.randint(0, 100)
        self.right_value = random.randint(0, 100)
        
        self.left_box.setText(str(self.left_value))
        self.right_box.setText(str(self.right_value))

        self.multiply = self.left_value * self.right_value

        # Generate new random numbers for the answer buttons
        first_button, second_button, third_button, fourth_button = self.random_answers()

        # Create a list of button values
        button_values = [first_button, second_button, third_button, fourth_button]
        # Randomly select one button to have the left_value
        answer = random.randint(0, 3)

        button_values[answer] = self.multiply

        # Update the answer buttons with new random numbers
        self.refresh_button1.setText(str(button_values[0]))
        self.refresh_button2.setText(str(button_values[1]))
        self.refresh_button3.setText(str(button_values[2]))
        self.refresh_button4.setText(str(button_values[3]))


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.clear_layout(sub_layout)


    def game_over(self):
        # Clear the existing layout
        self.timer.stop()
        self.clear_layout(self.layout)       
        
        # Display game over message
        game_over_label = QLabel('GAME OVER')
        game_over_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.layout.addWidget(game_over_label, alignment=Qt.AlignCenter)
        
        # Display the final score and misses
        self.score_board()

        # Add "Play Again" button
        play_again_button = QPushButton('Play Again')
        play_again_button.setFont(QFont('Arial', 14))
        play_again_button.clicked.connect(self.reset_game)
        self.layout.addWidget(play_again_button, alignment=Qt.AlignCenter)

    def score_board(self):
        score_layout = QVBoxLayout()
        self.score_label = QLabel(f'Score: {self.count}')
        self.score_label.setFont(QFont('Arial', 14))
        self.miss_label = QLabel(f'Misses: {self.miss}')
        self.miss_label.setFont(QFont('Arial', 14))
        score_layout.addWidget(self.score_label, alignment=Qt.AlignCenter)
        score_layout.addWidget(self.miss_label, alignment=Qt.AlignCenter)
        self.layout.addLayout(score_layout)

    def reset_game(self):
        #self.user_name = None
        self.left_value = 0
        self.right_value = 0
        self.count = 0
        self.miss = 0
        self.current_timer_val = QTime(0, 0, 0)
        self.timer.stop()  # Stop the timer
        self.clear_layout(self.layout)  # Clear the current layout
        self.start_game_session() # Reinitialize the UI to show the login screen


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

