# T.I.M.

## Touchless Interactive Manager

<p align="center">

[![react](https://img.shields.io/badge/react-frontend-61DAFB.svg?style=for-the-badge&logo=react)](https://docker.com)
[![python](https://img.shields.io/badge/Python-backend-3776AB.svg?style=for-the-badge&logo=python)](https://docker.com)
[![flutter](https://img.shields.io/badge/Flutter-mobile-02569B.svg?style=for-the-badge&logo=flutter)](https://docker.com)
[![js](https://img.shields.io/badge/javaScript-backend-F7DF1E.svg?style=for-the-badge&logo=javaScript)](https://docker.com)
[![mongoDB](https://img.shields.io/badge/mongodb-database-47A248.svg?style=for-the-badge&logo=mongodb)](https://docker.com)
[![SQLite](https://img.shields.io/badge/SQLite-database-003B57.svg?style=for-the-badge&logo=SQLite)](https://docker.com)
[![docker](https://img.shields.io/badge/Docker-containers-2496ED.svg?style=for-the-badge&logo=docker)](https://docker.com)

</p>

![alt text](FrontEnd/src/assets/branding/logo/Touchless_Interactive_Manager_Letters_plus_logo_C.png)

<p align='center'>
              <a href="https://skillicons.dev">
                <img src="https://skillicons.dev/icons?i=py,js,ts,dart,flutter,react,nextjs,mongodb,firebase,sass,docker,express,flask,tensorflow,opencv" />
              </a>
            </p>

T.I.M. (Touchless Interactive Manager), is a web-based dynamic tool that uses CV2 library for computer vision and ML to create face recognition, and hand interpreter for interactive porpuses, mainly focuses on preventing users from touching no interface in order to accomplish certain health protocols, this version of TIM is the Assistance Manager with mobile Token Auth. Originally designed to work with a raspberrypi as an IoT device, it's web version for demo porpuses resulted the best option.

> HomePage

![alt text](FrontEnd/public/media/homepage_simple.png)

> User Page (Offline mode)

![alt text](FrontEnd/public/media/UserPage_offline_mode.png)

On docker containers, the EngineServer uses Open Cv2 on Python3.11 with face_recognition modules and QOTT decoding for transfering information to the backend(Node.js - express app), front end(React Node) to be chaged to react-next.js on next version.

The system decodes a face recognition utilizing the 128 landkmarks and sends API call through Python engineServe to MongoDB(originally on SQL Server) to get the userID that will be fetched through SQL(thorugh the backEnd)L to get as a result a User object that contains the modular information of the person recognized, that will be served to the front-end.

Once the Identity of the user is confirmed, the back end will send a request to a mobile app, that will simply send a token to the app where the user will have to do a 2step verification, to confirm the access, on Y/N slection. with that response the back end will automatically send a response to the back end that will with cookies anable the users access to the navigation page, where the user could then give option to the console withput tpuching the screen, making it pasobiel for the user to clock in, change status, log out, etc.

![alt text](FrontEnd/public/media/branding_bg_ref.png)
