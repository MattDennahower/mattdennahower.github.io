
## Objective

This project involves web scraping in Python, followed by preprocessing, data cleaning, and exporting the data into a dataframe. Each English Premier League game is processed, with player statistics for each game saved to a dataframe and exported as a CSV file for further analysis.

<br>
Sample Data - 2023-2024 EPL Season Player Game Statistics

| Player         | #  | Nation | Pos | Age    | Min | Gls | Ast | PK | PKatt | Sh | SoT | CrdY | CrdR | Touches | Tkl | Int | Blocks | xG  | npxG | xAG | SCA | GCA | Cmp | Att | Cmp% | PrgP | Carries | PrgC | Att.1 | Succ | Team    |
| -------------- | -- | ------ | --- | ------ | --- | --- | --- | -- | ----- | -- | --- | ---- | ---- | ------- | --- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | ---- | ---- | ------- | ---- | ----- | ---- | ------- |
| Zeki Amdouni   | 25 | SUI    | FW  | 22-250 | 60  | 0   | 0   | 0  | 0     | 1  | 1   | 0    | 0    | 23      | 1   | 0   | 0      | 0   | 0    | 0   | 1   | 0   | 10  | 11  | 90.9 | 0    | 11      | 1    | 4     | 2    | Burnley |
| Anass Zaroury  | 19 | MAR    | FW  | 22-277 | 29  | 0   | 0   | 0  | 0     | 1  | 0   | 0    | 1    | 13      | 0   | 0   | 0      | 0   | 0    | 0   | 1   | 0   | 10  | 12  | 83.3 | 0    | 6       | 0    | 0     | 0    | Burnley |
| Lyle Foster    | 17 | RSA    | LM  | 22-342 | 89  | 0   | 0   | 0  | 0     | 2  | 0   | 0    | 0    | 37      | 2   | 0   | 2      | 0.1 | 0.1  | 0   | 3   | 0   | 14  | 20  | 70   | 2    | 14      | 2    | 3     | 1    | Burnley |
| Nathan Redmond | 15 | ENG    | LM  | 29-158 | 1   | 0   | 0   | 0  | 0     | 0  | 0   | 0    | 0    | 2       | 0   | 0   | 0      | 0   | 0    | 0   | 0   | 0   | 1   | 2   | 50   | 0    | 2       | 0    | 0     | 0    | Burnley |
| Josh Cullen    | 24 | IRL    | CM  | 27-126 | 90  | 0   | 0   | 0  | 0     | 0  | 0   | 0    | 0    | 46      | 1   | 0   | 1      | 0   | 0    | 0   | 0   | 0   | 37  | 43  | 86   | 2    | 16      | 0    | 0     | 0    | Burnley |

<br>

[![](https://img.shields.io/badge/Python-white?logo=Python)](#) [![](https://img.shields.io/badge/pandas-white?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMIAAAEDCAMAAABQ/CumAAAAeFBMVEX///8TB1QAAEb/ygDnBIgPAFLNzNYTAFnQ0NgMAFcAAETb2eP39/oUBlfV1N7/xwDmAID/9tfLydcjG17/4Yz//vbCwM3ykcL61OfoBIwyKmgAADYAAE0AAErx8PTIxdT/+un/34T85/Lyir/lAHv50eX+9fkpH2Ma8J+4AAACEklEQVR4nO3dzVIaQRSAUYNCEIGoiYmJivnP+79hFrmLVHELZ6pnmG483xqaPruh5lb32ZkkSZIkSZIkvb52z7dZU2+rT4uH2X6rx6m31afF7M1+87dTb6tPCDWEUEMINYRQQ5MS1tu0nqtMSrhKn26e1v1WmZawyn58g4DQL4QIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECOFA6cvM5a4nYb29yjoO4WmVvM58WPQkbF8e+RqPcDlPVp4t+xLS/W0QEBCqI8yTLpsizN8n/WmJ0CEEBAQEBAQEBIT2CF+/fci6a4hw8y7rvC3CeRYCAgICAgICAgICAgICwlCEtJYIdzdp/3+kdkKHToFQ+RjJMCEcCKF7CAdC6B7CgRC6Nylh9zGtJUJ6uNCsnsOFhhkvPAHC9x+fsloi/Pp5nXTREuH++iLpMwICAgICAgICAgICAgKC/87R7/u0lggdQkBAQEBAQEB4dYQON67UTqh9KuwkDlRBQED4R8gOF5o3Rdh8yepLGO0ez6MNPO+WQ9w3NilhvBAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyECKEshAihLIQIoSyEKJt+lL0SNeADUR4TG9cGWXHew10AkPP4aRBO9ohEuOFUEMINYRQQwg1dAKEDvd41t5t2u7lL0qSJEmSJEnSyfUXeomSFq0EzbkAAAAASUVORK5CYII=)](#)


Skills developed: Python (pandas - dataframes), Web Scraping - BeautifulSoup

Link : [epl_game_data](https://github.com/MattDennahower/mattdennahower.github.io/tree/main/docs/epl_web_scraping)

----
#### Project Board

2024-08-07 : 

- Creation of readme

----
#### Future work

1. Enhance the formatting and data cleaning process.

2. Incorporate additional visualizations from the data.