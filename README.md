
<p align="center">
  <br /><img
    width="600"
    src="logo.png"
    alt="Rem - Clipboard Sharing Service"
  />
</p>

***
![Build - Dev](https://github.com/RangerDigital/rem/workflows/Build%20-%20Dev/badge.svg?branch=dev)
![Build - Production](https://github.com/RangerDigital/rem/workflows/Build%20-%20Production/badge.svg?branch=master)
![Deploy - Frontend](https://github.com/RangerDigital/rem/workflows/Deploy%20-%20Frontend/badge.svg?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Source of **Rem**, simple clipboard sharing service build with **Flask** and **Vue.js** used to share snippets of code between my colleagues during university labs.

> 🎉 Check it out live at [rem.bednarski.dev](https://rem.bednarski.dev/)!

<br>

## 📦 Why build another Pastebin service?

Aside from learning experience, Using Rem has some advantages over other methods of sharing text:

-   **Number Only Codes**

Because of the temporality of shares only numbers are used for identifying them, which means It's easier to share them with people sitting next to you.

-   **No Login Required**

Using Rem doesn't require you to login unlike using a Facebook on which you have to do it on somebody's else computer.

<br>

## 🛠 Technology Stack

#### Backend
The servers side of Rem consists of the **Redis** database with a simple dockerized **Flask** app. **PyTest** with **Docker Compose** is used for basic functional testing on the GitHub Actions platform.

Metrics are gathered using self-hosted **TIG** stack and exceptions monitoring is handled by managed **Sentry** instance.

Rem is currently deployed on (Arm/Amd64) **Docker Swarm** cluster.

#### Frontend
As for the client-side, **Vue.js** with **Axios** is used for the logic of the **CSS Grid** heavy interface. **Sentry** is also used for monitoring exceptions.

<br>

## 🚧 Contributing

**You are more than welcome to help me improve Rem!**

Just fork this project from the `master` branch and submit a Pull Request (PR) to the `dev` branch.
If you are modifying backend you should also run `pytest` functional tests inside `backend/tests` directory.

<br>

## 📃 License
This project is licensed under [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) .
