# C++ Projects

This repository contains two beginner-friendly C++ projects:

1. **Login and Registration System**  
2. **Rock Paper Scissors Game**

Both projects use basic C++ concepts such as input/output streams, file handling, structures, and control statements.

---

## 1. Login and Registration System

### Project Goal
A simple login system where users can register and login using a username and password. User credentials are stored in files to simulate a simple database.

### Technologies Used
- C++ programming language  
- Input/Output Streams (`<iostream>`)  
- File Handling (`<fstream>`)  
- Strings (`<string>`)  
- Structures (`struct User`)  

### Features
- **User Registration**
  - Enter a username and password
  - Validate that username is unique
  - Password validation (e.g., minimum length)
  - Store credentials in a file (`username.txt`) or a common database file
- **User Login**
  - Enter username and password
  - Verify credentials from stored files
  - Grant or deny access
- Persistent storage (data remains after program exit)
- Optional: simple password hashing for security

### Program Flow
1. Display menu:
   - Register
   - Login
   - Exit
2. Registration process:
- Ask for username
- Validate uniqueness
- Ask for password
- Store credentials in file
3. Login process:
- Ask for username and password
- Verify credentials
- Grant or deny access
4. Exit program

### Input Validation
- Username: unique, no spaces, not empty  
- Password: minimum length (e.g., 6 characters), not empty  

### Testing Checklist
- Register a new user → file created  
- Try registering existing username → blocked  
- Login with correct credentials → success  
- Login with wrong credentials → failure  
- Program persists data after restart  

---

## 2. Rock Paper Scissors Game

### Project Goal
A two-player game (user vs computer) where each player chooses Rock, Paper, or Scissors. The winner is decided according to standard rules:

- Rock vs Scissors → Rock wins  
- Rock vs Paper → Paper wins  
- Paper vs Scissors → Scissors wins  

### Technologies Used
- C++ programming language  
- Input/Output Streams (`<iostream>`)  
- Standard Library Functions (`<cstdlib>`, `<ctime>`)  

### Features
- User selects choice: Rock, Paper, or Scissors  
- Computer randomly selects choice  
- Compare choices to determine winner  
- Display both choices and result  
- Optional: keep score and allow replay  

### Program Flow
1. Display menu:
   - Play
   - Exit
2. User selects choice  
3. Computer generates random choice  
4. Display choices using readable names  
5. Determine winner:
- If equal → Draw
- Else, apply rules to determine winner
6. Ask user if they want to play again  

### Suggested Functions
```cpp
  int getUserChoice();
  int getComputerChoice();
  void showChoices(int user, int computer);
  void determineWinner(int user, int computer);
```
