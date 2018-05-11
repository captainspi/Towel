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