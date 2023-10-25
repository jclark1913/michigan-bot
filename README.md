<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<div align="center"><img src="./docs/main.png"></div>

<h3 align="center">Michigan Fact Bot</h3>

  <p align="center">
    <br />
    <a href="https://github.com/jclark1913/michigan-bot"><strong>View documentation »</strong></a>
    <br />
    <br />
    <a href="https://discord.com/api/oauth2/authorize?client_id=1146813156325339259&permissions=67110976&scope=bot">Discord invite link</a>
    ·
    <a href="https://github.com/jclark1913/michigan-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/jclark1913/michigan-bot/issues">Request Feature</a>
  </p>
</div>

<div align="center">

![Top Languages](https://img.shields.io/github/languages/top/jclark1913/michigan-bot)
![GitHub repo size](https://img.shields.io/github/repo-size/jclark1913/michigan-bot)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/jclark1913/michigan-bot)
![GitHub contributors](https://img.shields.io/github/contributors/jclark1913/michigan-bot)
![GitHub last commit](https://img.shields.io/github/last-commit/jclark1913/michigan-bot)
![GitHub issues](https://img.shields.io/github/issues/jclark1913/michigan-bot)
![GitHub](https://img.shields.io/github/license/jclark1913/michigan-bot)

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
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">

![Product Name Screen Shot][product-screenshot]

</div>

Michigan Bot is a simple discord bot I built to educate/annoy my friends. Invite it to your server and any time someone mentions "Michigan" the bot responds with trivia about the state. The bot itself is written in Python using the discord.py library, while the facts themselves are accessed via an <a href="https://github.com/jclark1913/michigan-facts-ts">API</a> I built in Typescript.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<div align="center">

![Python][Python]

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

You can invite Michigan Bot to your server using this <a href="https://discord.com/api/oauth2/authorize?client_id=1146813156325339259&permissions=67110976&scope=bot">invite link.</a>

If you want to build from source and create your own version, you'll need to set up an app and get a bot token in your personal discord account first.

To run the bot locally:

1. Clone repo and set up `.env`

```bash
git clone https://github.com/jclark1913/michigan-bot
cd michigan-bot
touch .env
```

2. Add the following to your `.env`:
```env
DISCORD_TOKEN = YOUR_DISCORD_TOKEN_HERE
```

3. Set up virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install dependencies

```bash
pip3 install -r requirements.txt
```

5. Run

```bash
python3 bot.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Justin Clark - [@JustinClarkJO](https://twitter.com/@JustinClarkJO) - jclarksummit AT gmail DOT com

Project Link: [https://github.com/jclark1913/michigan-bot](https://github.com/jclark1913/michigan-bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* All 5 of the Great Lakes
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jclark1913/michigan-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/jclark1913/michigan-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jclark1913/michigan-bot.svg?style=for-the-badge
[forks-url]: https://github.com/jclark1913/michigan-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/jclark1913/michigan-bot.svg?style=for-the-badge
[stars-url]: https://github.com/jclark1913/michigan-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/jclark1913/michigan-bot.svg?style=for-the-badge
[issues-url]: https://github.com/jclark1913/michigan-bot/issues
[license-shield]: https://img.shields.io/github/license/jclark1913/michigan-bot.svg?style=for-the-badge
[license-url]: https://github.com/jclark1913/michigan-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: docs/reply.png
[React]: https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=white
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white
[ElephantSQL]: https://img.shields.io/badge/ElephantSQL-2D9CDB?logo=elephantsql&logoColor=white
[Render]: https://img.shields.io/badge/Render-000000?logo=render&logoColor=white
[Express]: https://img.shields.io/badge/Express-000000?logo=express&logoColor=white
[Node.js]: https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=white
[React Router]: https://img.shields.io/badge/React_Router-CA4245?logo=react-router&logoColor=white
[Vercel]: https://img.shields.io/badge/vercel-%23000000.svg?&logo=vercel&logoColor=white
[TypeScript]: https://img.shields.io/badge/typescript-%23007ACC.svg?&logo=typescript&logoColor=white
[Prisma]: https://img.shields.io/badge/Prisma-3982CE?&logo=Prisma&logoColor=white
[ChatGPT]: https://img.shields.io/badge/chatGPT-74aa9c?&logo=openai&logoColor=white
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
