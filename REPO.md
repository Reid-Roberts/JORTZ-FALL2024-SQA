COMP 5710 SQA - Team JORTZ - Project Report

Activities Performed:
Setting up:
  - Uploaded the project files as a repository
  - Added needed details to the repository and connected collaborators to the project on github
Software Quality Assurance Activity 1 - Git Hooks:
  - In the main directory of the Github repository insert this command, “git log –pretty=format:”%h,%an,%ad,%s > commits.csv” to automatically include git push logs
  - Added a file to the git hooks called “.pre-commit-config.yaml” and put bandit code to look at our repository and run statically check it
  - Added and edited a file called pre-commit and added code so bandit knows to check the whole repository
  - Pip install pre-commit so the file works
Software Quality Assurance Activity 2 - Fuzzing:
  - Created a method to randomly generate file names of character length 10 to fuzz with.
  - Created a method called fuzzing(name) to implement the methods getDataLoadCount, getDataLoadCountb, getDataLoadCountc, getModelLoadCounta, and getModelLoadCountb with a random file name.
  - Implemented a simpleFuzzer method to test each method implemented in fuzzing(name) 10 times.
Software Quality Assurance Activity 3 - Forensics:
  - Created logging file: MLForensics-farzana/FAME-ML/projectLogger.py
  - Added code from logging workshop to have similar formatted logging output
  - Imported projectLogger into lint_engine.py for access to the logging file and creation of logging objects in the chosen methods
  - Modified file to create logging objects of the projectLogger class
    getDataLoadCount()
    getDataLoadCountb()
    getDataLoadCountc()
    getModelLoadCounta()
    getModelLoadCountb()
  - Added logging methods to track initiation and completion time and value of the counting process in each of the above methods to be outputted to the PROJECT-LOGGER.log file
  - Software Quality Assurance Activity 4 - Continuous Integration:
  - Consulted Codacy continuous integration sequence
  - Added the following file to the .github folder: .github/workflows/codacy-analysis.yaml
      - This is done to add the “Codacy Analysis For Project” action to the Actions tab in the repository that then logs and analyzes the commits made to the repository

Lessons Learned:
  1.We became more familiar with the github interface and learned how to interact with a github repository from our machines and through the github.com user interface.
  2. When implementing git hooks, we learned how to create files in a github that are able to be used and connected with bandit to automatically run static checks for commits into a github repository. 
  3. When implementing git hooks, we also learned valuable skills that will make coding, especially on a team, easier and more streamline to test code statically in a way that can be traced, which can be used for personal and professional work.
  4. When implementing fuzzing, we learned that we could generate random inputs to fuzz in a way that tests the code and reveals weaknesses and or bugs.
  5. When implementing fuzzing, we also learned how to simplify implementing fuzzing on multiple methods at once.
  6. When implementing logging, we learned more about the value of logging the manipulation of or collection of data.
  7. When implementing logging, we also learned more about what kind of things should be logged when deciding what functions to add logging to strategically.
  8. When implementing continuous integration (CI), we learned the value of automated code reviews and why it is important to have them available as needed.
  9. When implementing CI, we also learned how to make use of github actions to make the development proccess and quality assurance process alongside each other quicker and more efficient.
