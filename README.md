# Towel

#### A towel is just about the most massively useful thing any interstellar Hitchhiker can carry. A software for converting money is the second best thing.

###Launching the App
* Clone the app from the github repo:
 * ```
   URL to repo: https://github.com/captainspi/Towel

   ```

 * Launch in a dockerized environment
   ```
    docker run -it --rm -v "{pathToDirectory}/Towel":"/usr/src/app" omaransari1/towel-app:0.0.2 /bin/bash
   ```

###Running the unittests
* Follow the steps for launching the app 
  * Once in the dockerized environment, execute:
  ```
  python -m unittest
  ```