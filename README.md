# Towel

#### A towel is just about the most massively useful thing any interstellar Hitchhiker can carry. A software for converting money is the second best thing.

### Launching the App
* Clone the app from the github repo:
 * ```
   URL to repo: https://github.com/captainspi/Towel

   ```
 * Launch in a dockerized environment
    ```
    docker run -it --rm -v "{pathToDirectory}/Towel":"/usr/src/app" omaransari1/towel-app:1.0.1 /bin/bash -c "PYTHONPATH=./ python3 src/Main.py --filename=sample_logs"
   ```
 
 * Add your own input file
   * Please copy your input file to ./assets/logs
   * Don't forget to pass the --filename when you execute the program :)
 

### Running the unittests
  ```
  docker run -it --rm -v "{pathToDirectory}/Towel":"/usr/src/app" omaransari1/towel-app:1.0.1 /bin/bash -c "python3 -m unittest discover" 
  ```
### Generating codecoverage
  ```
  docker run -it --rm -v "{pathToDirectory}/Towel":"/usr/src/app" omaransari1/towel-app:1.0.1 /bin/bash -c "python3 -m coverage html --rcfile=tests/unit/coverage.ini" 
  ```
  
### Dev Notes

#### Limitations
* Bank cannot convert money for a transaction (which could be composed of multiple currencies)
* Lack of interfaces in python makes me uncomfortable. Ideally I would have multiple interfaces per package. Can achieve the same affect with abstract class
hack but no
* Lack of value/domain objects for a nicer 'contract'. Ideally I would spend some time to refactor the tokenizer and have each unique token type be represented by its own class or something to that effect. Just lists and dictionaries with unknown unknown types makes me a bit uncomfortable.
* App class is not covered by unit tests.
* Factory class is not covered by unit tests.
* View class is not covered by unit tests.
* No logger.
* Lack of DI container forces me to inject NumeralsFactory into App

#### Assumptions
* Tokenizer is very vigorous in terms of what it expects from sentences
  * Declaration of Numeral Map Format (case insensitive): A is B (example: glod is V)
  * Declaration of Currency (case sensitive): {numeral}+ {Currency1} is {value} {Currency2} (example:glob glob Silver is 34 Credits)
  * Question to evaluate Value (case sensitive): how much is {numeral}+ ?
  * Question to convert Money (case sensitive): how many {Currency} is {numeral}+ {Currency2} ? 