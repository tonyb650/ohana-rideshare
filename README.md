# Ohana Rideshare

<a id="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tonyb650/ohana-rideshare">
    <img src="flask_app/static/car_cartoon.png" alt="" width="120">
  </a>

  <h3 align="center">Ohana Rideshare</h3>

  <p align="center">
    A platform for riders and drivers to connect for help with transportation.  
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A simple platform for riders and drivers to connect and message each other about upcoming rides.
* Any user can request a ride
* Any user can 'pick up' a ride (commit to driving)
* Riders and drivers can add messages to a given ride, sharing updates or other information 
* Drivers can cancel their commitment
* Riders can delete rides

<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Built With

[![Flask][Flask]][Flask-url]\
[![Jinja][Jinja]][Jinja-url]\
[![Mysql][Mysql.com]][Mysql-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

**NOTE**: *This project is not complete and served strictly as a learning project.*\
To get a local copy up and running follow these steps.

### Prerequisites

Python and Pip are required. Visit `https://www.python.org/downloads/`

### Installation

**NOTE:** _This was a learning project and not in any way a finished, secure or stable application._

1. Clone the repo
   ```sh
   git clone https://github.com/tonyb650/ohana-rideshare.git
   ```
2. Navigate to project
   ```sh
   cd ohana-rideshare
   ```
3. Install virtual environment
   ```sh
   py -m venv .venv      # windows
   python3 -m venv .venv # mac / linux
   ```
4. Activate virtual environment
   ```sh
   source .venv/Scripts/activate # windows
   source .venv/bin/activate     # mac / linux
   ```
5. Install requirements
   ```sh
    pip install -r requirements.txt
   ```
6. Create database with MySQL Workbench
- Launch MySQL Workbench
- Go to `File` > `Open Model...` and select the `ohana_rideshare_erd.mwb` file located in `sql_files`
- Go to `Database` > `Forward Engineer...`
- Follow the wizard to generate and execute the SQL script
7. Update the values for 'user' and 'password' in `flask_app/config/mysqlconnection.py` for your local database.
8. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```
9. Start the application.
    ```sh
    python server.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Requesting a Ride
![Request Ride Animation][request-ride-animation]
### Pick Up a Ride
![Pick Up Ride Animation][pick-up-ride-animation]
### Register and Login
![Login Screen Shot][login-screenshot]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

This was a learning project only and there will be no further development.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tony Brierly

[![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [Ohana Rideshare](https://github.com/tonyb650/ohana-rideshare.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best Readme Template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[request-ride-animation]: flask_app/static/request_a_ride.gif
[pick-up-ride-animation]: flask_app/static/pick_up_a_ride.gif

[login-screenshot]: flask_app/static/ohana_login.png

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tony-brierly

[Flask]: https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=61DAFB
[Flask-url]: https://flask.palletsprojects.com/

[Jinja]: https://img.shields.io/badge/jinja-041f30?style=for-the-badge&logo=jinja&logoColor=00bcff
[Jinja-url]: https://jinja.palletsprojects.com/

[Mysql.com]: https://img.shields.io/badge/mysql-000000?style=for-the-badge&logo=mysql&logoColor=white
[Mysql-url]: https://mysql.com/